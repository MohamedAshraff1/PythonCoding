# 1). WAP to print equal if the both inputs are equal
# def equal(a,b):
#     if a==b:
#         return 'Both Are Equal'
#     return 'Both Are Not Equal'
# print(equal('ash','a1sh'))

# 2). Write a program to check whether the input number is greater than 10 or not if it is greater 
# than 10 print message as greater and print that number if that number is not greater than 10 
# print that number

# def gr(a):
#     if a > 10:
#         return a,'a is gr than 10'
#     return a
# print(gr(11))

# 3. Write a program to check whether the given input is 0 or not if 0 print 0
# def zero(a):
#     if a==0:
#         return 'zero'
#     return 'non zero'
# print(zero(1))

# 4. Write a program to check whether the given string is palindrome or not if it is a palindrome 
# string palindrome along with the string if it is not a palindrome print not palindrome

# def palin(a):
#     temp=''
#     out=''
#     if type(a) in [int,float,bool,complex]:
#         temp=str(a)
#     else:
#         temp=a
#     print(temp)
#     for i in temp:
        # out=i+out
#     if temp==out:
#         return 'palindrome'
#     return 'non palindrome'
# print(palin('malayalam'))

# 10. Write a program to check whether a square or rectang
# length = int(input("Enter the length of the shape: "))
# width = int(input("Enter the width of the shape: "))

# length=------------------
# widith=|
#        |
# if length == width:
#     print("This is a square")
# else:
#     print("This is a rectangle")

# 11. Write a program to check whether a given number is multiple of 5 or not

# def div(a):
#     if a%5==0:
#         print('true')
#     else:
#         print('false')
# div(3)

# 14. Write a program to check whether the input number is divisible by 3 and 5 if the number 
# divisible by 3 print fizz if the number divisible by 5 print bizz if it is divisible by both then 
# print fizzbuzz
# def div(a):
#     if a%3==0 and a%5==0:
#         print('FizzBizz')
#     elif a%5==0:
#         print('Fizz')
#     elif a%3==0:
#         print('Bizz')
# div(75)
# . Write a program to check the maximum of three numbers

# def maxi(a,b,c):
#     if a>b:
#         print(a,'a is gr than b',b)
#     elif b>c:
#         print(b,'b is gr')
#     elif c>a and c>b:
#         print(c,'c is gr')   
# maxi(10,10,20)

# 17. Write a program to check given number is one digit or two digit or three digit for more than 
# 3 digit
# def leng(a):
#     temp=str(a)
#     if len(temp)==1:
#         print('one dig')
#     elif len(temp)==2:
#         print('two dig')
#     elif len(temp)==3:
#         print('three dig')
#     else:
#         print('len is out of range')
# leng(2222)
# 18. Write a program to accept any number from 1-5 and display that number in word form
# def word(a):
#     d={1:'one',2:'two',3:'three',4:'four',5:'five'}
#     if a==1:
#         print(d[a])
#     elif a==2:
#         print(d[a])
#     elif a==3:
#         print(d[a])
#     elif a==4:
#         print(d[a])
#     elif a==5:
#         print(d[a])
#     else:
#         print('number not exit')
# word(5)
        

# 21. Write a program to check whether the given input character is present in a given string 
# collection or not if it is present then string collection then check whether the collection
# length is even or odd if it is even print even indexed items of that collection if it is our print 
# odd index item of the collection if the character not present in the collection just bring that 
# collection

# def fun(a):
#     out=''
#     ch=str(input('enter find value'))
#     if ch in a and len(a)%2==0:
#         for i in range(len(a)):
#             if i%2==0:
#                 out+=a[i]
#         print(out)
#     else:
#         print(a)

# fun('ashraf')

# 23. [14:40, 11/8/2021] .: Write a program to check length of both string collection equal or not if 
# it is equal print the connection any one of the collection if it is not equal print both the 
# collection

# def fun(a,b):
#     if len(a)==len(b):
#         print(a)
#     else:
#         print(b)
# fun('helelo','heloo')

# 24. [14:40, 11/8/2021] .: Write a program to check whether both string collection equal or not if 
# it is not equal print the both string along with the length of a string if both are equal ignore it
# def fun(a,b):
#     if a==b:
#         pass
#     else:
#         print(len(a),len(b),a,b)
# fun('Ash','Ash')

# 25. [14:40, 11/8/2021] .: Write a program to check whether the given number lies between 1 to 
# 10 if it is true square that number if it is false cube that number
# def fun(a):
#     if a<=10:
#         print(a*2)
#     else:
#         print(a*3)
# fun(20)

# 26. To check whether both input variable pointing to same memory location or not if it is true 
# print last item of the second collection if it is false print the first item of the first collection 
# along with the memory address
# def fun(a,b):
#     if a is b:
#         print(b[-1])
#     else:
#         print(a[0],id(a))
# fun('hello','he1llo')
    
# 28. Ravi would like to buy a new cello or red pen the cost of the pen should be 10 if the pen 
# available on the shop he will buy the pen if it is not there he will come out of the shop

