import re
s=str(input())
s=re.sub(r'[aeiuo]','',s)
print(s)