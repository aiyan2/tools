import random
import string
import uuid
import time
import argparse
import os
import json
import sys

import subprocess 

class DataTuple(object):
# http request type
    GET = 0
    POST = 1


class Configurations(object):

    def __init__(self):
        self.connections = []
        self.tmp_pars = '' # tmp storage 

    def add_connection(self, connection):
        self.connections.append(connection)


def generate_random_data(length_range):
    def random_string(length):
        alphabet = string.ascii_letters
        data = ''.join(random.choice(alphabet) for i in range(length))
        return data

    length = random.randint(length_range[0], length_range[1])
    return random_string(length)


# generate txt file for file filter, file size etc test cases
def handle_random_data_query(conf, tuple):
    no_of_files = int(tuple['no_of_files'])
    for i in range(no_of_files):
        print(f"\n\nGenerating file no {i} out of {no_of_files}")
        filename = "loader_" + str(time.time()) + ".txt"
        file_data = generate_random_data([1 , int(tuple['max_len'])]).encode("utf-8")
        print(f"file {filename} is read with size {len(file_data)}")
        sent = handle_file_communication(conf, tuple, filename, file_data)
        if sent:
            print("Randomly generated file sent successfully")
        else:
            print(f"ERROR: file integrity check failed", file=sys.stderr)


## map args to curl http version            
def ver_map(conf):
    print ("conf.httpver:"+conf.httpver)
    if conf.httpver == "2":
        cver = "--http2"
    elif conf.httpver =="1.0":
        cver = "--http1.0"
    else: 
        cver ="--http1.1"
    return cver 
def auth_map(conf,tuple):
    # preserve = False if 'preserve' not in tuple else True if tuple['preserve'] == 1 else False
    if conf.proxy:
        user = " --proxy-user "
    else:
        user = " -U "    
    return user    
##@todo: other auth to be implimented 


def handle_run(conf,tuple):
    pars = conf.uri+" "+ver_map(conf)+conf.tmp_pars
    if conf.proxy:
        pars +=" -x " +conf.proxy 
        pars += auth_map(conf, tuple)+ conf.username +":"+conf.password 
    print ("curl -k "+pars);

    p = subprocess.Popen("curl -k  "+pars, stdout=subprocess.PIPE, shell=True)
    print(p.communicate())

    # curl -x 172.18.43.67:8080 https://172.18.43.100 --proxy-user u1:12345678
    # curl -v https://www.cnn.com -k --http1.1  -d /etc/hosts -x 172.18.43.67:8080 --proxy-user u3:12345678
    # smb@krb5:~/enghttp/mt$ python3 enghttp.py --uri https://172.18.43.100  --username u1 --password 12345678 --data-tuples pc100tuple.txt  --proxy 172.18.43.67:8080


def handle_get(conf, tuple):
    conf.uri = args.uri
    conf.uri += tuple['file_id'] # add file_id to get  
    conf.tmp_pars = ""  
    
    ### MUST try and catch it one by one otherwise
    
    try:  
        if tuple['output'] == 1:
            conf.tmp_pars = ' -o /tmp/http_get_big '        
    except KeyError as e:  
        print ("missing key:")
        print (e)
        pass  

    try:  
        if tuple['web_filter'] == 1:            
            conf.uri = "https://www.ibm.com"
    except KeyError as e:  
        print ("missing key:")
        print (e)
        pass  
        
    finally:
        handle_run(conf,tuple)    
        
def handle_post(conf, tuple):
    mfile = tuple['file_id']
    print("file is:"+mfile + "& tuple['form_urlencode']")
    print(tuple['form_urlencode'])
    if tuple['form_urlencode'] == 0:  # multi-part, it's int of 0
        pars = " -F file=@"+mfile
    else:
        pars = " -d "+mfile 
    

    conf.tmp_pars = pars      
    handle_run(conf, tuple)    

