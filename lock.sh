#!/bin/bash

# setup server to be multi-platform
if [[ "$(uname -m)" != "x86_64" ]]; then
    docker pull tonistiigi/binfmt
    docker run --privileged --rm tonistiigi/binfmt --install amd64
fi

# Match CPython version with Docker image that contians ROOT
BUILD_IMAGE="python:3.10-slim-bookworm"
docker pull \
    --platform linux/amd64 \
    "${BUILD_IMAGE}"

docker run \
    --rm \
    --platform linux/amd64 \
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
