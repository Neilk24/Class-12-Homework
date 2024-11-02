num=int(input("Enter the number you want as a binary number: "))

if num==0:
    print("0 as a binary number is 0")
elif num==1:
    print("1 as a binary number is 1")
else:
    temp=''
    while num>=2:
        quotient=num//2
        remainder=num%2
        temp=temp+str(remainder)
        num=quotient

    final_number=(num%2)

    temp=temp+str(final_number)

    other_temp=str(temp)

    final_result=(other_temp[::-1])
    
    print(final_result)