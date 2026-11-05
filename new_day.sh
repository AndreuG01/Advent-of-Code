#!/usr/bin/env bash
# Create the directory structure for an Advent of Code day.
# Usage: ./new_day.sh <year> <day>
# Example: ./new_day.sh 2015 4  ->  2015/Day4/{Day4.py,data.txt,example.txt}

set -euo pipefail

if [[ $# -ne 2 ]]; then
    echo "Usage: $0 <year> <day>" >&2
    exit 1
fi

year="$1"
day="$2"

if ! [[ "$year" =~ ^[0-9]{4}$ ]]; then
    echo "Error: year must be a 4-digit number (got '$year')" >&2
    exit 1
fi
if ! [[ "$day" =~ ^[0-9]+$ ]] || (( 10#$day < 1 || 10#$day > 25 )); then
    echo "Error: day must be a number between 1 and 25 (got '$day')" >&2
    exit 1
fi

day=$((10#$day))  # strip leading zeros, e.g. 04 -> 4
root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
dir="$root/$year/Day$day"
script="$dir/Day$day.py"

mkdir -p "$dir"
touch "$dir/data.txt" "$dir/example.txt"

if [[ -e "$script" ]]; then
    echo "$script already exists, leaving it untouched."
else
    cat > "$script" <<'EOF'
import sys

file_content = open(sys.argv[1]).read().strip()

part_1_res = 0
part_2_res = 0


print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
EOF
fi

echo "Created $year/Day$day:"
ls "$dir"
