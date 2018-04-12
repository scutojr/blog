

systemd units? system, scope, slice
Available systemd Unit Types?


# Command

[systemd-cgls](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/resource_management_guide/sec-Obtaining_Information_About_Control_Groups)

systemctl list-units

systemd-cgtop

systemd-cgls [subsys name]


systemctl daemon-reload // reload the systemd configuration


systemctl:
```
System Commands:
  is-system-running               Check whether system is fully running
  default                         Enter system default mode
  rescue                          Enter system rescue mode
  emergency                       Enter system emergency mode
  halt                            Shut down and halt the system
  poweroff                        Shut down and power-off the system
  reboot [ARG]                    Shut down and reboot the system
  kexec                           Shut down and reboot the system with kexec
  exit                            Request user instance exit
  switch-root ROOT [INIT]         Change to a different root file system
  suspend                         Suspend the system
  hibernate                       Hibernate the system
  hybrid-sleep                    Hibernate and suspend the system
```


display the status of service managed by systemd
```
systemctl list-units --type service --all
```

[run a command in specified cgroup](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/resource_management_guide/chap-using_control_groups#sec-Creating_Cgroups)
```
systemd-run --unit=name --scope --slice=slice_name command
```


# systemd & cgroup


# Configuration

**about JoinControllers**: modify it in /etc/systemd/system.conf won't take effect if your os apply initrd
[solution](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/sec-verifying_the_initial_ram_disk_image)
```
dracut --force
```


# FAQ

1. how to start process at system startup by systemd
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/sect-Managing_Services_with_systemd-Services#tabl-Managing_Services_with_systemd-Services-systemctl
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/sect-Managing_Services_with_systemd-Services#tabl-Managing_Services_with_systemd-Services-chkconfig
```
systemctl enable name.service
systemctl disable name.service

systemctl list-unit-files --type service
systemctl list-dependencies --after
systemctl list-dependencies --before
```
2. what is target?



# Reference

> https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/resource_management_guide/sec-default_cgroup_hierarchies

> [Systemd Unit Files Locations](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/chap-Managing_Services_with_systemd#tabl-Managing_Services_with_systemd-Introduction-Units-Locations)
