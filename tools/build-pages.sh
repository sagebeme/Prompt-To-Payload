#!/usr/bin/env bash
# Puts together the course website for GitHub Pages, in the folder given (default _site):
#   index.html, day.html, syllabus.html   the pages
#   assets/                               shared script (day list, saved progress)
#   days/                                 the lessons, which day.html fetches as Markdown
#   code/                                 the exercise files the lessons link to
#   .nojekyll                             serve files as they are
# Only files committed to Git are copied, so a local .env, .venv or log never gets published.
# Try it locally under a subpath, the way Pages serves it:
#   tools/build-pages.sh /tmp/p2p/Prompt-To-Payload && python3 -m http.server -d /tmp/p2p 8000
#   then open http://localhost:8000/Prompt-To-Payload/
set -euo pipefail

cd "$(dirname "$0")/.."
out="${1:-_site}"

# Every day in assets/days.js needs its lesson file.
count=$(grep -c '{ day: ' assets/days.js)
for n in $(seq 1 "$count"); do
  f=$(printf 'days/day-%02d.md' "$n")
  [ -f "$f" ] || { echo "Missing $f (assets/days.js lists $count days)" >&2; exit 1; }
done

rm -rf "$out"
mkdir -p "$out"
git ls-files -z index.html day.html syllabus.html .nojekyll assets days code |
  while IFS= read -r -d '' f; do
    mkdir -p "$out/$(dirname "$f")"
    cp "$f" "$out/$f"
  done

echo "Built $out: $(find "$out" -type f | wc -l) files, $count lessons"
