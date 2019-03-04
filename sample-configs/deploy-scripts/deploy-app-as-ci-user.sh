#!/bin/bash

# This script is meant to be a wrapper run directly by the CI/CD tool.
# Remember to add the deploy script to the sudoers file with this user and no password.
# Suggested name: /home/studlan/deploy-studlan-EXAMPLE.sh

INSTANCE_NAME="app-EXAMPLE"

sudo /srv/studlan/deploy-background-${INSTANCE_NAME}.sh
