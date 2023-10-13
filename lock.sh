#!/bin/bash

# This should be the base image the Docker image built by the GitHub Action uses
BUILD_IMAGE="python:3.11-slim-bookworm"
docker pull "${BUILD_IMAGE}"

# Don't need to ensure emulation possible on non-x86_64 platforms at the
# `docker run` level as the platform is specified in the conda-lock command.
docker run \
    --rm \
    --volume "${PWD}":/read:ro \
    --volume "${PWD}/book":/write \
    --workdir /work \
    "${BUILD_IMAGE}" \
    /bin/bash -c "\
        python -m venv venv && . venv/bin/activate \
        && python -m pip install --upgrade pip wheel \
        && python -m pip install pip-tools \
        && cat /read/binder/requirements.txt /read/book/requirements.txt > requirements.txt \
        && mkdir -p book \
        && pip-compile \
            --resolver=backtracking \
            --generate-hashes \
            --output-file book/requirements.lock \
            requirements.txt \
        && cp book/requirements.lock /write \
        "
# Ensure owned by user and not root
touch book/tmp.lock
cp book/requirements.lock book/tmp.lock
mv --force book/tmp.lock book/requirements.lock