# def ravi(ravi):
#     if ravi=='cello' or ravi=='red':
#         print('finally purchased the pen')
#     else:
#         print('come out the shop')
# ravi('ok')

# 29. Write a program to check whether the middle of the item present in the list is string data 
# type or not if it is string print that list if it is not then print that items

# def fun(a):
#     out=len(a)//2
#     print(out)
#     if type(a[out])==str:
#         print(a)
#     else:
#         print(a[out])
# fun([1,2,3,4,6,'hello',4,5,'',7,8,9,'hello',6,5,(1,2,3)])

# def password(a):
#     upper=0 
#     lower=0
#     sep=0
#     num=0
#     if len(a) >= 8:
#         for i in a:
#             if "A" <= i <= "Z":
#                 upper+=1
#             elif 'a' <=i<='z':
#                 lower+=1
#             elif '0' <= i <= '9':
#                 num+=1
#             else:
#                 sep+=1
#     return upper,lower,num,sep
# valid=password('1')
# if valid[0]!=0 and valid[1]!=0 and valid[2]!=0 and valid[3]!=0:
#     print('valid passowrd')
# else:
#     print('non valid password')

# 43. WAP to print all the string data present inside an input list if it consists at least one ‘a’ in it
# def fun(a):
#     for i in a:
#         for j in i:
#             if j =='a':
#                 print(i)
#                 break
# fun(['hello','hai','bye','ashraff',''])
# 45. WAP to print square of all the numbers present inside the list.
# def fun(a):
#     for i in a:
#         if type(i)==int:
#             print(i*2)
# fun([1,2,3,4,5,'hello','1'])

# 46. WAP to print all the even number present in the position of odd index from the given list.

# def fun(a):
#     for i in range(len(a)):
#         if i%2==1 and a[i]%2==0:
#             print(a[i])
# fun([1,2,3,4,5,6,6,8])

# 53. Input: [1, 3, “LADDU”, 3+8j, 4-17j, {1:2,2:3,3:4},[826,4], 9.45, (112,180)]
# Output:Integer 2
# Float 1
# Complex 2
# Boolean 0
# String 1
# List 1
# Tuple 1
# Set 0
# Dictionary 1
# a=[1,3,'laddu',3+8j,4-17j,{1:2,2:3,3:4},[773,3],8.09,(112,109)]
# d={'int':0,'float':0,'complex':0,'bool':0,'str':0,'list':0,'tuple':0,'set':0,'dict':0}
# for i in a:
#     if type(i)==int:
#         d['int']+=1
#     elif type(i)==float:
#         d['float']+=1
#     elif type(i)==complex:
#         d['complex']+=1
#     elif type(i)==bool:
#         d['bool']+=1
#     elif type(i)==str:
#         d['str']+=1
#     elif type(i)==list:
#         d['list']+=1
#     elif type(i)==tuple:
#         d['tuple']+=1
#     elif type(i)==set:
#         d['set']+=1
#     elif type(i)==dict:
#         d['dict']+=1
# print(d)

# wap to elminate the odd index value

# def fun(a):
#     s=''
#     for i in range(0,len(a)):
#         if i%2==0:
#             s+=str(a[i])
#     print(s)
# fun('hello')
# 54. WAP to print all the odd numbers present in the even index position inside the string.
# def fun(a):
#     for i in range(len(a)):
#         if i%2==0 and a[i]%2==1:
#             print(a[i])
# fun([1,2,3,4,5,6,7,8])

# 58. WAP to print all the string items present in the odd position inside in the list.

# def fun(a):
#     for i in range(len(a)):
#         if type(a[i])==str and i%2==1:
#             print(a[i])
# fun([1,'hello',2,'3',4])

# 1. WAP to print 3rd multiplication table.

# a=int(input('give the range'))
# b=int(input('choose the tabel'))
# for i in range(1,a+1):
#     print( i,'*',b,'=',i*b )


# 63. Python Program to find Sum of Even Numbers

# def fun(a):
#     sum=0
#     for i in a:
#         if i % 2== 0:
#             sum+=i
#     print(sum)
# fun([2,1,2,1,2])

# 85. Python program to Remove Odd Characters in a String

# def fun(a):
#     out=''
#     for i in range(len(a)):
#         if i %2==0:
#             out+=a[i]
#     print(out)
# fun(['hello','bye'])


# 102. Write a program to convert the upper case letter to lowercase letter and lowercase 
# letter to uppercase letter if the character is number 3 place with the zero if the character is 
# special symbol replace with * for the given input string
# def fun(a):
#     out=''
#     for i in a:
#         if 'a'<=i<='z':
#             out+=i.upper()
#         elif 'A'<=i<='Z':
#            out+= i.lower()
#         elif '0'<=i<='9':
#             out+='0'
#         else:
#             out+='*'
#     print(out)
# fun('ASHRAFFashraff333@@@')
        

# 105. WAP to check whether both input numbers are even or odd. I both inputs are odd 
# perform addition operation. If any one of the input is even perform multiplication operation.

