#!/usr/bin/env bash


# Install dependencies
poetry install --no-root

exec "$@"
