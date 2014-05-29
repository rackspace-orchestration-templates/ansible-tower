ansible-tower
======================
This template will deploy the latest version of [Ansible
Tower](http://www.ansible.com/tower).

Requirements
============
* An OpenStack username, password, and tenant id.
* An already registered [Nova
Keypair](http://docs.rackspace.com/servers/api/v2/cs-gettingstarted/content\
nova_summary_serverkeypairs.html)
* [python-heatclient](https://github.com/openstack/python-heatclient) `>=
v0.2.8`:

```bash
pip install python-heatclient
```

We recommend installing the client within a [Python virtual
environment](http://www.virtualenv.org/).

Example Usage
=============
Here is an example of how to deploy this template using the
[python-heatclient](https://github.com/openstack/python-heatclient):

```
heat --os-username <OS-USERNAME> --os-password <OS-PASSWORD> --os-tenant-id \
<TENANT-ID> --os-auth-url https://identity.api.rackspacecloud.com/v2.0/ \
stack-create Ansible-Tower -f ansible-tower.yaml \
-P server_name=ansible-tower
```

* For UK customers, use `https://lon.identity.api.rackspacecloud.com/v2.0/` as
the `--os-auth-url`.

Optionally, set environmental variables to avoid needing to provide these
values every time a call is made:

```
export OS_USERNAME=<USERNAME>
export OS_PASSWORD=<PASSWORD>
export OS_TENANT_ID=<TENANT-ID>
export OS_AUTH_URL=<AUTH-URL>
```

Parameters
==========
Parameters can be replaced with your own values when standing up a stack. Use
the `-P` flag to specify a custom parameter.

* `server_name`: Sets the hostname of the server. (Default: ansible-tower)
* `flavor`: Cloud server size to use. (Default: 1GB Standard Instance)
* `ansible_tower_tarball`: Location of the Ansible Tower installer. (Default:
  Latest release from Ansible.)

Outputs
=======
Once a stack comes online, use `heat output-list` to see all available outputs.
Use `heat output-show <OUTPUT NAME>` to get the value fo a specific output.

* `private_key`: Private key for logging in as root to your server.
* `public_ip`: The public IP address of the server.
* `private_ip`: The private IP address of the server.
* `ansible_username`: Username for logging into Tower (will always be `admin`)
* `ansible_password`: Admin password for logging into Tower.
* `ansible_url`: URL to use when accessing Ansible Tower
* `postgres_admin_password`: Admin password for Posgresql that's bundled with
  Tower.  It's automatically configured with Tower.
* `rabbitmq_admin_password`: Admin password for RabbitMQ that's bundled with
  Tower.  It's automatically configured with Tower, you probably won't need it.

For multi-line values, the response will come in an escaped form. To get rid of
the escapes, use `echo -e '<STRING>' > file.txt`. For vim users, a substitution
can be done within a file using `%s/\\n/\r/g`.

Stack Details
=============
This installs on a Ubuntu 12.04 server using the installer provided by
Ansible.

Contributing
============
There are substantial changes still happening within the [OpenStack
Heat](https://wiki.openstack.org/wiki/Heat) project. Template contribution
guidelines will be drafted in the near future.

License
=======
```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
