print('MTA EXAM PREPARATION')
'''
https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
''' #link for Questions
#level 1 Q1
"""ls=[]
for piece in range(2000,3201):
    if piece % 7 == 0 and piece % 5 !=0:
        ls.append(piece)

print(','.join(str(x) for x in ls))"""

#level 1 Q2
"""def factorial(x):
    if x in [0,1]:
        return 1
    return x * factorial(x-1)

print(factorial(8))"""

#level 1 Q3
"""def power_dictionary(n):
   return dict((i,i*i) for i in range(1,n+1))

print(power_dictionary(8))"""
#level 1 Q4
"""string=input('3,4,5 ==> : ')
print(string.split(','))
print( tuple( string.split(',') ))"""

#level 1 Q5

"""class Get_Print_String():
    def getstring(self):
        self.got_string = input("=> ")
    def printstring(self):

        return self.got_string.upper()
strObject = Get_Print_String()
strObject.getstring()
print(strObject.printstring())"""
#level 2 Q6

"""import math

string = input('=> ')
ls=[int(piece) for piece in string.split(',')]
result_ls=[str(int(math.sqrt( (2*50*var)/30 ))) for var in ls]
print(','.join(result_ls))"""

#level 2 Q7
"""dimensions = list(map(int,input(' = >').split(',')))
result_lsofls=[ [base*power for power in range(dimensions[1])]for base in range(dimensions[0])]
print(result_lsofls)"""

#level 2 Q8
"""print( ','.join( sorted( input('=>').split(','), key=lambda  piece: piece[0]) ) )

"""

#level 2 Q9
"""string_taken=[input("").upper() for take in range(2)]
print(*[out for out in string_taken],sep='\n')
"""

"""ls=list()
ls.append(input(''))
while ls[-1] !='.':
    ls.append(input())
    # print(ls)

print(ls)"""
"""
this program will start taking input when user only give dot . as input
```
ls=list()

ls.append(input(''))
while ls[-1] !='.':
    ls.append(input())
    # print(ls)

print(ls)
```

Input 

```
Greeting
God bless you
I am muslim 
who is certain That there is no GOD except One 
and Prophet Muhammad is The last messenger
and I would Encourage you to Read and discuss your Question to clear you perspective by asking the relevant person

There is a life after death 
and this world is a place of test with few goods init
those who believe in Islam and do good deeds will be in heavens
and those who rejected God for this short period of wordly life 
all will reject them hereafter

God will surely show you HIS signs with in you and in this world
Those who belive in HIM without seeing HIM


....


.

```
Output
```
['Greeting', 'God bless you', 'I am muslim ', 'who is certain That there is no GOD except One ', 'and Prophet Muhammad is The last messenger', 'and I would Encourage you to Read and discuss your Question to clear you perspective by asking the relevant person', '', 'There is a life after death ', 'and this world is a place of test with few goods init', 'those who believe in Islam and do good deeds will be in heavens', 'and those who rejected God for this short period of wordly life ', 'all will reject them hereafter', '', 'God will surely show you HIS signs with in you and in this world', 'Those who belive in HIM without seeing HIM', '', '', '....', '', '', '.']

`````
"""

#level 2 Q10
"""import pandas as pd
s=pd.Series(data=input().split(' '))
s.drop_duplicates(keep="first",inplace=True,)  #or use set to remove duplicate :)
print(sorted(s.tolist()))"""

#level 2 Q11
#for loop to check if list element %2==0               mapping binary to decimal using lambda as function and values   taken as input
"""binary_input=print(*[check for check in list(           map( lambda x: int(x,2),input('=> ').split(','))) if check %2 == 0])

"""

#level 2 Q12
# for loop to get values      if condiction on value -->all(checking each digit and give each digit place True or False status )
"""ls = [ str(value) for value in range(1000,3001)if all([ True if int(digit)%2==0 else False   for digit in str(value) ]) ]
print(','.join(ls))
"""

#level 2 Q13
"""sentence=input('=>')
import re
print('DIGITS : ',len(''.join(re.compile(r'[0-9]').findall(sentence))))  #seperatly doing to find len of digits
print('LETTERS : ',len(''.join(re.compile(r'[\w]',re.IGNORECASE).findall(sentence))))
"""

