import sys
import re
for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'(z...z)+', line) != None:
        print.append(line)