def process_data_tuple(conf, tuple):
    type = tuple['type']
    if type == DataTuple.GET:
        print(f"http get")
        handle_get(conf, tuple)
    elif type == DataTuple.POST:
        print(f"http post")
        handle_post(conf, tuple)


if __name__ == '__main__':
    cmd_parser = argparse.ArgumentParser(description="Http server and user information.")
    cmd_parser.add_argument("--uri", required=True, help="http/s uri, i.e. https://www.cnn.com")
    #cmd_parser.add_argument("--port", type=int, required=True, help="Server Port, http and https distinguish", default=443)
    cmd_parser.add_argument("--username", required=False, help="Username")
    cmd_parser.add_argument("--password", required=False, help="Password")
    cmd_parser.add_argument("--proxy", required=False, help="proxy ip:port")
    cmd_parser.add_argument("--version", type=str, default="1.1", help=" Http version "
                                                                          "0.9 = HTTP/0.9, "
                                                                          "1.0 = HTTP/1.0, "
                                                                          "1.1 = HTTP/1.1,  "
                                                                          "2 = HTTP/2,  "
                                                                          "Post2 = Post-Htpp/2 "
                                                                          "3 = HTTP/3")
  #  curl -v https://www.cnn.com -I -k --http1.1  for http1.1, 
    cmd_parser.add_argument("--data-tuples", required=True, help="The data tuples themselves")
    
    args = cmd_parser.parse_args()
   
    #share = r"\\%s\%s" % (server, args.share)
    conf = Configurations()
    conf.uri = args.uri
    conf.username = args.username
    conf.password = args.password
    conf.proxy = args.proxy
    conf.httpver = args.version

    try:
        ###
        with open(args.data_tuples, "r") as data_tuple_file:
            data_tuples = json.loads(data_tuple_file.read())

        counter = 1
        for key, value in zip (data_tuples.keys(), data_tuples.values()):
            #random.seed(args.seed)
            print(f"\n \nProcessing data tuple of key '{key}' and value \n {value} \n\n")
            process_data_tuple(conf, value)

        # test argus 
        print (conf.password)
        print (conf.httpver)
    finally:
        # connection.disconnect(True)
        print("DONE!")

"""
smb@krb5:~/enghttp/mt$ python3 enghttp.py --uri https://172.18.43.100  --username u1 --password 12345678 --data-tuples pc100tuple.txt  --proxy 172.18.43.67:8080 > log
{"http-get": {"connection_id":0, "session_id":0, "tree_id":0, "compound":1, "type":0, "file_id":"/", "range":"none", "output":0},

 "http-get-av": {"connection_id":0, "session_id":0, "tree_id":0, "compound":0, "type":0,  "file_id":"/eicar.com.1",  "range":"none", "output":0},
 
 "http-post-multipart": {"connection_id":0, "session_id":0, "tree_id":0, "compound":0, "type":1, "form_urlencode":0, "file_id":"./enghttp.py", "range":"none", "output":0},
 
 "http-get-big": {"connection_id":0, "session_id":0, "tree_id":0, "compound":0, "type":0,  "file_id":"/test/4m",  "range":"none", "output":1},
 
 "http-webfilter": {"connection_id":0, "session_id":0, "tree_id":0, "compound":0, "type":0,  "file_id":"/",  "web_filter":1, "output":0},
 
 "http-post-form": {"connection_id":0, "session_id":0, "tree_id":0, "compound":0, "type":1,  "form_urlencode":1, "file_id":"/etc/hosts", "range":"none", "output":0}, 
 
 "http-post-av": {"connection_id":0, "session_id":0, "tree_id":0, "compound":0, "type":1, "form_urlencode":1, "file_id":"./eicar.com.1", "range":"none", "output":0},
 
 "http-post-big": {"connection_id":0, "session_id":0, "tree_id":0, "compound":0, "type":1,  "form_urlencode":1, "file_id":"./10g", "range":"none", "output":0}
 }
 
aiyan@pc100:~/myweb$ nghttpd 8448 -v ./key.pem ./cert.pem -d /var/www/html/


 
"""
