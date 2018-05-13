---
title: cgroup
categories: []
---

# Related Command

- ss, ip, iptable
- unshare
- bridge, brctl


**Command**
```
ip link add veth0 type veth peer name veth1
ip netns exec ns1 ip link set dev veth1 up
ip link set veth1 netns <namespace>
ip route change to default dev eth0 via {{ ansible_eth0.ipv4.address }} # set default eth
```

ss
```
ss -atp
```

**Config**

/etc/sysconfig/network-scripts/ifcfg-eth0


**Add a IP Address**
```
# it may lost on system restart
ip addr add 192.168.50.5 dev eth1
```

# Veth

Setting up their IP addresses and routing rules accordingly, plus enabling NAT
in the host side, will be enough to provide Internet access to the network
namespace.

**IP Forwarding**
```
IP forwarding is what routers do: take an IP packet, figure out where it should
go next, and then push (forward) it to the next router along the path.
```

## Steps

Now it’s necessary we make all external traffic leaving ns1 to go through v-eth1.
```
ip netns exec ns1 ip route add default via 10.200.1.1
```

# Terminology

**NAT**
Network Address Translation (NAT) is the process where a network device, usually
a firewall, assigns a public address to a computer (or group of computers) inside
a private network. The main use of NAT is to limit the number of public IP
addresses an organization or company must use, for both economy and security
purposes.

**Forward**

**** 

# Reference


Linux Namespace API
CGroup
LXC
Docker



https://blogs.igalia.com/dpino/2016/04/10/network-namespaces/

[Reading Routes and IP Information](http://linux-ip.net/html/basic-reading.html)


