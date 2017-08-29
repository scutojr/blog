

---

layout: post
title:  "Cgroups and Namespace"
date:   2017-03-25 12:08:13 +0800
categories: jekyll update

---

# Cgroups

To put it simple, cgroups are a metering and limiting mechanism, they control 
how much of a system resource (CPU, memory) you can use. On the other hand, 
namespaces limit what you can see. Thanks to namespaces processes have their 
own view of the system’s resources.

## Subsystem


## How to use cgroup?

command
- cgexec
```
cgexec -g blkio:test1 dd if=file-abc of=/dev/null
```
- 

configuration

subsystem


# Namespace

Network namespaces



---


# Usage

**Tools**
- nsenter


# Reference

> https://blogs.igalia.com/dpino/2016/04/10/network-namespaces/

> [Network Namespace](http://cizixs.com/2017/02/10/network-virtualization-network-namespace)