# def fun():
#     a=int(input('enter a value'))
#     b=int(input('enter b value'))
#     if a%2==1 and b%2==1:
#         return a+b
#     elif a%2==0 or b%2==0:
#         return a*b    
# print(fun())

# 106. WAP to check whether length of the string is even or odd. If it is even print that 
# string 10 times. If it is not print 5 times.

# def fun(a):
#     if len(a)%2==0:
#         return a*10
#     else:
#         return a*5
# print(fun('hello0'))

# 107. List_1=[1,2,5,”HAI”,”Hello”,4+10j] , 
# List_2=[3,”GOOD”, “HAVE”,”A”,”NICE”,”DAY”]
# WAP to check whether the first item of these two lists either integer or not. If it is 
# integer concatenate these two lists or else print memory address of these two lists.

# def fun(a,b):
#     for i,j in zip(range(0,len(a)),range(0,len(b))):
#         if type(a[0])==int and type(b[0])==int:
#             return a+b
#     return id(a),id(b)
# print(fun(['10',20,30],[10,20,30]))

# 109.WAP to find digits of the number by using len function. If it is one print ‘One Digit’ along 
# with that number. If it is Two print ‘Two Digit’ along with that number. If it is three prints ‘Three 
# Digit’ along with that number. If it is greater than three just print that number

# def fun(a):
#     if len(a)==1:
#         return 'one',a
#     elif len(a)==2:
#         return 'two',a
#     elif len(a)==3:
#         return 'three',a
#     elif len(a)>3:
#         return a
# print(fun('12'))
    
# 110. WAP to check whether the given item is present in the third item of the list or not. If it is
# present print first item of the list. If it is not print last item of the list.
# def fun(a):
#     check=eval(input('enter find value'))
#     if check in a[3]:
#         return a[0]
#     return a[-1]
# print(fun('helksjfbgdsfbmdshgmshlo'))

# 111.WAP to check given input character is vowel or not. If it is vowel print ascii value of that 
# character. If it is not print square of that ascii value

# i='k'
# if i in 'aeiouAEIOU':
    # print(ord(i))
#else:
# print(ord(i)*2)

# 112.WAP to print middle number of the given input number when the given input number is odd. If 
# it is even print invalid number
# def fun(a):
#     mid=len(a)//2
#     if a[mid]%2==1:
#         print(a[mid]) 
#     else:
#         print('invlaid')   
# fun([1,2,3,3,5,6,7]) 

# 113.WAP to print character of the given input ascii values . If the given input number lays between 
# from 33 to 126 print the character of respective ascii number. If it is not print invalid number 

# a=input('enter the char') #n
# if ord(a)>=33 and ord(a)<=126:
#     print(ord(a))
# else:
#     print('invlaid')

# find leap year

# def fun(a):
#     if a%400==0 or a%4==0 and a%100!=0:
#         print('leap')
#     else:
#         print('non leap')
# fun(2100)

# 73. Python program to Count Occurrence of a Character in a String
# def fun():
#     st=str(input('enter the value'))
#     temp=''
#     out=''
#     for i in st:
#         if i not in temp:
#             temp+=i
#         else:
#             out+=i
#     print(len(out))
# fun()

# natural num starts from 1
# whole num starts from 0

# to find the avg of naturals num
# a=[1,2,3,4,5,6]
# s=0
# for i in a:
#     s+=i
# print(s)
# print(s/len(a))

# # 79. Python program to Print First Occurrence of a Character in a String

# def fun():
#     st=str(input('enter the value'))
#     temp=''
#     out=''
#     for i in st:
#         if i not in temp:
#             temp+=i
#         else:
#             out+=i
#     print(out[0])
# fun()

# 80. Python program to Print last Occurrence of a Character in a String

# def fun():
#     st=str(input('enter the value'))
#     temp=''
#     out=''
#     for i in st:
#         if i not in temp:
#             temp+=i
#         else:
#             out+=i
#     print(out[-1])
#     print(out)
# fun()

# 87. Python program to Print remove First Occurrence of a Character in a String

# def fun():
#     st=str(input('enter the value'))
#     temp=''
#     out=''
#     for i in st:
#         if i not in temp:
#             temp+=i
#         else:
#             out+=i
#     res=list(out)
#     res.pop(0)
#     print(res)
# fun()


# 87. Python program to Print remove last Occurrence of a Character in a String

# def fun():
#     st=str(input('enter the value'))
#     temp=''
#     out=''
#     for i in st:
#         if i not in temp:
#             temp+=i
#         else:
#             out+=i
#     res=list(out)
#     res.pop(-1)
#     print(res)
# fun()

# 103. Write a program to print all the string values present inside the list if the length of 
# the string is odd under first character starts with vowel

# def fun(a):
#     if len(a)%2==1:
#         for i in range(len(a)):
#             if a[i][0] in "AEIOUaeiou":
#                 print(a[i])
# fun(['hello','apple','oramge'])

