# Ecoi Package
The aim of this package is to do some buisness operations without the use of real money. And use the artificial digital currency as an exchange.

---

## Package Usage Structure - Future
Lets say a user is importing and using it then it should be something like this in future.

### Basic Structure
```py
import ecoi
from ecoi import config

db = config.dbConfig.getDB() 
# or config.dbConfig.getDB() 

config.vslConfig.runAnalyticsServer()
# runs analytics dash-server in background
```

### CURD+ Operations
#### User CURD+ Operations
```py
from ecoi.core import users 

user = users.createUser(...)
user_id = user.user_id

user = users.getUser(user_id)
user.update(
    # name = str,
    # email = str,
    # bio = str,
    # profile_pic = str,
    ... 
)

readable_user = user.read(
    # format = Literal['dict', 'bson'],
    # print_console = True|False
    ...
)

user.user_block(
    # reason = str
    # by_user_id = str
    ...
)

user.group_block(
    # reason = str
    # by_user_id = str
    ...
)

user.user_unblock(
    # by_user_id = str
    # reason = str
    ...
)
user.group_unblock(
    # by_user_id = str
    # reason = str
    ...
)

user.block(
    # reason = str
    ...
)

user.unblock(
    # reason = str
    ...
)
# owners of the package
user.delete() # or deleted_user = user.delete()
```
#### Group CURD+ Operations
```py
from ecoi.core import groups

group = groups.createGroup(...)
group_id = group.group_id

group = groups.getGroup(group_id)

readable_group = group.read(...)

group.update(...)

group.block(...)
group.unblock(...)

group.delete()
```
#### Economy CURD+ Operations
##### Medium of Exchange CURD+ Operations
```py
from ecoi.core import economy
# MOE means Medium of Exchange
moe = economy.createMOE(...)
moe_id = moe.moe_id

moe = economy.getMOE(moe_id)

moe.update(...)

readable_moe = moe.read(...)

moe.block(...)
moe.unblock(...)

moe.delete(...)
```
##### Item CURD+ Operations
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
##### Service CURD+ Operations
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
##### Magic Cards CURD+ Operations
```py
magic_card = economy.createMagicCard(...)
magic_card_id = magic_card.magic_card_id

magic_card = economy.getMagicCard(magic_card_id)

magic_card.update(...)

readable_magic_card = magic_card.read(...)

magic_card.block(...)
magic_card.unblock(...)

magic_card.delete(...)
```
##### Advertisements CURD+ Operations
```py
advertisement = economy.createAdvertisement(...)
advertisement_id = advertisement.advertisement_id

advertisement = economy.getAdvertisement(advertisement_id)

advertisement.update(...)

readable_advertisement = advertisement.read(...)

advertisement.block(...)
advertisement.unblock(...)

advertisement.delete(...)
```
##### Transaction CURD+ Operations
```py
transaction = economy.createTransaction(...)
transaction_id = transaction.transaction_id

transaction = economy.getTransaction(transaction_id)

transaction.update(...)

transaction.cancel(...)
transaction.complete(...)
transaction.refund(...)
transaction.close(...)

transaction.open(...)

readable_transaction = transaction.read(...)

transaction.block(...)
transaction.unblock(...)

transaction.delete(...)
```
##### Bank CURD+ Operations
```py
bank = economy.createBank(...)
bank_id = bank.bank_id

bank = economy.getBank(bank_id)

bank.update(...)

readable_bank = bank.read(...)

bank.block(...)
bank.unblock(...)
bank.delete(...)
```
... similary others

### Users & Connections
```diff
+Users and Connections Docs shifted to ./docs/Users.md
```
### Groups
```py
group = groups.createGroup(..., owner_id=user1.user_id)
user2.reqGroupShip(group.group_id)
owner_id = group.getOwnerId()
owner = users.getUser(owner_id)
isAccepted = owner.requests.read(filter={
    "status": "pending",
    "fromType": "group",
    "limit": 1,
    "details":{
        "group_id": group.group_id,
        "type": "join",
        "user_id": user2.user_id,
    }
}, query_vars=["isAccepted"]).respond(True)
group.addMember(user2.user_id)

group.createSubGroup(...)
group.getSubGroups()
group.getSubGroup(sub_group_id)
group.deleteSubGroup(sub_group_id)
group.updateSubGroup(sub_group_id, ...)

group.read()
user1.getGroupShip()
group.getMembersInfo(user_id)
group.getMembers()
group.getOwnerId()


# Roles
role = group.createRole(name, ...)
role_id = role.id

role.update(...)

role.addMember(...)
role.memberInfo(...)
role.removeMember(...)
role.permissions(...).read()
role.permissions(...).add(...)
role.permissions(...).remove(...)
role.permissions(...).clear(...)
role.permissions(...).update(...)

role.block(...)
role.unblock(...)

role.delete(...)
```
### Advertisement
```py
from ecoi.core.economy import advertisements

adv = advertisements.createAdv(...)
adv_id = adv.id

adv.update(...)
adv.read()

adv.draft(...)
adv.publish(...)

advCampaign = company.createAdvCampaign(...)
advCampaign.upgrade(...)

advCampaign_id = advCampaign.id

advCampaign.update(...)
advCampaign.read()

advCampaign.start(...)
advCampaign.end(...)

advCampaign.delete(...)
```
### Companies 
```py
from ecoi.core import companies

company = companies.createCompany(...)
company_id = company.id

company = companies.getCompany(company_id)

company.read()

company.update(...)

company.hireEmployee(...)
company.fireEmployee(...)
company.getEmployees(...)
company.getEmployeeInfo(...)
company.advertise(...)
company.startAdvCampaign(...)
company.endAdvCampaign(...)

company.advertise(...)

company.contract(...)
company.breakContract(...)

role = company.createRole(...)
role_id = role.id

company.getRole(...)
company.getRoles(...)

# roles within the company
role.update(...)
role.addEmployee(...)
role.removeEmployee(...)
role.permissions(...).read()
role.permissions(...).add(...)
role.permissions(...).remove(...)
role.permissions(...).update(...)
role.permissions(...).clear(...)
role.block(...)
role.unblock(...)
role.delete(...)

# Salary or Giving something to Employee or Role
company.giveEmployee(...)
company.payEmployee(...)
company.giveRole(...)
company.payRole(...)

# Company Buisness Operations
item = company.createItem(...)
item_id = item.id

company.getItems(...)
company.getItem(item_id, ...)

item.updateItem(...)
company.deleteItem(item_id, ...)

company.sellItem(...)
company.buyItem(...)

service = company.createService(...)
service_id = service.id
company.getServices(...)
company.getService(service_id, ...)
company.updateService(...)
company.deleteService(...)
company.sellService(...)
company.buyService(...)

company.createMagicCard(...)
company.getMagicCards(...)
company.getMagicCard(...)
company.updateMagicCard(...)
company.deleteMagicCard(...)
company.sellMagicCard(...)
company.buyMagicCard(...)


# Collaborations
company.collab(...)
company.breakCollab(...)

company.block(...)
company.unblock(...)

company.delete(...)
```
```md
### Others
```py
from ecoi.core.economy import items, services

item = items.createItem(...)
item_id = item.id

item = items.getItem(item_id)



service = services.createService(...)
```
### Requests
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
### Banks
### Analytics
```