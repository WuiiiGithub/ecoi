# Users 
Let userX, another_userY be a created users. Where X, Y are numbers respectively. Here, the operations which could be performed by users are grouped as follows:

```py
# related packages
from ecoi.core import users, groups, terminal
from ecoi.core.economy import *
from ecoi.core.social import *
```

## CURD+ Operations
```py
user = users.createUser(...)
user_id = user.user_id

user = users.getUser(user_id)

user.update(...)
user.upgrade(...)

readable_user = user.read(
    format = Literal['dict', 'bson'],
    print_console = Literal[True, False],
    ...
)

user.active()
user.energize()
user.exhaust()

user.report(reason)

user.block(
    reason = str
    ...
)

user.unblock(
    reason = str,
    ...
)

user.delete()
```

## Profile
```py
user.profile.read()
user.profile.update(...)

user.profile.updateName(...)
user.profile.updatePfp(...)
user.profile.updateStatus(...)
user.profile.updateBio(...)
user.profile.updateGender(...)
user.profile.updateLocation(...)
user.profile.updateBirthday(...)
user.profile.updateRelationship(...)
user.profile.updateOrientation(...)
user.profile.updateWork(...)
```
### Personality Type
```py
pers = user.profile.getPersonality()
pers.read()
pers.update(...)
```
#### MBTI Type
```py
pers.setMbti(...)
pers.updateMbti(...)
```
#### Dominance Type
```py
pers.setDom(...)
pers.updateDom(...)
```
#### Moral Alignment
```py
pers.setMoral(...)
pers.updateMoral(...)
```
#### Enneagram Type

##### Traditional
```py
pers.setEnneg(...)
pers.updateEnneg(...)
```
##### Temparement
```py
pers.setTempr(...)
pers.updateTempr(...)
```
##### Analytical Variant
```py
pers.setAnalytical(...)
pers.updateAnalytical(...)
```
##### Zodiac Sign
```py
pers.setZodiac(...)
pers.updateZodiac(...)
```
#### Mental Age
```py
pers.setMentalAge(...)
pers.updateMentalAge(...)
```


### Academics
```py
user.profile.academics.read()
user.profile.academics.update(...)
```
#### Projects
```py
user.profile.academics.projects.read()
user.profile.academics.projects.add(...)
user.profile.academics.projects.update(...)
user.profile.academics.projects.delete(...)
```
#### Skills
```py
user.profile.academics.skills.read()
user.profile.academics.skills.add(...)
user.profile.academics.skills.update(...)
user.profile.academics.skills.delete(...)
```
#### Certifications
```py
user.profile.academics.certifications.read()
user.profile.academics.certifications.add(...)
user.profile.academics.certifications.update(...)
user.profile.academics.certifications.delete(...)
```
#### Education
```py
user.profile.academics.education.read()
user.profile.academics.education.add(...)
user.profile.academics.education.update(...)
user.profile.academics.education.delete(...)
```
#### Work Experience
```py
user.profile.academics.workExp.read()
user.profile.academics.workExp.add(...)
user.profile.academics.workExp.update(...)
user.profile.academics.workExp.delete(...)
```

### Interests 
```py
user.profile.interests.read()
user.profile.interests.add(...)
user.profile.interests.update(...)
user.profile.interests.delete(...)
```

### Hobbies
```py
user.profile.hobbies.read()
user.profile.hobbies.add(...)
user.profile.hobbies.update(...)
user.profile.hobbies.delete(...)
```

### Ratings
```py
user.profile.ratings.read()
user.profile.ratings.add(...)
user.profile.ratings.remove(...)
user.profile.ratings.update(...)
user.profile.ratings.delete(...)
```

### Likes
```py
user.profile.likes.read()
user.profile.likes.add(...)
user.profile.likes.remove(...)
user.profile.likes.update(...)
user.profile.likes.delete(...)
```

### Views
```py
user.profile.views.read()
user.profile.views.view()
```

## Terminal
```py
user.terminal.read()
user.terminal.query(...)
user.terminal.setSelf(...)
user.terminal.setGlobal(...)
user.terminal.setGroupRole(...)
user.terminal.setCompanyRole(...)
```
## Jobs
```py
user.jobs.getJobs()
job = user.jobs.getJob(job_id)
job.read()

job.update(...)
job.delete()

job.getInfo()

user.jobs.getJobHistory()
```

## Requests
### Send Requests
```py
req = user1.requests.createRequest(...)
req_id = req.req_id

user1.requests.readAll(...)
req = user1.requests.getRequest(req_id)
req.update(...)

req.read(...)

req.draft()
req.send()

user1.requests.readSent()
req.delete()
```
### Recieve Requests
```py
user1.requests.readInbox(...)
req = user1.requests.getInbox(req_id)
# OR
req = user1.requests.getRequest(req_id)

# Some default request types
req.accept(...)
req.deny(...)
req.acknowledge(...)
req.report(...)

req.respond(...)
req.ignore(...)

req.block(...)

req.unblock(...)

req.delete()
```

## Social

### Connections
```py
user1.connect(user2.user_id)
user1.disconnect(user2.user_id)
user1.connectlist.read(user2.user_id)
user1.connectlist.clear(user2.user_id)  
user1.connectlist.clearAll()
```

### Followers
```py
user1.follow(user2.user_id)
user1.unfollow(user2.user_id)
user1.followers.read(user2.user_id)
user1.following.read(user2.user_id)
user1.followers.stop()
user1.followers.limit()
```

### Friends
```py
user1.freq(user2.user_id) # if the other user also send friend request then it will be accepted
user1.freqlist.read()
user1.freqlist.clear(user2.user_id)
user1.freqlist.clearAll()
user1.friendship(user2.user_id)
user1.unfriend(user2.user_id)
user1.friendships.read()
user1.friends.limit()
user1.friends.stop()
```

### Confessions
```py
user1.confess(user2.user_id, message, amount)
user1.confesslist.read()
user1.confesslist.clear(user2.user_id)
user1.confesslist.clearAll()
user1.confesslist.deny(user2.user_id)
user1.confesslist.denyAll()
```

### Entertainment
```py
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

## Info Reading
```py
user1.status.read(user2.user_id)
user1.followers.read(user2.user_id)
user1.following.read(user2.user_id)
user1.groupship.read(user2.user_id)
user1.profile.read(user2.user_id)
```

## Allerts
### Send Allerts
```py
user1.allert.user(...)
user1.allert.users(...)
user1.allert.mods(...)
user1.allert.managers(...)
user1.allert.admins(...)
user1.allert.custom(...)
```
### Check Allerts
```py
user1.allerts.read(count=5)
user1.allerts.clear(allert_id)
user1.allerts.clearAll()
user1.allerts.deny(sender_id)
user1.allerts.denyAll()
user1.allerts.allow(sender_id)
user1.allerts.allowAll()
user1.allerts.allowedIds()
user1.allerts.deniedIds()
```

## Economic Operations
### Wallet
```py
user1.wallet.read()
user1.wallet.addMoney(1000)
user1.wallet.getMoney()
user1.wallet.removeMoney(1000)
user1.wallet.clear()
user1.wallet.upgrade()
```
### Safe
```py
user1.safe.read()
user1.safe.addMoney(1000)
user1.safe.getMoney()
user1.safe.removeMoney(1000)
user1.safe.clear()
user1.safe.upgrade()
```

### Banks
```py
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
```