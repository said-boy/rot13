#CRYPTOGRAPHY ROT13

import re

inp = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
oup = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm" 

result = []

a = input("Enter The ROT13 Text : ")

hasilinp = re.findall(r".", a)

for i in hasilinp:
    w = re.findall(i, inp)
    if w == [] :
        result.append(i)
    else:
        ind = inp.index(w[0])
        res = oup[ind]
        result.append(res)

string = ','.join(str(x) for x in result)
hasilAkhir = string.replace(',', '')

print(f"\n -> \t{hasilAkhir}\n")




