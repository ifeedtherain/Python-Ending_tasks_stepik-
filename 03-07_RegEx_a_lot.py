import sys
import re
#1
for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'\b(\w+)\1\b', line) != None:
        print(line)
#2
for line in sys.stdin:
    line = line.rstrip()
    h = re.sub(r'\b[Aa]+\b', 'argh', line, count=1,flags=re.IGNORECASE)
    print(h)
#3
for line in sys.stdin:
    line = line.rstrip()
    g = re.match(r'\w(\w)', line)
    h = re.sub(r'\w?', g,line, count = 1)
    print(h)
#4
for line in sys.stdin:
    line = line.rstrip()
    patern = r'\2\1'
    dupl = re.sub(r'\b(\w)(\w)', patern , line)
    print(dupl)

#5 reg not mine, but it's awesome :)
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub("(\\w)(\\1)+", "\\1", line))