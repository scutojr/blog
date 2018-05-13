---
title: diagnostic
categories: []
---

# Network

## Tcp Retrance

#### Possible cause of tcp retrans

**Root cause**:
    a) the TCP-ACK sent back by the receiving end is lost in transmition
        b) the TCP-DATA sent by the transmitting end is lost on the path

        2. port buffer overflow, some packet will be dropped. That is to say, the network is busy.

        3. network load balance, some time is good, some time retrance will happen

    In a word, it's because of network congestion, tcp retrans is merely a symptom.

    Cause of congestion: ethernet, network, and multicast broadcasts


**Related Config**
[RTO](https://www.extrahop.com/company/blog/2016/retransmission-timeouts-rtos-application-performance-degradation/)

**How to calculate?**

refer to example of ganglia


**Impact**
1. increase delay


**How to debug**

tools: traceroute, telnet, ping

Use traceroute to detect some feature:

1. large delay at particular hop



Unless you've gathered **network trace**, this is difficult to prove


## Question

1. how does ping and traceroute work?

2. what is fast retransmits, forward retransmits, retransmits in slow start, sack retransmits failed?
```
netstat -s |grep fast
```
