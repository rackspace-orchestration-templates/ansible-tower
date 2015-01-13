from fabric.api import env, run, task
from envassert import detect, file, group, package, port, process, service, \
    user


@task
def check():
    env.platform_family = detect.detect()
    release = run("/usr/bin/lsb_release -r | awk {'print $2'}")

    assert package.installed("ansible-tower"), "package ansible-tower is not installed"
    assert file.exists("/etc/tower/settings.py"), "/etc/tower/settings.py does not exist"
    assert port.is_listening(80), "port 80 is not listening"
    assert port.is_listening(443), "port 443 is not listening"
    assert user.exists("awx"), "user awx does not exist"
    assert group.is_exists("awx"), "group aws does not exist"
    assert process.is_up("apache2"), "process apache2 is not running"
    assert process.is_up("postgres"), "process postgres is not running"
    assert process.is_up("redis-server"), "process redis-server is not running"
    assert process.is_up("supervisor"), "process supervisor is not running"
    assert service.is_enabled("apache2"), "service apache2 is not enabled"
    assert service.is_enabled("postgres"), "service postgres is not enable"
    assert service.is_enabled("redis-server"), "service redis-server is not enabled"
    assert service.is_enabled("supervisor"), "service supervisor is not enabled"
