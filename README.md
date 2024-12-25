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

### Users 
- let userX, another_userY be a created users. Where X, Y are numbers.
- let group, another_group be a created groups for userX and userY respectively.
```py
from ecoi.core import users
from ecoi.core import groups

user1 = users.createUser(...)
user2 = users.createUser(...)

# Economic Operations of User
user1.wallet.read()
user1.wallet.addMoney(1000)
user1.wallet.getMoney()
user1.wallet.removeMoney(1000)
user1.wallet.clear()
user1.wallet.upgrade()

user1.safe.read()
user1.safe.addMoney(1000)
user1.safe.getMoney()
user1.safe.removeMoney(1000)
user1.safe.clear()
user1.safe.upgrade()

user1.banks.read()
user1Bank = user1.banks.getBank(bank_id)
acc_id = user1Bank.createAccount(bank_id, name, initial_amount=1000, ...)
user1Bank.getAccounts(bank_id).read()
user1Bank.getAccount(acc_id).read()
user1Bank.getAccount(acc_id).addMoney(1000)
user1Bank.getAccount(acc_id).getMoney()
user1Bank.getAccount(acc_id).removeMoney(1000)
user1Bank.getAccount(acc_id).borrowReq(1000, collateral)

lend_id = user1.requests.read(filter={
    "status": "pending",
    "fromType": "bank",
    "limit": 1,
    "details":{
        "bank_id": bank_id,
        "account_id": acc_id,
        "type": "borrow",
    }
}, query_vars=["lend_id"]
)["lend_id"]

user1Bank.getAccount(acc_id).borrow(1000, lend_id)
user1Bank.getAccount(acc_id).borrowClosure(lend_id, 1000)
user1Bank.getAccount(acc_id).clear()
user1Bank.getAccount(acc_id).upgrade()
user1Bank.delAccounts(acc_id)
user1.banks.delBank(bank_id)

user1.status.read()
user1.status.addStatus(link, ...)
user1.status.removeStatus()

# sending allerts
user1.allert.user(...)
user1.allert.users(...)
user1.allert.mods(...)
user1.allert.managers(...)
user1.allert.admins(...)
user1.allert.custom(...)

# checking allerts
user1.allerts.read(count=5)
user1.allerts.clear(allert_id)
user1.allerts.clearAll()
user1.allerts.deny(sender_id)
user1.allerts.denyAll()
user1.allerts.allow(sender_id)
user1.allerts.allowAll()
user1.allerts.allowedIds()
user1.allerts.deniedIds()

# Info Reading
user1.status.read(user2.user_id)
user1.followers.read(user2.user_id)
user1.following.read(user2.user_id)
user1.groupship.read(user2.user_id)
user1.profile.read(user2.user_id)
```
### Connections
```py
user1.follow(user2.user_id)
user1.unfollow(user2.user_id)
user1.followers.read(user2.user_id)
user1.following.read(user2.user_id)
user1.block(user2.user_id)
user1.unblock(user2.user_id)

user1.freq(user2.user_id) # if the other user also send friend request then it will be accepted
user1.freqlist.read()
user1.freqlist.clear(user2.user_id)
user1.freqlist.clearAll()
user1.friendship(user2.user_id)
user1.unfriend(user2.user_id)
# his own friendships
user1.friendships.read()

user1.friends.limit()
user1.friends.stop()

user1.followers.stop()
user1.followers.limit()

user1.report(user2.user_id, reason)

user1.confess(user2.user_id, message, amount)
user1.confesslist.read()
user1.confesslist.clear(user2.user_id)
user1.confesslist.clearAll()
user1.confesslist.deny(user2.user_id)
user1.confesslist.denyAll()

user1.connect(user2.user_id)
user1.disconnect(user2.user_id)
user1.connectlist.read(user2.user_id)

# entertainment
user1.hug(user2.user_id)
user1.cuddle(user2.user_id)
user1.pat(user2.user_id)
user1.poke(user2.user_id)
user1.slap(user2.user_id)
user1.tickle(user2.user_id)
user1.wink(user2.user_id)
user1.dance(user2.user_id)
user1.cry(user2.user_id)
user1.laugh(user2.user_id)
user1.smile(user2.user_id)
user1.wave(user2.user_id)
user1.punch(user2.user_id)
user1.kick(user2.user_id)
user1.play(user2.user_id)
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


print("The user1's groupship is:", user1.getGroupShip())
print("The user2's groupship is:", user2.getGroupShip())
print("The group's members are:", group.getMembers())
print("The group's owner's id is:", group.getOwnerId())
print("The group's info is: ", group.read())
print("The group's members info is: ", group.getMembersInfo(user_id))
```
### Others 
These will be planned soon.
```md
### Companies
### Banks
### Analytics
```