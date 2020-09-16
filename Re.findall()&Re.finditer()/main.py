import re

S = input()
consonants = '[qwrtypsdfghjklzxcvbnm]'
a = re.findall('(?<=' + consonants + ')([aeiou]{2,})' + consonants, S, re.I)
print('\n'.join(a or ['-1']))
