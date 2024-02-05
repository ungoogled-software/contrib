#!/usr/bin/env bash

# Helper to setup a digitalocean VPS with all the right stuff
# Usage: bash do-setup.sh [ssh-key-id]
# If you do not specify ssh-key-id, you need to know the root password!

# Example: bash do-setup.sh 28142601

if [ -z "$1" ]; then
    doctl compute droplet create "ungoogled-chromium" --image ubuntu-20-04-x64 --region nyc1 --size s-6vcpu-16gb
else
    doctl compute droplet create "ungoogled-chromium" --image ubuntu-20-04-x64 --region nyc1 --size s-6vcpu-16gb --ssh-keys $1
fi

echo "curl -fsSL https://get.docker.com -o get-docker.sh" | doctl compute ssh "ungoogled-chromium"
echo "sh get-docker.sh" | doctl compute ssh "ungoogled-chromium"
