# Network

## Tcp Retrance

#### Possible cause of tcp retrance

**Root cause**:
    a) the TCP-ACK sent back by the receiving end is lost in transmition
        b) the TCP-DATA sent by the transmitting end is lost on the path

        2. port buffer overflow, some packet will be dropped. That is to say, the network is busy.

        3. network load balance, some time is good, some time retrance will happen


**How to debug**

tools: traceroute, telnet, ping

Use traceroute to detect some feature:

1. large delay at particular hop


## Question

1. how does ping and traceroute work?
