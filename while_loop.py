# 1)Finding the sum of even numbers from 1 to 10 numbers using while loop.

# summ=0
# i=1
# while True:
# 	if i%2==0:
# 		summ=summ+i
# 		print("i=",i)
# 		print("summ=",summ)
# 	i+=1
# 	if i==11:
# 		break
# print("sum of even numbers=",summ)



# 2)Printing the square of  1 to 10 numbers using while loop.

# i=1
# square=1
# while True:
# 	square=i**2
# 	print("squaresquare=",square)
# 	i+=1
# 	if i==11:
# 		break


#  3)write a while loop programm, thats iterate through the string 
# and print all characters as soon as it encounters an empty string(" ").


# sents="America is stronger country in the world !"
# i=0
# count_empty=0
# counter=len(sents)
# print(counter)
# while True:
# 	if sents[i]==" ":
# 		print("empty=' '")
# 		count_empty=count_empty+1
# 		print("count_empty=",count_empty)
# 	i+=1
# 	if i==counter:
# 		break
	


# 4)Write a Python program that accepts a string and calculate the number of digits and letters.
# example : "Python 3.2"
# Expected Output : Letters 6, Digits 2
 

# sents="heppy new year 2022"
# count=len(sents)
# print("lengs_of_sents=",count)
# count_of_numb=0
# count_of_later=0
# count_of_prabell=0
# i=0
# while True:
# 	if sents[i].isdigit():
# 		count_of_numb=count_of_numb+1
# 		# print("count_of_numb=",count_of_numb)
# 	elif sents[i]==" ":
# 		count_of_prabell=count_of_prabell+1
# 		# print("count_of_prabell=",count_of_prabell)
# 	else:
# 		count_of_later=count_of_later+1
# 		# print("count_of_later=",count_of_later)
# 	i+=1
# 	if i==count:
# 			print("count_of_later=",count_of_later)
# 			print("count_of_numb=",count_of_numb)
# 			print("count_of_prabell=",count_of_prabell)		
# 			break



# 5)Write a program in Python to reverse a word.
# example : python
# Expected output:nohtyp

# word="argentina"
# word_revers=str()
# lengs=len(word)
# print("lengs_words=",lengs)
# i=lengs-1
# while True:
# 		print(word[i])
# 		word_revers=word_revers+word[i]
# 		print(word_revers)
# 		i-=1
# 		if i==-1:
# 			break



# 6)Calculate the sum of all numbers from 1 to a inputed number.

# summ=0
# i=0
# numb=int(input("enter_your_number="))
# while i<numb+1:
# 	summ=summ+i
# 	i+=1
# print("summ_of_numbers=",summ)



# 7)Write a program to use for loop to print the following reverse number pattern.
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1


# for i in range(0,6):
# 	for j in range(5-i,0,-1):
# 		print(j, end=" ")
# 	print()




# 8)Take a number from 1 to 10 and ask user to guess it. If user guess wrong
# number, the programm will continue.(use while loop)

# i=0
# numb=5
# while i<11:
# 	gusse_numb=int(input("gusse_numb="))
# 	if gusse_numb==numb:
# 		print("your_anser_is_true")
# 		break
# 	else:
# 		i+=1
# 		print("i=",i)
	

	