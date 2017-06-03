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


## Coding Skill


## Question

1. Is fact cached in Inventory?
