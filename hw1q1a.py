import sys

output = []
for ln in sys.stdin:
  for c in ln:
    if c in 'ACGT':
      output.append(c)
sys.stdout.write(''.join(output) + '\n')