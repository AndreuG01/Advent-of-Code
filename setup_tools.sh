#!/usr/bin/env bash
# Install Rust and a JDK inside this repo (.tools/), nothing global.
# C++ and Swift use the compilers from the Apple Command Line Tools.
# To remove everything: rm -rf .tools .build
# Usage: ./setup_tools.sh

set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
tools="$root/.tools"
mkdir -p "$tools"

if [[ "$(uname -s)-$(uname -m)" != "Darwin-arm64" ]]; then
    echo "Error: this script only knows the downloads for Apple Silicon Macs" >&2
    exit 1
fi

# Rust
if [[ -x "$tools/cargo/bin/rustc" ]]; then
    echo "Rust already installed, skipping."
else
    echo "Installing Rust into .tools/ ..."
    curl -fsSL -o "$tools/rustup-init" \
        "https://static.rust-lang.org/rustup/dist/aarch64-apple-darwin/rustup-init"
    chmod +x "$tools/rustup-init"
    RUSTUP_HOME="$tools/rustup" CARGO_HOME="$tools/cargo" \
        "$tools/rustup-init" -y --no-modify-path --profile minimal
    rm "$tools/rustup-init"
fi

# Java
if [[ -x "$tools/jdk/Contents/Home/bin/javac" ]]; then
    echo "JDK already installed, skipping."
else
    echo "Installing JDK into .tools/ ..."
    curl -fsSL -o "$tools/jdk.tar.gz" \
        "https://api.adoptium.net/v3/binary/latest/21/ga/mac/aarch64/jdk/hotspot/normal/eclipse"
    mkdir -p "$tools/jdk"
    tar -xzf "$tools/jdk.tar.gz" -C "$tools/jdk" --strip-components=1
    rm "$tools/jdk.tar.gz"
fi

echo "Done."
