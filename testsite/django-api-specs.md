## Auth

### Login

url: root/api/login?username=kyabia&password=kyabia
method: GET
parameters: username, password
returns: JSON response with keys user_id and username.
status code: 200 if login is successful, otherwise 403.

### Signup

url: root/api/signup?

Not implemented yet

### Logout

url: root/api/logout

Not implemented yet


## Messaging

### Save Message

url: root/message-save
method: POST
data:
  - msg_content: str
  - sender_id: int
  - receiver_id: int

### Load Message

url: root/message-load?sender_id=[int]&receiver_id=[int]
method: GET
parameters:
  - sender_id: int
  - receiver_id: int

### Load Chatlist

url: root/chatlist-load
method: GET
parameters:
  - user_id: int
