# list1=[23,24,25,26]
# list2=[27,28,29,30]
# for i in list2:
# 	list1.attend(i)
# print(list1)


#  # 9rd
# list1=[2,3,4,5,2,6,3,2]
# list2=[]
# for i in list1:
# 	if i not in list2:
#  		list2.append(i)   


# myTuple=(10,20,30,40,50)
# i=56
# while i<0:
# 	print(myTuple[i])
# 	i-=1
# print()

# tuple1=(11,22,33,44,55,66)
# tuple2=()
# i=1
# while i<6:
# 	if tuple1[i]==22 or 55:
# 		tuple2=tuple1[i]
# 		print(tuple2)
# 	else:
# 		continue
# 	i+=1
	
# tuple1=(50,10,60,70,50)
# print(tuple1.count(50))

# myset={1,10,2,10}
# print(myset) 
#   

# i=1
# b=set()
# while i<11:
# 	k=input("entr_nunbr-")
# 	b.add(k)
# 	print(b)
# 	i+=1



# set1={1,2,3,4}
# set2={1,4,3,5}
# set3={1,7,3,5}
# result = set1.difference(result)
# result1 = set3.difference(result)
# print(result1)

# i=1
# user_num=random.randint(1,10)
# print(user_num)
# while False:
# 	input("enter_your_number-")
# 	if 


# my_tuple=(1,1,1,1)
# if my_tuple.count(my_tuple[3])==len(my_tuple):
# 	print("all items are the same")
# else:
# 	print("all items are not the same")
 
# t=(("33","33"),("1416","55"))
# t2=tuple((int(i),int(j)) for i,j in t)
# print(t2)


# my_list=[9,222,18,34,68,17,45]
# minimum=my_list[0]
# for i in my_list:
# 	if i<minimum:
# 		minimum=i
# 		# print(minimum)      
# print(minimum)
 
# dislist=['apple','banana','chery']
# print(dislist)

# dislist=['appple','banana','chery']
# print(len(dislist))


# dielist1=['apple','banana','chery']
# dislist2=[4,7,1]
# dislist3=[True,False,True]
# print(dielist1)
# print(dislist2)
# print(dislist3)

# list1=['suro',123,True,False,'asnm']
# print(list1)

# mylist=['apple','banana','chery']
# print(type(mylist))


# thislist=list(('apple','banan','chery'))
# print(thislist)


# thilist=['apple','banana','charry']
# print(thilist)

# list1=['abc',111,True,False,'male']
# print(type(list1))


# thislist=list(('apple','banana','cherry'))
# print(thislist)


# fruits=['apple','banana','cherry']
# fruits.append('banana')
# print(fruits)

# fruits=['apple','banana','orange']
# cars=['bmw','mersedes','opel']
# fruits.extend(cars)
# print(fruits)

# fruits=['apple','banana','cherry']
# x=fruits.index('cherry')
# print(x)


# fruitd=[55,777,44,4,77,88,77]
# k=fruitd.index(77)
# print(k)

# fruits=['apple','banana','cherry']
# fruits.insert(1,'orange')
# print(fruits)


# fruits=['apple','banana','orang']
# fruits.pop(0)
# print(fruits)

# fruits=['apple','banana','orang']
# fruits.remove('orang')
# print(fruits)

# fruits=[1,2,3,4,5,6,7,8,9]
# fruits.reverse()
# print(fruits)

# cars=['mersedes', 'bmw','oppel']
# cars.sort()
# print(cars)


# numbers=[1,2,3,5,6,7]
# print(numbers[-1])

# fruits=['apple','banana','cherry']
# fruits[2]='blaqkcruit'
# print(fruits)



# fruits=['apple','banana','cherry']
# del fruits
# print(fruits)


# thislist=['apple','banana','charry']
# for i in range(thislist):
# 	print(i)

# x=range(6)
# for i in x:
# 	print(i)


# x=range(3,6)
# for i in x:
# 	print(i)


# x=range(3,20,2)
# for i in x:
# 	print(i)

# thislis=['apple','banana', 'charry']
# for i in range(len(thislis)):
# 	print(thislis[i])


