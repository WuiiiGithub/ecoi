# Products
## Item 
### CURD+ Operations
```py
item = economy.createItem(...)
item_id = item.item_id

item = economy.getItem(item_id)

item.update(...)

readable_item = item.read(...)

item.block(...)
item.unblock(...)

item.delete(...)
```
## Service 
### CURD+ Operations
```py
service = economy.createService(...)

service_id = service.service_id
service = economy.getService(service_id)

service.update(...)

readable_service = service.read(...)

service.block(...)
service.unblock(...)

service.delete(...)
```