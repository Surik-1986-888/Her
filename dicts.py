# 1)Write a Python program to match key values in two dictionaries.
# Sample dictionary:dict_1= {'key1': 1, 'key2': 3, 'key3': 2},dict2 = {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both dict_1 and dict_2


# dict_1= {'key1': 1, 'key2': 3, 'key3': 2}
# dict_2 = {'key1': 1, 'key2': 2}
# for i in dict_1:
# 	for j in dict_2:
# 		if i==j and dict_1[i]==dict_2[j]:
# 			print(i,':',dict_1[i],'is present in both dict_1 and dict_2')



# 2) Write a Python program to drop empty Items from a given Dictionary.
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}


# dic1={'c1': 'Red', 'c2': 'Green', 'c3': None}
# dic2=dict()
# for i in dic1:
# 	if dic1[i] != None:
# 		dic2.update({i: dic1[i]})
# print(dic2)


# 3)A Python Dictionary contains List as value. Write a Python program to update the list values in the said dictionary.
# Original Dictionary:
# {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
# Update the list values of the said dictionary:
# {'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]} 

# dic1={'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
# dic1['Math']=[89, 90, 91]
# dic1['Physics']=[90,92,87]
# print(dic1)


# 4)Get a dictionary from 2 lists.

# list1=['brand','model','color','year']
# list2=['mersedes','W222','black',2021]
# dicsh=dict()
# for i in list1:
# 	dicsh.update({i:None })  
# print(dicsh)
# for j in list2:
# 	# dicsh[i]=[j]
#     print(j)

# d=dict(zip([1,2],[3,4]))
# ptint(d)
 


# 5) Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# n=10
# i=1
# dicsh=dict()
# while i<10:
# 	dicsh.update({i:i*i})  
# 	i+=1
# print(dicsh)
 

#  6)Write a Python program to get the top three items in a shop.
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3


dic1={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
dic2=dict()
lis=list()
for i in dic1:
	lis.append(dic1[i])
	lis.sort(reverse=True)
    print(lis)
j=0
while j<3:
	print(lis[j])
	j+=1
	for k in dic1:
		print(dic1[k])
		if lis[j]==dic1[k]:
			print(k,dic1[k])

