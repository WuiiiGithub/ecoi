# Magic Cards 
## CURD+ Operations
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