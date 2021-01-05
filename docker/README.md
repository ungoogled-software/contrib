## Docker + ungoogled_chromium builds

This folder is intended to contain scripts, Dockerfiles, and other misc. files to assist in the creation of reproducible builds.
To that end, all Dockerfiles are pinned to a particular Debian version (it's a best practice anyways) and everything is, if possible, specified by hash.
A reproducible environment is the first step towards reproducible builds.
Each separate platform will be in a different folder (e.g. [`./debian/`](/docker/debian)).

## Building on a VPS
To aid in the ease of reproducing (the easier it is to reproduce or build, the more people will do it), some simple scripts have been added to setup and teardown a VPS instance.
Right now, the scripts are only written for DigitalOcean, but contributions are welcome!

### DigitalOcean setup
Deps:

- [doctl](https://github.com/digitalocean/doctl)

To setup a VPS instance on DigitalOcean, run:
```
bash do-setup.sh [ssh-key]
```
where `[ssh-key]` is the id of one of your DigitalOcean ssh keys (you can list them by running `doctl compute ssh-key list`)

To teardown, execute:
```
bash do-teardown.sh
```

## Contributions
Just follow the same format as above.
