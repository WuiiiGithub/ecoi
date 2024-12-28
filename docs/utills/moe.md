# Medium of Exchange 
## CURD+ Operations
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