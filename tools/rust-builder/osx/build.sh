#!/usr/bin/env bash

set -e

# Add cargo to path
export PATH="$HOME/.cargo/bin:$PATH"
cd /app

# OSX linker and ar
export OSX_VER=20.4
export CARGO_TARGET_X86_64_APPLE_DARWIN_LINKER=/osxcross/bin/x86_64-apple-darwin$OSX_VER-clang
export CARGO_TARGET_X86_64_APPLE_DARWIN_AR=/osxcross/bin/x86_64-apple-darwin$OSX_VER-ar
export CARGO_TARGET_AARCH64_APPLE_DARWIN_LINKER=/osxcross/bin/aarch64-apple-darwin$OSX_VER-clang
export CARGO_TARGET_AARCH64_APPLE_DARWIN_AR=/osxcross/bin/aarch64-apple-darwin$OSX_VER-ar


# Build for platforms
#cp /osxcross/bin/x86_64-apple-darwin$OSX_VER-strip /usr/bin/strip
cargo build --release --target x86_64-apple-darwin
#cp /osxcross/bin/aarch64-apple-darwin$OSX_VER-strip /usr/bin/strip
cargo build --release --target aarch64-apple-darwin
