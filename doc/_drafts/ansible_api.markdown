
---
layout: post
title:  "Ansible API"
date:   2017-03-25 12:08:13 +0800
categories: jekyll update
---

# Premise

**version**: 2.3


# Class

loader


# Inventory
```
"""
return the vars in group_vars/<group name>
return the vars in host_vars/<host name>

type of return result is dict
"""
ivt.get_group_vars(<group object>, return_results=True)
ivt.get_host_vars(<host object>, return_results=True)

"""
dict from group name to group instance
"""
ivt.get_groups()

"""
get group by name
"""
ivt.get_group(<group name>)

ivt.get_hosts()
ivt.get_host(hostname)

```

# Group

"""
get child group, list
"""

**data members:**
- group.child_groups # list of group object
- group.name
- group.get_ancestors() # list of Group instance
- group.get_hosts() # all the host belongs to this group
- group.get_vars()
- group.hosts  # list of Host instance,  only direct hosts under this group

# Host
- host.get_groups()  # list of Group objects
- host.get_vars() # dict


Playbook


Executor