#level 2 Q14
"""import re
sentence=input('')
print('UPPER :',len(''.join(re.compile(r'[A-Z]').findall(sentence))))
print('LOWER :',len(''.join(re.compile(r'[a-z]').findall(sentence))))
"""

#level 2 Q15
"""digit=input('=> ')
result=0
for times in range(1,5):
    value=int(digit*times)
    result+=value
print(f"{'+'.join([digit*times for times in range(1,5)])} results as => : ",result)
"""
#level 2 Q16
"""# using map (lambda to find square of odd, list of odd to get list of add use for if  for to iterate from input if for condition check %2!=0)
print ( ','.join(list(map(lambda odds :str(int(odds)*2),[value for value in input('').split(',') if int(value)%2!=0])) ))
"""

#level 2 Q17
"""structure=tuple(input("=> ").split(' '))
account=0
while structure[0] !='stop':

    if structure[0].upper()=='D':account += int(structure[1]); print('balance now :',account)

    elif structure[0].upper() == 'W': account -= int(structure[1]) if account - int(structure[1]) >=0 else print('get credit you don\'t have enough to take out'); print('balance now :',account)

    else : print('wrong structure try to use\n D 400 for deposit \n W 400 with draw')
    structure = tuple(input("=> ").split(' '))"""
"""structure=tuple(input("=> ").split(' '))
account=0
while structure[0] !='stop':

    if structure[0].upper()=='D':
        account += int(structure[1])
        print('balance now :',account)

    elif structure[0].upper() == 'W':
        if (account - int(structure[1])) >=0:
            account =account - int(structure[1])
        else:
            print('get credit you don\'t have enough to take out')

        print('balance now :',account)
    else:
        print('wrong structure try to use\n D 400 for deposit \n W 400 with draw')

    structure = tuple(input("=> ").split(' '))"""


#level 3 Q18
"""import re
accepted=[]
passwords = input("").split(",")
for each_password in passwords:
    ls=[]
    if len(each_password)  in list(range(6,13)) :
        for each_condition in [r'[a-z]',r'[0-9]',r'[A-Z]',r'[$#@]']:
             if any(re.compile(each_condition).findall(each_password)):
                 ls.append(True)
             else:
                 ls.append(False)
        if all(ls)==True :
            accepted.append(each_password)
print(accepted)"""

#level 3 Q19
"""n_age_h = [tuple(input("").split(','))]
while n_age_h[-1] != ('.',):
    n_age_h.append(tuple(input("").split(',')))
del n_age_h[-1]
def fun(x):
    return x[0],x[1],x[2]
print(*sorted(n_age_h,key=fun),sep='\n')"""

"""Tom,19,80
John,20,90
Jony,16,94
Jony,17,93
Jony,10,90
Json,21,85
John,20,90
Jony,16,94
Jony,17,93
Jony,10,90
Json,21,85"""
#########
"""from operator import itemgetter
inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
print(list(map(itemgetter(1),(inventory))))"""
"""
#adding number less then 4
from functools import reduce
def numeric_compare(x,y):
    print('-->',x,y)
    if y<4:
        print('ppp',y)
        return x+y
    else:
        return x
print((reduce(numeric_compare,[0,5, 2, 4, 1, 3] )))"""
#level 3 Q20
"""class Divisibal_By():
    def __init__(self,d,n):
        self.d=d
        self.n = n

    def span(self):

        for i in range(self.n):
            if i%self.d==0:
                yield i
            else:
                continue


obj=Divisibal_By(7,100)

one_at_a_time=obj.span
print(one_at_a_time())
print(one_at_a_time())
print(one_at_a_time())"""

