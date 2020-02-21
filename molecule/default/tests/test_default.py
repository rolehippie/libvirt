import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_libvirt_is_installed(host):
    pkg = host.package("libvirt-bin")
    assert pkg.is_installed
