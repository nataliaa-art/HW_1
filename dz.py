#1
s = input()
print(len(s))

#2
s = input()
print(s[::-1])

#3
s = input()
print(s[s.find("'")+1:s.rfind("'")])

#4
s = input()
s = s.split(' ')
print(*s[::-1])

#5
s = input()
print(s[:s.find('@')])

#6
s = input()
for x in '-)( ':
    s = s.replace(x,'')
print(s)

#7
s = input()
s = s.split(' ')
for i in range(len(s)):
    print(s[i])

#8
s = input()
if s == s[::-1]:
    print('yes')
else:
    print('no')
