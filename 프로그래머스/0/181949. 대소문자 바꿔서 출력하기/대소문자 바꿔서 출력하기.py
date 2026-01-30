str = input()
change_str=[]
for i in str:
    if i.isupper():
        change_str.append(i.lower())
    else:
       change_str.append(i.upper())
    
print("".join(change_str))