##################orelly
"""a=1
b=2
print(a+b)
print(a+x) #error we did not tell what x was
"""
"""
in most languages we would say that a variable is a
'named storage location'
But that is NOT TRUE for python
in python a variable is jus a name
that means  it has no attributes and no memory 
location, until it is assigned as a name for a piece of data -that data supplies the attributes
Remember ,a varaible is just a name
u dont declear it u just assign it
and attributes of any variable are attributes of data which assign to that varaible

don't think variable name has particula place in memory
don't think it store particular kind of data it does not
it is just a name of any kind of data that you want to represent

to increment u first has to declare it
n = n +  1 #this will fail

n = 5   #start with initialy value  #assigment is a action #first we assign value to n
n = n + 1  #second time we will re assign new value

n = n + 1 #is not incrementing it is re assingment 
"""  # assignment part 1
"""
#combined add/assign 
n+=    ----> n = n + 1    ( n getting add up and getting redefined and re assigned , n is not incrementing in reality it is re assign remeber n come first,  
n*=expr ---> n = n*expr   (from  n we are multiplying, remember n come first)
n-=expr  ---> n = n - expr ( from n we are taking -1 , remember n come first)
n/=expr --> n = n/expr  (remember n come first)
in python when we assign  a variable to a number
we actually giving a name  to a path that leads us to  that number
so variable name is just a path to number in reality it does not have memory located
like in other languages you declear a variable and in memeory your language give specific sapce to that variable
but in python you are only creating a button that will leads you to  number store in memeory 
"""  # assignment part 2
"""
first character must be underscore _ or letter 
subsequent character must be an underscore _ ,letter, or digit
No embedded spaces
No kewords, if,else,def,for,and,in,or
all names in programs are case sensitive x is not equal to X
first character cannot be a number it will confuse it with actual number 
"""  # rule for variable name
""" 
A comment consists of everything from 
the hash tag(#)-outside a quoted string-
to end of line

a = b # a assigned val. of b
"""  # add comments hash tag
"""
in python u create variable u can't just
don't declare it
x=int()
print(x)
it give output -> 0
see it did not declare it gave 0 a name x 
where 0 is int
x=str()
print('->>',x,'<---')
it printed->> <--- blank space so it assigne blank space
x=float()
print(x)
output --> 0.0
see it assign value a name x 
we can't just only declare a variable
x=list()
print(x)
output --> [] see empty list with no value 
x=tuple()
print(x)
output ---> () it gave empty tuple we can't declare a variable
minimum is to give empty tuple
x=dict()
print(x)
output ---> {} same case 
what about bool ??
x=bool
print(x)
out put --> <class 'bool'>
x=None
print(x)
output --> None

what about null ??
what about None ??
or is there undefined ??
"""  #assignment summery
'Boolan data types'
#understanding numeric and boolean data type
"""
integer have no fractional portion,
but the are always absolutely precise,
Example -10,3000,1 (they can positive,negative)
but the cannot contain fractional protion

Floating point numbers have a fraction portion but potentially have 
rounding error
Examples 2.5,-100,7,2.35e27,1.0
"""#integer vs Floating  points
"""
integer in most language are very limited 
for example 16 bit integer can only be as big as 64k
but in python
integer has no limitation other then physical limitation of a system
for example
"google"(googol) is 10 to the 100th 
far bigger then the no of particles in universe
"""#infinite integers in python
"""
g =10**100
print('{:,}'.format(g))  #this give 10,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000
print('{:,f}'.format(g)) #10,000,000,000,000,000,159,028,911,097,599,180,468,360,808,563,945,281,389,781,327,557,747,838,772,170,381,060,813,469,985,856,815,104.000000
print(float(g))#10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
print((float(g)))#1e+100
print('{:f}'.format(float(g)))#10000000000000000159028911097599180468360808563945281389781327557747838772170381060813469985856815104.000000
print(g == g + 1) #False #thing about integers is tha thtey are absolutly precise  this means it s that tiny tiny  change get recorded and not thrown away
print(1.000000 == 1) #True
== is use to test whether two values on sides are equal or not and it give suse True or False bool
"""#google vs google + 1
"""
cool thing about python is that every thing is object
every single piece of data is object
what i mean by that is 

simply put, an object is a data type
through which you can call special functions,
called 'methods'

object: is also data with build in capabilities
thats also cool even integer have build in capabilities

but to use those capabilities we use method
and to use them we put . againts object
and name of method and then () argument if needed

example object_name.method_name(arguments)



"""#integers,objects and methods
"""
what does it means to say that every piece of
data is an object??
it means that every object supports
"methods" supplied by python.
you can see a list of methods supported for integer
by typing
help(int)  #to see all methods for integers
"""#objects and methods (part1)
"""
a=4
print(a.bit_length()) #no of bits required to for integer
output--> 3


print('{:b}.format(a)') out but will be in bites
output ---> '100' <---because 4 decimal in bits ==100



note 4.bit_length() #will not work because
4. looks like floating point so that would'nt work

but (4).bit_length() #will work


1 bit for 1
2 bit for 2
3 bit for 3-4
4 bit for 5-8
5 bit for 9-16
6 bit for 10-32
7 bit for 33-64
8 bit for 65-128
""" #bit required for integer integer Methods
"""
floating point numbers contain a fractional portion
drawback is that floating point numbers
have limited precision, leading to rounding
error in the case of very large or tiny numbers
"""#floating points Pros and Cons
"""
/ give regular division 3 /5 -> 0.6
// give floor division  3 // 5 -> 0
%  give reminder ->     3 % 5 -> 3

"""#Division in python 3.0
"""
1.'Dot' operator,parentheses

2.highest-Exponentiation operator **

3.Multiply,Division,Mod Operators
*,/,//,%
print(2/2*4) #gives 4.0 both / * belong to same group in this case calculation happen left to right so first / then *
print(2*2/4) #gives 4.0 first * happen then /

4.Additon subtraction '+' '-'

5.Comparison,Boolean operator (explained later)

6.Assignment and Combined  Assignment Ops
"""#operator precedence

