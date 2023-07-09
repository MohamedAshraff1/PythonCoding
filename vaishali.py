# 1. WAP to check the given string is starts with upper case or not.
# st='ashraff'
# if "A" <= st[0]<='Z':
#     print(True)
# else:
#     print(False)

# 4. WAP to check given string is startswith vowels or not.
# s='ashraff'
# if s[0] in 'aeiouAEIOU':
#     print(True)
# else:
#     print(False)

# 11. WAP to check given char is Special symbol or not.
# sy='9'
# if sy != 'a' <= sy <= 'z' or '0' <= sy <= '9':
#     print('sy in not a symbol')
# else:
#     print('sy is symbol')

# 12. WAP to check middle element of the list is even or not.

# l=[1,2,3,4,5]
# mid=len(l)//2
# if l[mid]%2==0:
#     print('even')
# else:
#     print('odd')

# 13. WAP to check whether the given value is divisible by 6 or not, if divisible by 6 print cube of that value or else perform left shift operation step 3.

# div=int(input('enter the number'))
# if div %6==0:
#     print(div**3)
# else:
#     print('No')

# 16. WAP to check which is the smallest number among 4 numbers.
# a=int(input()) 
# b=int(input()) 
# c=int(input())
# d=int(input())  
# if a>b and a>c and a>d:
#     print('a is gr')
# elif b>c and b>d:
#     print('b is gr')
# elif c>d:
#     print('c')
# else:
#     print('d is gr')
 
# 18 WAP to print series of 20 natural numbers.
# nat=int(input())
# for i in range(0,20+1):
#     if i != 0:
#         print(i)
#     else:
#         continue

# 19 WAP to print the series of upper case characters.
# s='ashraff'
# print(s.upper())

# 20 WAP to print the series of upper case characters in reverse.
# s='ashraff'
# upp=s.upper()
# rev=''
# for i in upp:
#     rev=i+rev
# print(rev)

# 23. WAP to count number of accurances of specified element in that collection.
# s='ashraff'
# temp=''
# c=0
# for i in s:
#     if i not in temp:
#         temp+=i
#     else:
#         c+=1
# print(c)

# 24. WAP to find the position of first accurance of the specified character.
# s='ashraff'
# sp='f'
# temp=''
# for i in range(0,len(s)):
#     if s[i] not in temp:
#         temp+=s[i]
#     else:
#         if s[i]==sp:
#             print(i)
#         else:
#             print('char not present')
# # 25. WAP to replace specified character by given new character  without using inbuilt method. (replace "a" with "b")
# s='ashraff'
# l=list(s)
# new='k'
# re='f'
# temp=''

# for i in range(0,len(l)):
#     if l[i] not in temp:
#         temp+=l[i]
#     else:
#         if l[i]==re:
#             l[i]=new                  
# print(str(l))
# 27.WAP to store all the data items inside the collection in reverse order without using builtin methods
# l=[10,20,30+0j,'hi',[90,99],(6,),{5,0},{'hai':9}]
# rev=[]
# for i in l:
#     rev=[i]+rev
# print(rev)

# 29 WAP to append each and every value to a list. (extractelements from nested)
# a = [[1,1,1],"hai", (2, 3, 4),[1,2], 4.2+3j, 6,{"a":1, "b" :2}, ["hello","good", "morning"],"hai",['hai']]
# temp=[]
# out=[]
# for i in a:
#     if type(i)!=list:
#         out+=[i]
#     else:
#         for j in i:
#             if type(j)!= int:
#                 for k in j:
#                     temp+=[k] 
#             else:
#                 temp+=[j]  
# out+=temp         
# print(out)
# output=['hai', (2, 3, 4), (4.2+3j), 6, {'a': 1, 'b': 2}, 'hai', 1, 1, 1, 1, 2, 'h', 'e', 'l', 'l', 'o', 'g', 'o', 'o', 'd', 'm', 'o', 'r', 'n', 'i', 'n', 'g', 'h', 'a', 'i']


# a=int(input())
# b=int(input())
# c=int(input())

