#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'core'}


DOCUMENTATION = """
---
module: net_l3_interface
version_added: "2.4"
author: "Ricardo Carrillo Cruz (@rcarrillocruz)"
short_description: Manage L3 interfaces on network devices
description:
  - This module provides declarative management of L3 interfaces
    on network devices.
options:
  name:
    description:
      - Name of the L3 interface.
  ipv4:
    description:
      - IPv4 of the L3 interface.
  ipv6:
    description:
      - IPv6 of the L3 interface.
  aggregate:
    description: List of L3 interfaces definitions
  purge:
    description:
      - Purge L3 interfaces not defined in the aggregates parameter.
    default: no
  state:
    description:
      - State of the L3 interface configuration.
    default: present
    choices: ['present', 'absent']
"""

EXAMPLES = """
- name: Set eth0 IPv4 address
  net_l3_interface:
    name: eth0
    ipv4: 192.168.0.1/24

- name: Remove eth0 IPv4 address
  net_l3_interface:
    name: eth0
    state: absent
"""

RETURN = """
commands:
  description: The list of configuration mode commands to send to the device
  returned: always, except for the platforms that use Netconf transport to manage the device.
  type: list
  sample:
    - set interfaces ethernet eth0 address '192.168.0.1/24'
"""