"""
examples
2**3 *10 + 2*5  is equal to  ((2**3)*10)+(2*5) 

---combined operation +=,*=,-=,/=  ------
x*=2+3 is not equal to x=x*2+3 but:
x = x* (2+3)
x*=2+3 in this first left hand side computed 2+3=5
then *= get executed which is x = x*5
so combined operation perform after + -
x*=2+3 ---> x = x* (2+3)
x/=2+3  ---> x = x/(2+3)
x+= 2-3 ---> x = x+(2-3) 
"""#operation Precedence (Example)
"""
x=2
x*=2+3
same to 
x=2
x=x*(2+3) 
"""#assignment or combined assignment *= += always carry out on last

#BOOLEAN DATA TYPE
"""
-Boolean data is either True or False
 its important in if,while and for as we'll see

-But other type of data automatically convert to bool
 type as needed
-bool(n)->True if n is any nonzero number.
-bool(0)->False
-bool()->False #same as bool(None) 

all automatically converted in to boolean True when come under bool() logic
all True
print(bool(''),bool(0),bool(0.0),bool([]),bool(()),bool(set()),bool({}),bool(),bool(None),bool(False))

all automatically converted in to boolean False when come under bool() logic
all False
print(bool(' '),bool(1),bool(0.0001),bool([0]),bool((0,)),bool({0}),bool({'':''}),bool(True))

"""#boolean Data
"""
first 6 comes out as True or False
as these are 
---comparions operators--
1. == Test for quality
2. != Not equal test
3. > Greater than 
4. < Less than 
5. >= Greater than or equal to 
6. <= Less than or equal to 
---these below will be use to combine boolian condtions most of it---
and logic AND
or  logic OR
xor logical ExclusiveOR #it does not take duplicates 1,1 = 0     0,0=0
not Logical negation
"""#boolean operators
"""
-we don't declare variables
-the don't have fix type of variable
-The same x can be a name for any kind of data type

x = 1
x ='I am a string'
x=[0,1,22,4]
its look like x type is constantly changing but its not
infact you are using x in different contexts

"""#remember,Varaibels are Just Names
"""
like i,j,k,l,m,n for integers
x,y,z for floating point values
s1,s2,s3 or xx_str for strings
xxx_ls or ls,ls1,ls2 for list
"""#develop naming conventions
"""
most common numeric type is integer and floating-point
integers are infinite and absolutely precise
floating point advantage is that it can hold fractions but are not precise
Boolean (True/False) is also important
"""#summary numeric type
"""
print(x=2) #this give error as type error as we cannot assign in print
print(x==2)#this is now comparison operator so it will work in print
"""


"""
we can slice a string using indexing 
but we cannot assign a part of string 
new value using indexing
s='hello'
s[0] ='H'  #this give error because string is immutable
how ever
s='Hello' #is valid
"""#Slicing string







