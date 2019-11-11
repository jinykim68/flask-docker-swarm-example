#!/bin/bash

ansible-playbook ./server.yaml -e @./host_vars/host_vars.yaml
