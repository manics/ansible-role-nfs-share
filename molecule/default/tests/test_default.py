import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_readwrite(host):
    f = '/mnt/rw/hello'
    with host.sudo('test'):
        c1 = host.run('touch %s', f)
    assert c1.rc == 0
    assert host.file(f).exists
    with host.sudo('test'):
        c2 = host.run('rm %s', f)
    assert c2.rc == 0
    assert not host.file(f).exists
