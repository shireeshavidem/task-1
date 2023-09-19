# Conditional statements
# 1. program for if statement
a = 10  
b = 20  
if a<b:  
  print("a is less than b")

# 2.program for if else statement
letter = "A"

if letter == "B":
 print("letter is B")

else:
    if letter == "C":
        print("letter is C")
   
    else:
      if letter == "A":
	        print("letter is A")
      else:

            print("letter isn't A, B and C")
          
	
	
 

# 3.program for elif statement
num = 10
if (num == 0):
     print("Number is Zero")
 
elif (num > 5):
       print("Number is greater than 5")
 
else:
       print("Number is smaller than 5")
             

# 4.program for Nested if statement
num = 10

if num > 5:
 print("Bigger than 5")

if num <= 15:
 print("Between 5 and 15")

# 5.program for if elif statement

letter = "A"

if letter == "B":
	print("letter is B")

elif letter == "C":
	print("letter is C")

elif letter == "A":
	print("letter is A")

else:
	print("letter isn't A, B or C")
     
     
#Iterative statements

# 1.program for While loop
x = 0
while (x < 5):
   print(x)
   x = x + 1


# 2.program for While loop with else 
x = 1
while (x < 5):
   print('inside while loop value of x is ',x)
   x = x + 1
else:
   print('inside else value of x is ', x) 

# 3.program for For loop   
for letter in"python":
 print("The current letter:", letter)

# 4.program for Nested loop
rows = 5
# outer loop
for i in range(1, rows + 1):
    # inner loop
    for j in range(1, i + 1):
        print("*", end=" ")
    print('')

# 5.program for Nested for loop

for i in range(2, 4):

	# Printing inside the outer loop
	# Running inner loop from 1 to 10
	for j in range(1, 11):

		# Printing inside the inner loop
		print(i, "*", j, "=", i*j)
	# Printing inside the outer loop
	print()

#Unconditional loops
# Break statement
for letter in"python":
     if letter=='h':
          
           break
     print(letter)
print("bye")

# Continue statement
for var in "shireesha":
	if var == "e":
		continue
	print(var)
     
# pass statement

s = "shireesha"

# Empty loop
for i in s:
	# No error will be raised
	pass

# Empty function
def fun():
	pass

# No error will be raised
fun()

# Pass statement
for i in s:
	if i == 'h':
		print('Pass executed')
		pass
	print(i)




