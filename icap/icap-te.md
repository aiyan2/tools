 Mesg Encapsulating
 =========
The ICAP encapsulation model is a lightweight means of packaging any number of HTTP message sections into an encapsulating ICAP message-body, in order to allow the vectoring of requests, responses, and request/response pairs to an ICAP server.
For example, the header 
```
Encapsulated: req-hdr=0, res-hdr=80, res-body=2100
``` 
indicates a message that encapsulates a group of request headers, a group of response headers, and then a response body.  Each of these is included at the byte-offsets listed.

Methods
--------
### Option

### REQMOD 

### RESPMOD

### PREVIEW 
( to use OPTION to notify how many bytes for preview)
