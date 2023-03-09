import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_files(host):
    ansible_service_mgr = host.ansible("setup")["ansible_facts"]["ansible_service_mgr"]
    files = ["/usr/local/bin/exploitdog_agent"]
    if ansible_service_mgr == 'systemd':
        files.append("/etc/systemd/system/exploitdog_agent.service")
    if ansible_service_mgr == 'sysvinit':
        files.append("/etc/init.d/exploitdog_agent")
    if ansible_service_mgr == 'upstart':
        files.append("/etc/init/exploitdog_agent.conf")
    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file

def test_permissions_didnt_change(host):
    dirs = [
        "/etc",
        "/root",
        "/usr",
        "/var"
    ]
    for file in dirs:
        f = host.file(file)
        assert f.exists
        assert f.is_directory
        assert f.user == "root"
        assert f.group == "root"


def test_user(host):
    assert host.group("exploitdog-agent").exists
    assert "exploitdog-agent" in host.user("exploitdog-agent").groups
    assert host.user("exploitdog-agent").shell == "/usr/sbin/nologin"
    assert host.user("exploitdog-agent").home == "/"


def test_service(host):
    s = host.service("exploitdog_agent")
    assert s.is_running

def test_config(host):
    f = host.file("/etc/exploitdog_agent/config.json")
    assert f.exists
    assert f.user == "exploitdog-agent"
    assert f.group == "exploitdog-agent"

def test_dirs(host):
    dirs = [
        "/var/lib/exploitdog_agent",
        "/var/log/exploitdog_agent"
    ]
    for file in dirs:
        f = host.file(file)
        assert f.exists
        assert f.is_directory
        assert f.user == "exploitdog-agent"
        assert f.group == "exploitdog-agent"
