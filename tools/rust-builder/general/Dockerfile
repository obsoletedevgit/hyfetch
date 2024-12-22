FROM debian:10-slim

# Install Rust building environment
RUN apt update && apt install -y curl build-essential gcc libssl-dev bash musl-tools mingw-w64
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
RUN source $HOME/.cargo/env

# Add toolchains for building for gnu[x86_64, aarch64, armv7l], musl[x86_64], and windows[x86_64, aarch64]
RUN rustup target add \
    x86_64-unknown-linux-gnu \
    aarch64-unknown-linux-gnu \
    armv7-unknown-linux-gnueabihf \
    x86_64-unknown-linux-musl \
    x86_64-pc-windows-gnu \

WORKDIR /app
