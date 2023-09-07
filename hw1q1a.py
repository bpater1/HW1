import sys

output = []
for ln in sys.stdin:
    for c in ln:
        if c.upper() in 'ACGT':
            output.append(c.upper())
sys.stdout.write(''.join(output) + '\n')