# if a>b and a>c:
#     print(c)
# elif b>c and b>a:
#     print(a)
# else:
#     print(c)
# class sam:
#     def __init__(self,a):
#         self.a=a
#     def __len__(self):
#         return len(self.a)
#     def __contains__(self,con):
#         return con in self.a
#     def __setitem__(self,index,new):
#         self.a[index]=new
#     def __getitem__(self,index):
#        return self.a[index]
# oa=sam([1,2,3])



# practice in my home 

# 33. WAP to extract special characters from give string and store  in a list.
# s = "$hello$ *Good* #morning# @#$%"
# for i in s:
#     if 'a'<=i<='z' or 'A'<=i<='Z' or '0'<=i<='9':
#         continue
#     else:
#         print(i)


# 34. WAP to split all the words and store in a list without using  inbuilt methods.   

# s='hello hai riju jsnd askjdfna khsadb                                       '
# l=[]
# k=''
# for  i in s:
#     if i!=' ':
#         k+=i
#     else:
#         if len(k)!=0:
#             l+=[k]
#         k=''
# if len(k)!=0:
#     l+=[k]
# print(l)
# 36. WAP to return position of first accured specifies character

# s='hai hello keduvaan'
# specified=str(input('enter specified char'))
# for i in range(0,len(s)):
#     if specified==s[i]:
#         print(i)
#         break
# 37  WAP to return position of first accured specifies character  without using inbuit method and without using range.
# s='hai hello keduvaan'
# specified=str(input('enter specified char'))
# i=0
# while i < len(s):
#     if s[i]==specified:
#         print(i)
#         break
#     i+=1
# 40. WAP to reverse characters in words in a list.
# l=['ashraff','hamza','rijwan']
# out=[]
# i=0
# while i < len(l):
#     out+=[l[i][::-1]]
#     i+=1
# print(out)
# 49. WAP to get given o/p
# 	l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 	o/p [1, 2]
# 	 [3, 4]
# 	[5, 6]
# 	 [7, 8]
# 	 [9]
# l=[1,2,3,4,5,6,7,8,9,10,11,12,100]
# out=[]
# i=0
# while i < len(l)-1:
#     out=[l[i]]+[l[i+1]]
#     print(out)
#     i+=2
# if len(l)%2==1:
#     out=[l[-1]]
#     print(out)

# 52. WAP that returns a list of names starting with vowels in string.
# s = ['ateve', 'laura', 'bill', 'james', 'bob', 'greg', 'scott']
# for i in s:
#     if i[0] in 'aeiouAEIOU':
#         print(i)


# 54. WAP to filter the names which are less than 6 characters.
# s = ['apple', 'google', 'yahoo', 'gmail', 'flipkart', 'instagram', 'microsoft']
# l=[]
# g=[]
# for i in s:
#     if len(i)<6:
#         l+=[i]
#     else:
#         g+=[i]
# print(f'less than 6 char is {l}')
# print(f'gr than 6 char is {g}')

# 57. WAP to create a dictionary with word and its length pair only if it is even length.
# s = 'hey guys good afternoon welcome to python session'
# s=s.split()
# d={}
# for i in s:
#     if len(i)%2==0:
#         d[i]=len(i)
# print(d)

# 58. WAP to print index and word pair if word is even length keep it as it is else reverse it.
# s = 'hey guys good afternoon welcome to python session'
# s=s.split()
# d={}
# for i in range(0,len(s)):
#     if len(s[i])%2==0:
#         d[i]=s[i]
#     else:
#         d[i]=s[i][::-1]
# print(d)

# 59. WAP to flip the keys and values of dictionary using dict comprehension.
# d = {'a': 1, 'b': 'hello', 'c': '85', 'd': 12.3, 'e': (1, 2, 3) }
# l=list(d)
# o={}
# for i in l:
#     o[d[i]]=i
# print(o)

# 61. WAP to grouping cars and bikes in below list.
items = ['Honda-bike', 'audi-car', 'bmw-car', 'apache-bike', 'bullet-bike', 'skoda-car', 'renault-car','fz-bike','bike' ]
car=[]
bike=[]
for i in items:
    b=i.lower()
    if b[-4::]=='bike':
        bike+=[i]
    elif b[-3::]=='car':
        car+=[i]
print(f'list of car {car}')
print(f'list of bike{bike}')