#input output
# x=input('=> ')
# print('{:_<12.7}hr'.format(x))
'12 means is the space located for x'
'<  means x will start from left of this 12 open space'
'_ means any left over space fill with this'
'.7 means strip text from 1-7 only show text 1-7 which is x'
# print('{:_^8d}'.format(int(x)))
# print('%-7.3dhr'%(int(x)))
"""from datetime import datetime
print(datetime.strftime(,datetime.today())
print('{:%C%y == %Y\"""n%B == %m\n%A == %d }'.format(datetime(2020,3,5,6,56)))
# FILE INPUT OUTPUT



#print('love '.rstrip()+'hi')
#lovehi

#print('i'+'love'+'u')
#iloveu

#print('i','love','u')
#i love u

#print('love'.ljust(5,'0'))
#love0

# x='dog'
# y='dog'
# print(x is y)
#True  -because there value has same -id

#print('dog' is 'dog')
#True -because they belong to same -id


# x=0.0
# y=0
# print( x is y)
# False because 0 has different -id then 0.0 -id

#print(0==0.0)
#x=0.0
#y=0
#print( x == y)
#True because it only compare values in quantitative  manner

# print(0 is 0.0,id(0),id(y),id(0.0),id(x))
# False,140734818980640 140734818980640 2144340583120 2144340583120

# --String--
# "double "
# 'single'
""" #multi line for documentation


# r''. r" ". r""" """ presereve all character
# \n \t \ there are special but in r'' the come in there form
#in r'' if we but \n we get printed \n
#in '' or "" or  """ """ if we use  \n it means next line
#\t measn tap
#print(4%3) # in reminder we don't go above 4 either keep 3 multiple lower or  equal
#print(-4%3)  # in this we also want to keep 3 multiple lower then  -4 so we go to 3(-2)=-6 now -6 is lower then -4 and we can change back multiple sign and get +6-4=2
#print((-4)%(-3)) #this show that denominator sign will always dominate in reminder
#print(4%-3) # denominator sign is dominated
#rule of thumb when there is sign difference
#go beyond  numerator value and keep denominator sign

#when there is no sign difference keep below
#numerator and change sing for subtraction moment
#print(-4%7)
# isnumeric() accept all other types of numeric roman chines etc
# isdigit() only accept 0-9  no decimal point
# isalnum() have option either alphabhet or numeric

# isalphat() only abc
#is mean --inside string

# def age(a):
#     rating=''
#     if a==None:rating='C'
#     elif a<13:rating ='C'
#     elif a <18:rating='T'
#     else:rating='A'
#     return  rating
# print(age(30))
#
# print(int(-1E+10))

"""try:
    print(7/0)
except ZeroDivisionError as e:
    print(8/0)
except ZeroDivisionError as e:
    print(9/1)
else:
    print('l')
finally:
    print('end')"""
# with open('aaaaaa.txt') as f:
#     pass
# import math
#
# print(math.floor(-13.6))

"print('grgerg'.replace('g','1',2))"

"""import time
import datetime
s=(time.time())
for x in range(5000000):
    print(x)
d=time.time()-s
print(datetime.timedelta(seconds=d).)
""" #time of program run using time module and datetime


#### Things to do
## os
## os.path
## sys done
## random done
## datetime
## time
## open() as f and modes read file write file
##eval done
##Exceptions
"""print('-'*30)
import random
#random.randint(1,30) give integer from 1-30 both included
for i in range(0,6):
    print(random.randint(1,10)*3) #randint include both limits
""" #randint
"""import random
x = ['5', '1', '2', '3', '4']
for i in range(30):
    random.shuffle(x,random=lambda : random.random)
    print(x)""" #shuffle
"""import random
a=['a','b','c','d','e']
dic={}
for i in range(1,101):
    print(a)
    random.shuffle(a)
    dic['{0:_<4d}std'.format(i)]=a
    print('=>',dic['{0:_<4d}std'.format(i)])
# print(dic)
dic.update()""" #shuffle

"""import  random,keyboard
ls=input('range=> 1-10: ').split('-')
while True:
        a=random.randint(int(ls[0]),int(ls[1]))
        print(a)
        if keyboard.is_pressed('s'):
                print('------')
                print('selected',a)
                break
          """ #random

"""
import keyboard

while True:
    print('please say yes')
    if keyboard.is_pressed('ENTER'):
         break
print('i got u :) ')
print('i was trying to write you are a idiot ')
print('  :( ')""" #keyword

