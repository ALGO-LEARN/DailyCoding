import re
n = input()
p = re.compile('[A-Z]')
q = re.compile('[0-9]')
print(''.join(sorted(p.findall(n))) + str(sum(map(int, q.findall(n)))))
