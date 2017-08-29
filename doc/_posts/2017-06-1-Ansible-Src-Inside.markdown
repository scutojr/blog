---
layout: post
title:  "Ansible Investigation"
date:   2017-03-25 12:08:13 +0800
categories: jekyll update
---

# Ansible Source Invetigation


# Summary

## Class Structure

InventoryManager
    ----> InventoryData

InventoryData
    ----> *Group
    ----> *Host

## Ansible Hack

special host variables:
    - inventory_file
    - inventory_dir

## Special Inventory

group_vars/, host_vars and var plugin

## Pattern

pattern is used in playbook after hosts field so as to select hosts satisfied the pattern

supportted pattern:
- raw
- difference !
- intersection &
- subscript such as DataNode[10], DataNode[1:10], DataNode[01:10]
- regular expression
- regular expression began with ~ will ignore subscript


```
# select hosts that is NameNode and ZooKeeper but not HMaster
- hosts: NameNode:!HMaster:&ZooKeeper

# select the first 10 DataNode
- hosts: DataNode[10]
```

## Playbook
    - 'include' is taggable and conditional


## Coding Skill

### Design Skill
    Include syntax is modeled by class PlaybookInclude. User can add condition, tags and vars to tasks and
    include statement, so It's reasonable to create super class Conditional and Taggable for PalybookInclude

## Usage Skill

### Play descriptor

```
    _name                = FieldAttribute(isa='string', default='', always_post_validate=True)

    # TODO: generalize connection
    _accelerate          = FieldAttribute(isa='bool', default=False, always_post_validate=True)
    _accelerate_ipv6     = FieldAttribute(isa='bool', default=False, always_post_validate=True)
    _accelerate_port     = FieldAttribute(isa='int', default=5099, always_post_validate=True)

    # Connection
    _fact_path           = FieldAttribute(isa='string', default=None)
    _gather_facts        = FieldAttribute(isa='bool', default=None, always_post_validate=True)
    _gather_subset       = FieldAttribute(isa='barelist', default=None, always_post_validate=True)
    _gather_timeout      = FieldAttribute(isa='int', default=None, always_post_validate=True)
    _hosts               = FieldAttribute(isa='list', required=True, listof=string_types, always_post_validate=True)

    # Variable Attributes
    _vars_files          = FieldAttribute(isa='list', default=[], priority=99)
    _vars_prompt         = FieldAttribute(isa='list', default=[], always_post_validate=True)
    _vault_password      = FieldAttribute(isa='string', always_post_validate=True)

    # Role Attributes
    _roles               = FieldAttribute(isa='list', default=[], priority=90)

    # Block (Task) Lists Attributes
    _handlers            = FieldAttribute(isa='list', default=[])
    _pre_tasks           = FieldAttribute(isa='list', default=[])
    _post_tasks          = FieldAttribute(isa='list', default=[])
    _tasks               = FieldAttribute(isa='list', default=[])

    # Flag/Setting Attributes
    _force_handlers      = FieldAttribute(isa='bool', always_post_validate=True)
    _max_fail_percentage = FieldAttribute(isa='percent', always_post_validate=True)
    _serial              = FieldAttribute(isa='list', default=[], always_post_validate=True)
    strategy: String
        linear: batch run
        free: each host run as fast as it can
    _order               = FieldAttribute(isa='string', always_post_validate=True)

```

## Question

1. Is fact cached in Inventory?
2. How to add timeout to fact gathering?
3. How to discover and clean the dead worker?
