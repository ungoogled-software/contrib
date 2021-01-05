#!/usr/bin/env bash

# Helper to destroy a digitalocean VPS that was created with do-setup.sh
# Usage: bash do-teardown.sh 

doctl compute droplet delete "ungoogled-chromium"
