heat-templates
==============

This repository holds various HEAT templates for use with [OpenStack Heat](https://wiki.openstack.org/wiki/Heat) on the [Rackspace Cloud](http://www.rackspace.com/cloud/).

Requirements
============
* An OpenStack username, password, and tenant id.
* [python-heatclient](https://github.com/openstack/python-heatclient) `>= v0.2.8`:

```bash
pip install python-heatclient
```

We recommend installing the client within a [Python virtual environment](http://www.virtualenv.org/).

Example Usage
=============
Here is an example of how to deploy this template using the [python-heatclient](https://github.com/openstack/python-heatclient):

```
heat --os-username <OS-USERNAME> --os-password <OS-PASSWORD> --os-tenant-id \
<TENANT-ID> --os-auth-url https://identity.api.rackspacecloud.com/v2.0/ \
stack-create Minecraft-Stack -f minecraft-server.yaml \
-P server_hostname=MineStack -P ssh_keypair_name=mine-example
```

* For UK customers, use `https://lon.identity.api.rackspacecloud.com/v2.0/` as the `--os-auth-url`.

Optionally, set environmental variables to avoid needing to provide these values every time a call is made:

```
export OS_USERNAME=<USERNAME>
export OS_PASSWORD=<PASSWORD>
export OS_TENANT_ID=<TENANT-ID>
export OS_AUTH_URL=<AUTH-URL>
```
