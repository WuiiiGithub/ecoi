# Banks
## CURD+ Opperations
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
## Transaction CURD+ Operations
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