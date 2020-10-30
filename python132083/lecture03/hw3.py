temp = input('Введите температуру в цельсиях (С) или фаренгейтах (F):' )
temp = temp.strip()
temp = temp.replace(",", ".")

# +5.5C
# -10F
# 3C

if len(temp) < 2:
    exit(1)
    
tempnum, grad = temp[:-1], temp[-1]

if tempnum[0] in ["+", "-"]:
    tempnum = tempnum[1:]

if grad not in ["F", "C"]:
    print('Введите температуру в цельсиях (С) или фаренгейтах (F)')
    exit(1)
    
terms = tempnum.split(".")

if not(0 < len(terms) <= 2):
    exit(1)

if len(terms) == 1 and not terms[0].isdigit():
    exit(1)
    
if len(terms) == 2 and (not terms[0].isdigit() or not terms[1].isdigit()):
    exit(1)
    
tempnum = float(tempnum)
    
if grad in "F" :
    cel = (tempnum-32)/1.8
    print ("Результат:", round((cel), 2), "C")
    
elif grad in "C" :
    far = tempnum*1.8+32
    print ("Результат:", round((far), 2), "F")

