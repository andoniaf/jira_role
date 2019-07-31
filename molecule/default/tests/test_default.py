import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_openjdk_installed(host):
    pkg = host.package("openjdk-11-jdk-headless")
    assert pkg.is_installed
    assert pkg.version.startswith("11.0.4+11-1~bpo9+1")


def test_jira_group_exists(host):
    jira_group = host.group("jira")
    assert jira_group.exists


def test_jira_user_exists(host):
    jira_user = host.user("jira")
    assert jira_user.name == "jira"


def test_jira_home_exist(host):
    jira_home = host.file("/opt/atlassian/jira")
    assert jira_home.exists
    assert jira_home.is_symlink


def test_jira_service_running(host):
    jira_service = host.service("jira")
    assert jira_service.is_running
    assert jira_service.is_enabled


def test_jira_listening(host):
    jira_socket = host.socket("tcp://0.0.0.0:8080")
    assert jira_socket.is_listening
