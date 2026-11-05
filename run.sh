#!/usr/bin/env bash
# Compile (if needed) and run one solution.
# Usage: ./run.sh <year> <day> <py|cpp|rust|swift|java> [input file, default data.txt]
# Example: ./run.sh 2015 3 rust example.txt
# With BUILD_ONLY=1 it compiles and does not run.

set -euo pipefail

if [[ $# -lt 3 || $# -gt 4 ]]; then
    echo "Usage: $0 <year> <day> <py|cpp|rust|swift|java> [input file]" >&2
    exit 1
fi

year="$1"
day="$((10#$2))"
lang="$3"
input="${4:-data.txt}"

root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
dir="$root/$year/Day$day"
name="Day$day"
out="$root/.build/$year/$lang"

# Only for this process: the local toolchains from setup_tools.sh
export RUSTUP_HOME="$root/.tools/rustup"
export CARGO_HOME="$root/.tools/cargo"
export JAVA_HOME="$root/.tools/jdk/Contents/Home"
export PATH="$CARGO_HOME/bin:$JAVA_HOME/bin:$PATH"

case "$lang" in
    py) source_file="$dir/$name.py" ;;
    cpp) source_file="$dir/$name.cpp" ;;
    rust) source_file="$dir/$name.rs" ;;
    swift) source_file="$dir/$name.swift" ;;
    java) source_file="$dir/$name.java" ;;
    *) echo "Error: unknown language '$lang'" >&2; exit 1 ;;
esac

if [[ ! -f "$source_file" ]]; then
    echo "Error: $source_file does not exist" >&2
    exit 1
fi

mkdir -p "$out"
binary="$out/$name"
[[ "$lang" == "java" ]] && binary="$out/$name.class"

if [[ "$lang" != "py" && ( ! -e "$binary" || "$source_file" -nt "$binary" ) ]]; then
    case "$lang" in
        cpp) clang++ -std=c++20 -O2 -o "$binary" "$source_file" ;;
        rust) rustc --edition 2021 -O -o "$binary" "$source_file" ;;
        swift) swiftc -O -o "$binary" "$source_file" ;;
        java) javac -d "$out" "$source_file" ;;
    esac
fi

[[ "${BUILD_ONLY:-}" == "1" ]] && exit 0

# Run from the day's folder, as the file names matter ("example" in the name)
cd "$dir"
case "$lang" in
    py) exec python3 "$name.py" "$input" ;;
    java) exec java -cp "$out" "$name" "$input" ;;
    *) exec "$binary" "$input" ;;
esac
