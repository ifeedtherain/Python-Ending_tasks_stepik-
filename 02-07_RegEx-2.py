import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.match(r'.*\bcat\b.*', line) != None:
        print(line)