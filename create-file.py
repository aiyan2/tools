import os
player = 'bob'

filename = player+'.txt'
seed = '012'
if os.path.exists(filename):
    append_write = 'a' # append if already exists
else:
    append_write = 'w' # make a new file if not
highscore = open(filename,append_write)
for i in range(500*400):
    
    highscore.write(seed)
highscore.close()
