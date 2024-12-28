# Advertisement
## General Advertisements
```py
from ecoi.core.economy import advertisements

adv = advertisements.createAdv(...)
adv_id = adv.id

adv.update(...)
adv.read()

adv.draft(...)
adv.publish(...)

adv.block(...)
adv.unblock(...)

adv.delete(...)
```
## Advertisement Campaign
```
advCampaign = company.createAdvCampaign(...)
advCampaign.upgrade(...)

advCampaign_id = advCampaign.id

advCampaign.update(...)
advCampaign.read()

advCampaign.start(...)
advCampaign.end(...)

advCampaign.block(...)
advCampaign.unblock(...)

advCampaign.delete(...)
```