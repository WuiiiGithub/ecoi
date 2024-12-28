# Companies 
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