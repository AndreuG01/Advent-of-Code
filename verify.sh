#!/usr/bin/env bash
# Compare every ported solution of a year against the Python one.
# Usage: ./verify.sh <year> [lang ...]   (default: cpp rust swift java)
# Each cell shows the run time in ms, FAIL for a different result, - if not ported.

set -uo pipefail

if [[ $# -lt 1 ]]; then
    echo "Usage: $0 <year> [lang ...]" >&2
    exit 1
fi

year="$1"
shift
langs=("$@")
[[ ${#langs[@]} -eq 0 ]] && langs=(cpp rust swift java)

root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cache="$root/.build/$year/expected"
mkdir -p "$cache"

extension() {
    case "$1" in
        cpp) echo cpp ;; rust) echo rs ;; swift) echo swift ;; java) echo java ;;
    esac
}
now_ms() { perl -MTime::HiRes=time -e 'printf "%d", time * 1000'; }
results() { grep -E '^Part [12] res: ' || true; }

failed=0
printf "%-6s" "day"
printf "%10s" "${langs[@]}"
echo

for day in $(seq 1 25); do
    [[ -f "$root/$year/Day$day/Day$day.py" ]] || continue

    # Python is the reference: run it once and keep the result
    expected="$cache/Day$day.txt"
    if [[ ! -s "$expected" || "$root/$year/Day$day/Day$day.py" -nt "$expected" ]]; then
        "$root/run.sh" "$year" "$day" py 2>/dev/null | results > "$expected"
    fi

    printf "%-6s" "$day"
    for lang in "${langs[@]}"; do
        if [[ ! -f "$root/$year/Day$day/Day$day.$(extension "$lang")" ]]; then
            printf "%10s" "-"
            continue
        fi
        if ! BUILD_ONLY=1 "$root/run.sh" "$year" "$day" "$lang" >/dev/null 2>&1; then
            printf "%10s" "NOBUILD"
            failed=$((failed + 1))
            continue
        fi
        start=$(now_ms)
        output=$("$root/run.sh" "$year" "$day" "$lang" 2>/dev/null | results)
        elapsed=$(( $(now_ms) - start ))
        if [[ -n "$output" && "$output" == "$(cat "$expected")" ]]; then
            printf "%10s" "${elapsed}ms"
        else
            printf "%10s" "FAIL"
            failed=$((failed + 1))
        fi
    done
    echo
done

echo
if [[ $failed -eq 0 ]]; then echo "All results match Python."; else echo "$failed failures."; fi
exit $(( failed > 0 ))
