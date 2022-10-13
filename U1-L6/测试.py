num=input("num")
alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
len1=len(num)
for n in range(0,len1):

    a=num[n]
    if a.isupper():
        n=1
    if a.islower():
        n=2
    a=a.lower()
    b=alpha.index(a)
    c=alpha[-b-1]
    if n==1:
        c=c.upper()
        print(c,end="")
    if n==2:
        print(c,end="")