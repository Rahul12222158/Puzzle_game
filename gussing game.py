i = 1
while i<=7:
    print("*" * i)
    i=i+1
print("Done")

secret_number=9
gusse_count=0
gusse_limit=3
while gusse_count<gusse_limit:
    gusse=int(input('Gusse: '))
    gusse_count+=1
    if gusse==secret_number:
        print("You won")
        break
else:
    print("You fail")
