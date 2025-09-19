# Auto-merge helper for .gitignore
# Reads current .gitignore (ours) and theirs.tmp (remote),
# appends lines from theirs that are not already present in ours.
from pathlib import Path
p = Path('.') / '.gitignore'
q = Path('.') / 'theirs.tmp'
if not p.exists():
    print('.gitignore not found')
    raise SystemExit(1)
if not q.exists():
    print('theirs.tmp not found')
    raise SystemExit(1)

ours = p.read_text(encoding='utf-8').splitlines()
theirs = q.read_text(encoding='utf-8').splitlines()
seen = set(ours)
out = list(ours)
for line in theirs:
    if line not in seen:
        out.append(line)
        seen.add(line)
# Ensure trailing newline
p.write_text("\n".join(out) + ("\n" if out and out[-1] != "" else ""), encoding='utf-8')
print('Merged .gitignore: kept', len(out), 'lines')
