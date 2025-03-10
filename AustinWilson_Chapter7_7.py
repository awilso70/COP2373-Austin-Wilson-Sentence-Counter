import re
s = input('Enter your message: ')
pat = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'
m= re.findall(pat, s, flags=re.DOTALL |re.MULTILINE)

for i in m:
    print('>', i)

print(f'Total number of sentences: {len(m)}')