"""import sys
#to run file in terminal --
# >py file.py argument1 argument2 argument3

sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')
sys.stdout.flush()

print(sys.argv)""" # complete file path as string in list
#sys.argv will display all of the arguments
"""import sys
x=sys.argv  
print('this is x : ',x[1])""" #basically --sys.argv-- is a list that takes input from command line
#benefit of sys.argv list is that you don't need to open file
#you can run file from command line
#python file.py 1argument 2arugment . . .

"""import sys

print(len(sys.path))

for i in sys.path:
    print(i)

import os
import time,datetime
print(datetime.datetime.fromtimestamp(time.time()))
os.getcwd()"""

"""a='config1'
print(a)
b=a
a+='config2'
print(a)
print(b)"""

"""import os
print(os.getcwd())

path_split=os.path.split(os.getcwd())

print(path_split)

file=path_split[-1]
file_path=path_split[0]

print(os.path.join(file_path,file))
print(os.path.isfile('MTA_exam_prepration.py'))"""

"""with open('final.txt') as f:
        for line in f.readlines():
            if line =='\n':
                continue
            else:
               with open('newfinal.txt','a+') as nf:
                   nf.write(line)
""" #removing spaces and inputting in newfile
"""with open('final.txt') as f:
    while True:
        string=f.readline()
        print(string)
        if string =='\n':
            continue
        elif string =='':
                break

        else:
            with open('new_final.txt','a+') as new_f:
                new_f.write(string)""" #breaking while loop at the end of text and remove entries
"""with open('final.txt') as f:
    para=0
    while True:    #come back and search for line which has no '\n' and if '' means end if file
        line= f.readline()
        if line !='':    #if line is empty means no more data
            if line == '\n':   #between paragraphs we always have '\n'
                continue       #looping out all '\n' to  find line without '\n'
            elif line != '\n':  # line without '\n' and '' is  new para graph
                   #first line of a paragraph
                para+=1
                print('so far paragraphers are :',para)
                while True:
                    if line not in ['','\n']: #checking paragraph brakers it not then paragraph continue

                        line = f.readline()
                        continue        #looping out all to find  '\n' or '' to reach end of paragraph
                    else:   #this mean line is either '' or '\n'
                        break
        else:
            break
print('finally total paragrpahs are :',para)""" #total paragraphs counter
"""
''    means end of data and no more data. 
'\n'  means there is more data but user have pressed enter in documents
""" #tips tricks

"""with open('final.txt') as f:
    table_line=0
    loop=0
    while True:
      line=f.readline()
      constant=loop-table_line
      loop+=1
      c=0

      if len(line.split(',')) ==3 :
          d=c
          with open('table_final.txt','a') as t:
              ls=line.split(',')
              table_line+=1
              t.write('{0:<10s}{1:>5s}{2:>5s}'.format(*ls))
              if loop-table_line==constant:
                  c=1
                  if c>d:
                    t.write('--------\n')
                    d=1



      elif line !='':
          continue
      else: break
""" #text csv table extracter from with in paragraphs

"""age=input('enter your age :')
age=int(age)
print(age)
import datetime
year_now=datetime.datetime.today().year
print(year_now)
born_year = year_now - age
print(born_year)""" #input age and get when your year born
# print('float(2) = ',float(2))
# print("float('2') = ",float('2')) #it takes hex,binary,oct and Bool and convert it in to float, BUT with integer it has special relation it convert integer into float even if integer is string just like it convert string float to float number
#
# print("""\nfloat("'2'") = value error """)
# print("""float(eval("'2'")) =""",float(eval("'2'")))

