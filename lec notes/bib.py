import subprocess, sys

commands = [
    ['xelatex', sys.argv[1] + '.tex'],
    ['biber', sys.argv[1]],
    ['xelatex', sys.argv[1] + '.tex'],
    ['xelatex', sys.argv[1] + '.tex']
]

for c in commands:
    subprocess.call(c)
