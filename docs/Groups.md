# Groups
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