def Q5_11():
	student_num=int(input("Enter the number of students "))
	First_Scores=int(input("Enter Num1 student's score: "))
	Sencond_Scores=First_Scores
	for i in range(1,student_num):
	    scores=int(input("Enter Num"+str(i+1)+" student's score: "))
	    if(scores>First_Scores):
	        Sencond_Scores=First_Scores
	        First_Scores=scores
	    elif scores>Sencond_Scores:
	        Sencond_Scores=scores
	print("The highest score is ",First_Scores,"and second-highest score is ",Sencond_Scores)
def Q5_18():
	numberOfLine=int(input("Enter the number of line: "))
	for rows in range(1,numberOfLine+1):
		for s in range(numberOfLine-rows,0,-1):
			print("   ",end=" ")	
		for l in range(rows,0,-1):
			print(l," ",end=" ")
		for r in range(2,rows+1,1):
			print(r," ",end=" ")	
		print()
def Q5_25():
	N=50000
	sumRightToLeft=0.0;
	sumLeftToRight=0.0;
	for x in range(N,0,-1):
		sumRightToLeft+=1/x
	print("Computing for right to left is ",sumRightToLeft)
	for y in range(1,N+1,1):
		sumLeftToRight+=1/y
	print("Computing for left to right is ",sumLeftToRight)
	difference=sumRightToLeft-sumLeftToRight
	print("difference is",difference)
def Q5_27():
	sum=0.0
	for x in range(1,100000,1):
		n=(-1)**(x+1)/(2.0*x-1)
		sum+=n*4.0
		if x%10000==0:
			print("pi is ",sum)
def Q5_41():
	n=1
	max=0
	count=0
	while(n>=1):
		n=int(input("Enter a number (0: for end of input):"))
		if n>max:
			max=n
			count=1
		elif n==max:
			count+=1
	print("The largest number is",max)
	print("The occurrence count of the largest number is ",count)


Q5_11()
Q5_18()
Q5_25()
Q5_27()
Q5_41()
