[![Circle CI](https://circleci.com/gh/rackspace-orchestration-templates/ansible-tower.png?style=badge)](https://circleci.com/gh/rackspace-orchestration-templates/ansible-tower)
Description
===========

A template that deploys Ansible Tower onto a single Linux server.


Instructions
===========

#### Getting Started
If you are new to [Tower](http://www.ansible.com/tower), check out the [user
guide](http://releases.ansible.com/ansible-tower/docs/tower_user_guide-latest.pdf).
This installation of tower is limited to 10 machines. If you require support
for more than 10 machines, you will need to upgrade your installation.
Pricing details for additional support server support can be found
[here](http://www.ansible.com/pricing#tower).

#### Accessing your Deployment
To access Tower, go to the Ansible URL in your browser, and login with the
credentials provided as a part of this deployment.

#### Logging in via SSH
The private key provided in the passwords section can be used to login as
root via SSH.  We have an article on how to use these keys with [Mac OS X and
Linux](http://www.rackspace.com/knowledge_center/article/logging-in-with-a-ssh-private-key-on-linuxmac)
as well as [Windows using
PuTTY](http://www.rackspace.com/knowledge_center/article/logging-in-with-a-ssh-private-key-on-windows).


Requirements
============
* A Heat provider that supports the following:
  * OS::Heat::RandomString
  * OS::Nova::KeyPair
  * Rackspace::Cloud::Server
* An OpenStack username, password, and tenant id.
* [python-heatclient](https://github.com/openstack/python-heatclient)
`>= v0.2.8`:

```bash
pip install python-heatclient
```

We recommend installing the client within a [Python virtual
environment](http://www.virtualenv.org/).

Parameters
==========
Parameters can be replaced with your own values when standing up a stack. Use
the `-P` flag to specify a custom parameter.

* `flavor`: Rackspace Cloud Server flavor to use. The size is based on the amount of
RAM for the provisioned server.
 (Default: 1 GB General Purpose v1)
* `ansible_tower_tarball`: Location of the Ansible Tower installer (Default: http://releases.ansible.com/ansible-tower/setup/ansible-tower-setup-latest.tar.gz
)
* `image`: Server image used for all servers that are created as a part of this
deployment
 (Default: Ubuntu 14.04 LTS (Trusty Tahr))
* `server_name`: The instance name (Default: ansible-tower)

Outputs
=======
Once a stack comes online, use `heat output-list` to see all available outputs.
Use `heat output-show <OUTPUT NAME>` to get the value of a specific output.

* `private_key`: SSH Private Key 
* `ansible_password`: Admin Password 
* `ansible_url`: Tower URL 
* `server_ip`: Server IP 
* `ansible_username`: Admin Username 

For multi-line values, the response will come in an escaped form. To get rid of
the escapes, use `echo -e '<STRING>' > file.txt`. For vim users, a substitution
can be done within a file using `%s/\\n/\r/g`.
