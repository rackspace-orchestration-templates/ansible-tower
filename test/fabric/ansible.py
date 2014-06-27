from fabric.api import env, run, task
from envassert import detect, file, group, package, port, process, service, \
    user


@task
def check():
    env.platform_family = detect.detect()
    release = run("/usr/bin/lsb_release -r | awk {'print $2'}")

    assert package.installed("ansible-tower")
    assert file.exists("/etc/awx/settings.py")
    assert port.is_listening(80)
    assert port.is_listening(443)
    assert user.exists("awx")
    assert group.is_exists("awx")
    assert user.is_belonging_group("awx", "awx")
    assert process.is_up("apache2")
    assert process.is_up("postgres")
    if release == "12.04":
        assert process.is_up("beam")  # RabbitMQ
    elif release == "14.04":
        assert process.is_up("rabbitmq-server")
    assert process.is_up("supervisor")
    assert service.is_enabled("apache2")
    assert service.is_enabled("postgres")
    assert service.is_enabled("rabbitmq-server")
    assert service.is_enabled("supervisor")
