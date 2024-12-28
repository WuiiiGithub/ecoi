# Requests
```py
from ecoi.core import requests

req = requests.createRequest(...)
req_id = req.req_id

req = requests.getRequest(req_id)

req.update(...)

req.upgrade(...)
req.read(...)

req.delete()
```