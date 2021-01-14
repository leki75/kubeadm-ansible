You should put your inventory file into this directory.

Example inventory:
```
[master]
kthw-master-1 ansible_host=172.22.70.31
kthw-master-2 ansible_host=172.22.70.32
kthw-master-3 ansible_host=172.22.70.33

[worker]
kthw-worker-1 ansible_host=172.22.70.111
kthw-worker-2 ansible_host=172.22.70.113
kthw-worker-3 ansible_host=172.22.70.112
kthw-worker-4 ansible_host=172.22.70.114

[etcd:children]
master

[all:vars]
ansible_user=ubuntu
ansible_python_interpreter=python3
```