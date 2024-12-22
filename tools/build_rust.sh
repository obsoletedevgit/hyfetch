#!/usr/bin/env bash

set -e

# Step 1: Build the Docker image
echo "Building the Docker image..."
docker build -t rust-builder-general tools/rust-builder/general

# Step 2: Run the Docker container and execute the builder script
echo "Running the Docker container..."
docker run --rm -v "$(pwd)":/app rust-builder-general bash -c "cd /app && ./tools/rust-builder/general/build.sh"
