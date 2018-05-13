---

title:  "Cgroups and Namespace"
categories: jekyll update

---

# Cgroups

To put it simple, cgroups are a metering and limiting mechanism, they control 
how much of a system resource (CPU, memory) you can use. On the other hand, 
namespaces limit what you can see. Thanks to namespaces processes have their 
own view of the system’s resources.

## Subsystem

*hierarchy*: combination of subsystem. subsystem can only be part of single hierarchy

*control group*: subdirectory of the hierarchy, it further limit the resource of its task other than the configuration of its parent group


## How to use cgroup?

*Command*

- cgexec
```
cgexec -g blkio:test1 dd if=file-abc of=/dev/null
```

- cgdelete subsystems:path
```
where:
    subsystems is a comma‑separated list of subsystems.
    path is the path to the cgroup relative to the root of the hierarchy.

As i know, this command will echo msg like 'cgdelete: cannot remove group 'hubble-agent': No such file or directory', but it succeeds most of the time
```

- create a control group
```
cgcreate -t uid:gid -a uid:gid -g controllers:path
```
controllers is not necessary to the subsystem combination


- lssubsys

lscgroup

configuration

subsystem


### other

1. /proc/<pid>/cgroup provides with list of hierarchy and corresponding control group that this process belongs to


# Namespace

Network namespaces



---


# Usage

**Tools**
- nsenter


# Reference

> https://blogs.igalia.com/dpino/2016/04/10/network-namespaces/

> [Network Namespace](http://cizixs.com/2017/02/10/network-virtualization-network-namespace)









---

# temporary note from youdao




## terminlogy in cgroup:
    1. https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/resource_management_guide/sec-relationships_between_subsystems_hierarchies_control_groups_and_tasks
    2. usage and tools
    https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/resource_management_guide/sec-default_cgroup_hierarchies
    
### hierarchy
### group
### subsystem
### controllers
    
    
    
    Never use libcgropup tools to modify the default hierarchies mounted by systemd since it would lead to unexpected behavior. The libcgroup library will be removed in future versions of Red Hat Enterprise Linux. 


systemd  https://linuxaria.com/article/how-to-manage-processes-with-cgroup-on-systemd 
    So Control Groups are two things: (A) a way to hierarchally group and label processes, and (B) a way to then apply resource limits to these groups. systemd only requires the former (A), and not the latter (B).
    
    systemctl kill auditd.service
    # systemctl kill -s SIGKILL auditd.service
    
    
     systemd-cgtop  for resource usage monitoring, 可以看看这个方法能否快速实现进程网络io的统计
     systemd-cgls


systemd + cgroup, i think it's a good combination


cgroup:
```
Multiple separate hierarchies of cgroups are necessary because each hierarchy is attached to one or more subsystems.
```


cmd to mount cgroup:
```
mount -t cgroup -o cpuset,memory hier1 /sys/fs/cgroup/rg1
```

[cgroup tutorial](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/resource_management_guide/sec-relationships_between_subsystems_hierarchies_control_groups_and_tasks)




# Terminlonogy

subsystem, cgroup, hierarchy and task ?

这个文章一定程度上暗示了什么是hierarchy: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/resource_management_guide/ch-using_control_groups
```
 Note that multiple subsystems can be mounted to a single hierarchy, but each subsystem can be mounted only once. 
```

**Command**
```
列出subsystem是否挂载，挂到哪个hierarchy上？
# lssubsys -am

Creating a mount entry，通过配置文件和命令的挂载方法？


重新调整hierarchy所挂载的subsystem: 使用 -o remount,[subsystem combination]


stat: /proc/cgroups

how to show all the hierarchy directory?  lssubsys


怎样列出 sussystems 下的所有hierarchy目录？ lssubsys -am只能显示一个，是不是说多个目录最终都映射到同一个中？ 我测试了一下，应该使用类似软连接的技术，我同时将同一个subsystem combination挂载到多个hierarchy下，重新remount其中一个，都会影响所有hierarchy。 同时，这意味着将所有相关的hierarchy umount后才能将subsystem combination释放掉，即unmount其中一个不会影响其他。 向其中一个hierarchy加入group，会影响其他的hierarchy目录。 测试了那么多，归根到底，只要在hierarchy下创建了group，直到你cgdelete这个group为止，这个hierarchy都会存在，即是是umount hierarchy

cgdelete并不会杀死group里面的task进程

lssubsys  列出所有的hierarchy，默认情况下hierarchy名为subsystem名
lssubsys -a 列出所有的subsystem
lssubsys -am
```

[Rule](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/resource_management_guide/sec-relationships_between_subsystems_hierarchies_control_groups_and_tasks)

1. subsystem特定的组合后，不能再切割或变成一个子组合。  这应该是rule 2


# TODO

1. 研究systemd and cgroup，他们怎样组合一起使用？
2. umount <hierarchy>的副作用以及怎样解决？
3. /proc/mounts  headers解析，比如第一列是device name
4. 当group还有task正在运行时， mount 和 mount -o remount[,xxx] 会报 **mount: <hierarchy dir> is busy**。 就算你umount了，由于group信息仍然残留在kernel中，**lssubsys** 和 **lssubsys -a**依然会显示这个subsystem combination，但是 **lssubsys -am**不会显示，因为没有mount point
5. if umounting hierarchy while there are still some running group, the hierarchy info skill exists in the kernel. You can not mount any subsystem within that hierarchy until you delete those group
6. [investigate systemd, its unit system and combination with cgroup] (https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/resource_management_guide/sec-modifying_control_groups)

[这个layer char不错](https://en.wikipedia.org/wiki/Systemd)

apply systemd config change:
```
# systemctl daemon-reload
# systemctl restart example.service
```

7. [how to let cgroup mount all the subsystem on start up for centos 6.x](https://www.digitalocean.com/community/tutorials/how-to-limit-resources-using-cgroups-on-centos-6)
