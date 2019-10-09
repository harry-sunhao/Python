'''
Suppose that the tuition for a uni- versity is $10,000 this year and increases 5% every year. Write a program that computes the tuition in ten years and the total cost of four years’ worth of tuition starting ten years from now.
'''
tuition = 10000.0
yearlyIncreasePercentage = 0.05
tuitionInTenYears = 0.0
fourYearsOfTuition = 0.0
for i in range(14):
    tuition += tuition * yearlyIncreasePercentage; 
    if (i == 9):
        tuitionInTenYears = tuition
    if (i == 10 or i == 11 or i == 12 or i == 13):
        fourYearsOfTuition += tuition
print("Tuition cost after 10 years is: ",tuitionInTenYears,"Four years of tuition after 10 years is: ",fourYearsOfTuition)
'''
Write a program that prompts the user to enter the number of students and each student’s score, and displays the highest and second- highest scores.
'''
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
'''
Use a while loop to find the largest integernsuchthatn3 islessthan12,000.
'''
limit = 12000
n = 1
while n*n*n < limit:
    n += 1
print(n-1)
print()
'''
**5.18 (Find the factors of an integer) Write a program that reads an integer and displays all its smallest factors, also known as prime factors. For example, if the input inte- ger is 120, the output should be as follows:
2, 2, 2, 3, 5
'''
# Prompt the user to enter a positive integer
number = int(input("Enter a positive integer: "))
    
# Find all the smallest factors of the integer
print("The factors for", number, "is", end = " ")
factor = 2
while factor <= number:
    if number % factor == 0:
        number = number / factor
        print(factor, end = "  ")
    else:
        factor += 1
'''
20 A
'''
print()
for i in range(1, 6 + 1):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()
print()
#20B
for i in range(1, 6 + 1):
    for j in range(1, 7 - i + 1):
        print(j, end = " ")
    print()
#20C
print()
for i in range(1, 6 + 1):
    # Print leading space
    for j in range(6 - i, 0, -1):
        print("  ", end = "")
      
    for j in range(i, 0, -1):
        print(j, end = " ")

    print()
#20D
print()
for i in range(1, 6 + 1):
    # Print leading space
    for j in range(i, 1, -1):
        print("  ", end = "")
      
    for j in range(1, 6 + 1 - i + 1):
        print(j, end = " ")
    
    print()
