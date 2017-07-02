import sys
import re
re_line = []
for line in sys.stdin:
    line = line.rstrip()

    x = re.search('(.*(cat+).*(cat+).*)+', line)
    try:
        if x.group(1) != None :
            print(line)
    except AttributeError:
        pass

