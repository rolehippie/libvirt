# libvirt

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/libvirt) [![General Workflow](https://github.com/rolehippie/libvirt/actions/workflows/general.yml/badge.svg)](https://github.com/rolehippie/libvirt/actions/workflows/general.yml) [![Readme Workflow](https://github.com/rolehippie/libvirt/actions/workflows/readme.yml/badge.svg)](https://github.com/rolehippie/libvirt/actions/workflows/readme.yml) [![Galaxy Workflow](https://github.com/rolehippie/libvirt/actions/workflows/galaxy.yml/badge.svg)](https://github.com/rolehippie/libvirt/actions/workflows/galaxy.yml) [![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/libvirt)](https://github.com/rolehippie/libvirt/blob/master/LICENSE) [![Ansible Role](https://img.shields.io/ansible/role/51458)](https://galaxy.ansible.com/rolehippie/libvirt)

Ansible role to install and configure libvirt.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of content

- [Default Variables](#default-variables)
  - [libvirt_daemon_opts](#libvirt_daemon_opts)
  - [libvirt_images](#libvirt_images)
  - [libvirt_machines](#libvirt_machines)
  - [libvirt_networks](#libvirt_networks)
  - [libvirt_virtlockd_args](#libvirt_virtlockd_args)
  - [libvirt_virtlogd_args](#libvirt_virtlogd_args)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Default Variables

### libvirt_daemon_opts

Arguments for the libvirtd

#### Default value

```YAML
libvirt_daemon_opts:
```

### libvirt_images

List of images to download

#### Default value

```YAML
libvirt_images: []
```

#### Example usage

```YAML
libvirt_images:
  - name: ubuntu-18.04.qcow2
    url: https://cloud-images.ubuntu.com/bionic/20200218/bionic-server-cloudimg-amd64.img
    checksum: sha256:3c3a67a142572e1f0e524789acefd465751224729cff3a112a7f141ee512e756
```

### libvirt_machines

Definition of available machines

#### Default value

```YAML
libvirt_machines: []
```

#### Example usage

```YAML
libvirt_machines:
  - name: foobar
    fqdn: foobar.example.com
    memory: 4096
    cpus: 4
    vnc: 5901
    userdata: True
    overwrite: False
    password: p455w0rd
    sshkeys:
      - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDwHEKPdszS27LCQCao4UhuP0TvFlccP6nRWKm00fquA user1@example
      - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKggkhEVy1Qgd+y3UNXXXeu9oz4LVsKc2njpSkjpzPdv user2@example
      - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICmthYIctiIh3UzYIXeSqMqgKm5n1yIX9/0rpeXSlMet user3@example
    interfaces:
      - type: network
        source: general
        mac: 18:03:73:40:90:4c
        device: ens3
        dhcp: True
    disks:
      - name: foobar-root
        type: lvm
        group: host-vg
        size: 50g
        device: vda
        source: /var/lib/libvirt/images/ubuntu-18.04.qcow2
    boot:
      - hd
```

### libvirt_networks

Definition of available networks

#### Default value

```YAML
libvirt_networks: []
```

#### Example usage

```YAML
libvirt_networks:
  - name: virbr1
    bridge: virbr1
    state: active
  - name: virbr2
    bridge: virbr2
    uuid: 9315F6EA-AEA2-43B0-A5C7-C69FBCF4899E
    mac: C5-9E-B7-34-F7-7B
    autostart: False
    state: active
  - name: virbr3
    state: absent
```

### libvirt_virtlockd_args

Arguments for the virtlockd

#### Default value

```YAML
libvirt_virtlockd_args:
```

### libvirt_virtlogd_args

Arguments for the virtlogd

#### Default value

```YAML
libvirt_virtlogd_args:
```

## Discovered Tags

**_images_**

**_libvirt_**

**_machines_**

**_networks_**

**_skip_ansible_later_**


## Dependencies

- None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