# thislist=['apple','banana','cherry']
# i=0
# while i<len(thislist):
# 	print(thislist[i])
# 	i+=1

# thislist=['apple','banana','chery']
# [print(x) for x in thislist]

# fruits=['apple','banana','cherrry']
# newlist=[]
# for x in fruits:
# 	if 'a' in x:
# 		newlist.append(x)
# 		print(newlist)

# fruits=['apple','banana','chery','mango']
# newlist=[x for x in fruits if 'a' in x]
# print(newlist)


# fruits=['apple','banana','cherry','mango']
# newlist=[x for x in fruits if x !='apple']
# print(newlist)


# fruits=['apple','banana','cherry','mango','kivi']
# newlist=[x for x in fruits]
# print(newlist)


# newlist=[x for x in range(10)]
# print(newlist)


# newlist=[x for x in range(10) if x<5]
# print(newlist)

# fruits=['apple','banana','orange','kivi','cherrry']
# newlist=[x.upper() for x in fruits]
# print(newlist)


# fruits=['apple','banana','cherry','orang','kivi']
# newlist=['hello' for x in fruits]
# print(newlist)

# fruits=['apple','banana','cherry','mango','kivi']
# nwelist=[x  if x != 'banana' else 'orange' for x in fruits]
# print(nwelist)


# thislist=['orang','mango','kivi','pinaple','banana']
# thislist.sort(reverse=True)
# print(thislist)


# thislist=[100,50,65,82,23]
# thislist.sort(reverse=True)
# print(thislist)
 
# thislist=['apple','banana','cherry','kivi','orang']
# thislist.sort(key=str.lower)
# print(thislist)

# list1=['a','b','c']
# list2=[1,2,3]
# list1.extend(list2)
# print(list1)


# thisdic={'brend':'ford',
# 'electrical':False, 
# 'color':['white','red','blue']}
# print(type(thisdic))


# thisdic=dict(name = 'jhon',age=36,country='norvey')
# print(thisdic)


# disdic={'brand':'ford','model':'mustang','year':1964}
# x=disdic.keys()
# print(x)

# i=1
# l=''
# while i<11:
# 	k=input('entr_world')
# 	print(k)
# 	i+=1
# 	for j in k:
# 		l=l+k
# 	print(l)
# 	if k==l:
# 		print('that is polidron')
# 	else:
# 		print('that is not polidron')


# lis1=[10,20,30,40,50,20,30,80,100]
# lis2=list()
# for i in lis1:
# 	if i not in lis2:
# 		lis2.append(i)
# print(lis2)

# username='username'
# pasvord='pasvord'
# username1=''
# pasvord1=''
# while True:
# 	username1=input('enter your username')
# 	pasvord1=input('enter your pasvord')
# 	if username==username1 and pasvord==pasvord1:
# 		print('pasvord is true')
# 		break
# 	else:
# 		print('pasvord is not true')
# 		continue


# list1=['p','q']
# lis2=list()
# i=1
# while i<6:
# 	lis2='p+str(i)','q+str(i)'
# 	i+=1
# 	print(lis2)


# Create a program that will play the “cows and bulls” game with the user. 
# The game works like this: Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
# For every digit that the user guessed correctly in the correct place, they have a “cow”. 
# For every digit the user guessed correctly in the wrong place is a “bull.” 
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
# Once the user guesses the correct number, the game is over. 
# Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

count_guess=0
while True:
	count_cow=0
	count_bull=0
	rand_numb=str(4571)
	print('random_nimber_is_',rand_numb)
	user_numb=input('enter_user_number_')
	print('user_nimber_is_',rand_numb)
	for i, j in zip(rand_numb, user_numb):
		print(i, j)
		if i==j:
			print('it_is_cowe')
			count_cow=count_cow+1
			print('count_cow=',count_cow)
		else:
			print('it_is_boll')
			count_bull=count_bull+1
			print('count_bull=',count_bull)
	print('you_have_cow',count_cow,'and_bull',count_bull)
	count_guess=count_guess+1
	print('count_guess_is',count_guess)
	if count_cow==4:
			break





