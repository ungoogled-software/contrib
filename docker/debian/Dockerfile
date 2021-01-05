# Here we make sure to specify the digest to prevent tampering and ensure reproducibility
# This is from https://hub.docker.com/layers/debian/library/debian/buster-slim/images/sha256-e0a33348ac8cace6b4294885e6e0bb57ecdfe4b6e415f1a7f4c5da5fe3116e02?context=explore

FROM debian@sha256:e0a33348ac8cace6b4294885e6e0bb57ecdfe4b6e415f1a7f4c5da5fe3116e02

LABEL maintainer="root@max.fan"

# The following lines have been modified from the README
RUN apt-get update && apt-get install -y git python3 packaging-dev equivs

RUN git clone --recurse-submodules https://github.com/ungoogled-software/ungoogled-chromium-debian.git

# Checkout to commit: https://github.com/ungoogled-software/ungoogled-chromium-debian/commit/1c1b44277f7b0c88fc510394e25ec9d1d0dfcb7a
RUN git -C ungoogled-chromium-debian checkout --recurse-submodules 1c1b44277f7b0c88fc510394e25ec9d1d0dfcb7a && mkdir -p build/src && cp -r ungoogled-chromium-debian/debian build/src/

# From: https://superuser.com/questions/164553/automatically-answer-yes-when-using-apt-get-install
RUN echo 'APT::Get::Assume-Yes "true";' >> /etc/apt/apt.conf.d/forceyes
RUN echo 'APT::Get::force-yes "true";' >> /etc/apt/apt.conf.d/forceyes

# The rest of the Dockerfile is modified from the README
RUN cd build/src && ./debian/scripts/setup debian && mk-build-deps -i debian/control 

# RUN rm ungoogled-chromium-build-deps_*

RUN cd build/src && ./debian/scripts/setup local-src

RUN cd build/src && dpkg-buildpackage -b -uc
