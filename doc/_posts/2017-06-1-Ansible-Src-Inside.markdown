---
layout: post
title:  "Yarn FS"
date:   2017-03-25 12:08:13 +0800
categories: jekyll update
---

# Ansible Source Invetigation


# Summary


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
