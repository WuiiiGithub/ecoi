# Banks

The `economy.banks` module provides a secure, ethical, and feature-rich banking system, avoiding debt traps while enabling profit-sharing and efficient management of funds. Below is the detailed API design with all possible classes, attributes, and methods.

---

## Bank Features and Operations

### Bank Creation and Management
```python
# Create a new bank
bank = economy.banks.createBank(
    name: str,  # Name of the bank
    profit_sharing_enabled: bool = False,  # Whether profit-sharing is enabled
    description: str = None,  # Optional description of the bank
)

# Retrieve an existing bank
bank = economy.banks.getBank(bank_id)

# Update bank details
bank.update(
    name: str = None,
    profit_sharing_enabled: bool = None,
    description: str = None,
)

# Read bank details
bank_info = bank.read(
    query_vars: list = ["bank_id", "name", "profit_sharing_enabled", "description"]
)

# Delete a bank
bank.delete()
```


### Bank Operations
```python
# Enable or disable profit-sharing at the bank level
bank.enableProfitSharing()
bank.disableProfitSharing()

# Block or unblock a bank
bank.block(reason: str = None)
bank.unblock()

# Add or remove users from the bank
bank.addUser(user_id: str)
bank.removeUser(user_id: str)

# Get a list of all users associated with the bank
users = bank.getUsers(
    filter: dict = None,  # Filter conditions (e.g., "investment_enabled": True)
    limit: int = 100,
)
```

---

## Account Features and Operations

### Account Creation and Management
```python
# Create a user account within a bank
account = bank.createAccount(
    user_id: str,
    initial_deposit: float = 0.0,
    is_investment_enabled: bool = False,
)

# Retrieve an existing account
account = bank.getAccount(account_id)

# Update account details
account.update(
    is_investment_enabled: bool = None,
)

# Delete an account
account.delete()
```


### Account Operations
```python
# Deposit or withdraw money
account.deposit(amount: float)
account.withdraw(amount: float)

# Clear all funds from the account
account.clear()

# Enable or disable investments for the account
account.enableInvestment()
account.disableInvestment()

# Retrieve account information
account_info = account.read(
    query_vars: list = ["account_id", "balance", "is_investment_enabled"]
)

# Get account balance
balance = account.getBalance()
```


## Transaction Features and Operations

### Transaction Creation and Management
```python
# Create a new transaction
transaction = account.createTransaction(
    amount: float,
    transaction_type: str,  # e.g., "deposit", "withdrawal", "profit-sharing"
)

# Retrieve an existing transaction
transaction = account.getTransaction(transaction_id)

# Update transaction details
transaction.update(
    status: str = None,  # e.g., "completed", "canceled"
)

# Read transaction details
transaction_info = transaction.read(
    query_vars: list = ["transaction_id", "amount", "status", "type"]
)

# Delete a transaction
transaction.delete()
```


### Transaction Operations
```python
# Complete or cancel a transaction
transaction.complete()
transaction.cancel()

# Refund a transaction
transaction.refund()

# Block or unblock a transaction
transaction.block(reason: str = None)
transaction.unblock()

# Close or reopen a transaction
transaction.close()
transaction.open()
```

---

## Profit-Sharing and Investments

### Bank-Level Profit Sharing
```python
# View investment portfolio
portfolio = bank.getInvestmentPortfolio()

# Distribute profit among accounts
bank.distributeProfit(
    total_profit: float,
    distribution_method: str = "equal",  # or "proportional"
)
```


### Account-Level Investment Controls
```python
# Enable or disable investments for an account
account.enableInvestment()
account.disableInvestment()

# View profit-sharing details
profit_details = account.getProfitDetails(
    query_vars: list = ["total_invested", "total_profit", "share"]
)
```

---

## Reporting and Notifications

### Reporting Features
```python
# Generate a bank-level report
report = bank.generateReport(
    start_date: datetime,
    end_date: datetime,
    filters: dict = None,  # e.g., {"type": "investment"}
)

# Generate an account-level report
account_report = account.generateReport(
    start_date: datetime,
    end_date: datetime,
    filters: dict = None,
)
```

### Notifications
```python
# Send notifications to users
bank.notifyUsers(
    message: str,
    user_ids: list = None,  # Notify specific users, or
    group: str = "all",  # Notify all users
)
```

---

## Security and Compliance

### Fraud Detection and Account Freezing
```python
# Monitor suspicious activities
suspicious_activities = bank.monitorSuspiciousActivities()

# Freeze or unfreeze an account
account.freeze(reason: str = None)
account.unfreeze()
```

### Audit and Compliance Checks
```python
# Run an audit on the bank
audit_report = bank.audit()

# Check compliance status
compliance_status = bank.getComplianceStatus()
```