"""print('\nfloat("2.2") = ',float("2.2"))

print('\nfloat(True) = ',float(True))
print('float("True") = ','value error')

print('\nfloat(0b101) = ',float(0b101))
print("float('0b101') = ",'value error')

print("\nrule of thumb :::\n float('2') ok\n float('2.2') ok\n rest best be without string Ok ")

print('\n\n integers')
print("int('2') = ",int('2'))
print("int(2) = ",int(2))

print("\nint('2.2') = value error")
print('int(2.9) = ',int(2.9))

print('\nint(0b101) = ',int(0b101))
print("int('0b101',base=2) = ",int('0b101',base=2))

print('\nint(0xF) = ',int(0xF))
print("int('0xF',base=16) = ",int('0xF',base=16))

print("\nRule of thumb::::\n int('2') ok\n rest of them must come without string ok")
#print('float_str--->int',int('2.2'))#integer does not support float to be string

print("\nint() carry only 'int' string \nfloat() carry 'int' and 'float' string\nrest should come clean to int or float   ")

print('\n\nvalue update hidden reality\n')

my_total_friends=5

print('my_total_friends = ',my_total_friends,id(my_total_friends))
birthdays_to_attend=my_total_friends
print('birthdays_to_attend = ',birthdays_to_attend)
print('\n after ')
my_total_friends+=5
print('my_total_friends = ',my_total_friends ,id(my_total_friends))
print('birthdays_to_attend = ',birthdays_to_attend)
print("\n this += is not pure updating  it is new variable assigning \n")
print("up dating is that in which 'id' of variable does not change")
print('when ever u will use = sign u will be disconnecting your relationships and redefining new one')

print('\n======\nuse list.extend() to update purely and see it\'s id' )

print('\n====\nbuild-in functions')
print("list sum([1,2]) =",sum([1,2]))
print("sum(['1','2']) =",'error its  not concatination ')
print('tuple sum((1,2,3)) =',sum((1,2,3)))
print("sum([1,2] , [1,2]) =",'error TypeError can only concatenate list (not "int") to list')
print("sum([1,2],1) =",sum([1,2],1))
print("sum((1,2),1) =",sum((1,2),1.1))

print('sum(1,2,3)','type error got 3 args take only 2args')
"""

#print("\n\n thumb rule:::\n\bsum() take 2 ags ok\n \bsum list with integer\\float ok\n \bsum tuple with integer\\float ok")
"""import datetime
anniversary = datetime.date(1991, 10, 12)
name= 'Friin'
print(f"{anniversary:%A,%B %d,%Y}")
print(f"so you born in {anniversary:%C} century")
print(f"you\'re name is {name!r}")
print(int(0x04d2))
print(f"{'s'!r}")
print(f"{{anniversary:%A,%B %d,%Y}}")
x=123232.23442
print(f"{x:_^10,.2f}")
print(f"{65!a}")""" #string
#https://www.python.org/dev/peps/pep-0498/
"""x=[chr(x) for x in range(65,26+65)]
x=''.join(x)
print(x)

print(x[0:15],'ABCDEFGHIJKLMNO')
print(x[3::3],'DGJMPSVY',',every 4th one')
print(x[2:-3],"x[2:-3]")
print(x[10:-7],"x[10,-7]k-s")
print(repr(x[-7:10]),"x[-7:10] because direction of index moving is increasing but -7 > 10 there index form is 17>11 it is decreasing")
print(x[-7:10:-1],"x[-7:10,-1]")

print('\n===\nif u are moving left-->right your direction must be positive')
print('if u are moving left<--right your direction must be negative')
print('moving on string means--identify [starting :ending] and see your direction on string')
print(x[-4:12:-1],'go from -4 to 12 index then drop 12index')
print(x[-7:4:-1],'go from -7 to 4 and drop 4 index T-G')
print(x[4:-7],'go from 4 to -7 and drop -7 index E-S')
print(x[12:-4],'go to 12index and take all to -4index then drop -4index M-V')
print(x[17:7:-2],'rpnlj')""" #list
# print("""feevrer
#         \rregregr""")  #string \r carriage return
# print("""
#    \rrtbetebwertsetesbtsbt
#    \rrerwvevrwervwvrwrre
#    \rerwevrwervew \f sbtetebrt
#     """) # \f page breaker formfeed

"""print('fergr '  'vergeg') #more then one string

print ('a'.center(2,'#'))"""

"""for i in range(1,21,2):
    print(i)"""

"""import math
print(math.e,math.copysign(-1,2),math.modf(1.2),math.degrees(2*math.pi),math.fsum([1,2]))
""" #math module
"""print(1+2\

      +3)"""
# import math
# print(math.pow(2,3))

# print(int("2.0"))

# ls =          ['a','b','c','d']
# where_to_go = [1,   0,  4,  3]
#
# final   = ['b','a','d','c']
#
# def blind(e):
#
#      return where_to_go[ls.index(e)]
#
# print(sorted(ls,key=blind))