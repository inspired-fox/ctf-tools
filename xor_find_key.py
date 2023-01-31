import base64
import sys

args = sys.argv
print(args[1]) # clear text
f = open(args[1], 'r')

datalist = f.readlines()
count = 0
for i in datalist:
    hex_str = (i.rstrip()).split(':')
    for data in hex_str:
        hex_data = data.split(' ')[1:]
        if count == 0:
            p = hex_data
        elif count == 1:
            cs = hex_data
        else:
            cl = hex_data
    
    count = count+1

print(p)
print(cs)
print(cl)

k = 0
key = []
for i in p:
    x16_num = int(i, 16) ^ int(cs[k], 16)
    key.append(x16_num)
    k = k + 1

for item in key:
    print(chr(item), end=' ')
    
print('')

k = 0
ans = []
for i in cl:
    x16_num = int(i, 16) ^ int(key[k])
    ans.append(x16_num)
    key.append(key[k])
    k = k + 1

print(ans)
for item in ans:
    print(chr(item), end = '')

print('')

