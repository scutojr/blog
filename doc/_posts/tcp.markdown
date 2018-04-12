

# Tcp keep alive

There are three configurable properties that determine how Keep-Alives work. On Linux they are1:

**tcp_keepalive_time**
    default 7200 seconds
**tcp_keepalive_probes**
    default 9
**tcp_keepalive_intvl**
    default 75 seconds

The process works like this:

1. Client opens TCP connection
2. If the connection is silent for tcp_keepalive_time seconds, send a single empty ACK packet.1
3. Did the server respond with a corresponding ACK of its own?
**No**
Wait tcp_keepalive_intvl seconds, then send another ACK
Repeat until the number of ACK probes that have been sent equals tcp_keepalive_probes.
If no response has been received at this point, send a RST and terminate the connection.

**Yes**: Return to step 2


# How to configure on os level
```
sysctl -w net.ipv4.tcp_keepalive_time=60
sysctl -w net.ipv4.tcp_keepalive_intvl=20
```


# TCP heartbeat


**environment**: QLB ---> Nginx API Gatewy ---> Upstream Server


**why**
- Checking for dead peers
- Preventing disconnection due to network inactivity
- reclaim network resource if connection is idle



You will not get far with the built-in keep-alives of the TCP stack. That's because the keep-alive interval cannot be tuned by your application, it is set by the OS, and the defaults are rather high (hours). This is not specific to Java.




