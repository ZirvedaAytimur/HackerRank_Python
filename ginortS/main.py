import string
S = input()
S = sorted(S, key=(string.ascii_letters + '1357902468').index)
print(*S, sep='')
