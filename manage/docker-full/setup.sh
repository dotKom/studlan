#!/bin/bash

# Setup for running the full application.

set -eu

LOCAL_DIR=".local/docker-full"
LOG_DIR="$LOCAL_DIR/log"
CONFIG_FILE="$LOCAL_DIR/local.py"
CONFIG_TEMPLATE_FILE="setup/local.docker.dev.py"
DB_FILE="$LOCAL_DIR/db.sqlite3"
DC_FILE="setup/docker-compose.full.yml"
DC="docker-compose -f $DC_FILE"

mkdir -p "$LOCAL_DIR"
mkdir -p "$LOG_DIR"

# Add config file and exit if missing
if [[ ! -e $CONFIG_FILE ]]; then
    echo "Creating new config file ..."
    cp "$CONFIG_TEMPLATE_FILE" "$CONFIG_FILE"
fi

# Create DB file so Docker doesn't make it a directory
if [[ ! -e $DB_FILE ]]; then
    echo "Creating DB file ..."
    touch "$DB_FILE"
fi

# Add version file
echo "0.0.0-SNAPSHOT" > VERSION

echo
echo "Building image ..."
$DC build app