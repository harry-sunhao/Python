# Week1
- To understand the **respective roles** of **hardware** and
  **software** in a computing system.
- To understand **the basic design** of a modern computer.
- To understand the respective roles of **Compiler** and
  **Interpreter**.
    - Compilers convert programs written in a high-level language into the machine language of some computer

    | interpreter  |  compiler  |
    |---|---|
    |Translates program one statement at a time. 每次翻译一个语句|  Scans the entire program and translates it as a whole into machine code.扫描整个程序并将其作为一个整体转换为机器代码 |
    |It takes less amount of time to analyze the source code but the overall execution time is slower.分析源代码所需的时间较少，但总体执行时间较慢 | It takes large amount of time to analyze the source code but the overall execution time is comparatively faster.分析源代码需要大量的时间，但总体执行时间相对较快
    |  No intermediate object code is generated, hence are memory efficient.没有生成中间对象代码，因此具有内存效率  | 	Generates intermediate object code which further requires linking, hence requires more memory.生成需要进一步链接的中间对象代码，因此需要更多的内存  |
    |  Continues translating the program until the first error is met, in which case it stops. Hence debugging is easy.继续翻译程序，直到遇到第一个错误为止，在这种情况下，程序将停止。 因此调试是很容易的| It generates the error message only after scanning the whole program. Hence debugging is comparatively hard.它只有在扫描整个程序之后才会产生错误信息，因此调试比较困难 |  
    
# Week2

- Variables
    - Python KeyWord
        1. and
        2. as
        3. assert
        4. ... 
     - Wrong case
        - 7Eleven = "Chain of convenience stores" 
        - more$ = 1000000 
        - "CPSC 111"
     - Type converter+
- expression
    - An expression is a combination of values, variables, operators, and calls to functions
- statements
- operation
    - \+ \- \* \/ 
    - **important**
        - // Floor Division
            - 5/2=2 
        - & Modulus
            - 5%2=1
        - \*\* Exponent
            - 2\*\*3=8
- data type
    - str represent any sequence of characters
    - char only represent **one** characters
    - str can use '+' 
        - "ab"+"cd"="abcd"
    - only same data type can use operation
        - When we use operation for example '+' Python convert int to float to execution
        
# Week3
- Pseudo-code
    - Pseudo-code is an outline of a program written in a way that it can be easily converted into a computer programming language.
- if statement
    ````python
    condition1=True
    condition2=True
    if condition1: #<--- check a condition don't forget ':'
        condition1=False #if condition is True, jump to this statement
    elif condition2: #if condition1 is False check this condition2 
        condition2=False
    else: # condition 1 and 2 are false then pass this block
        condition1,condition2=False
        
    ````
# Week4&5
- 2's complement
- ASCII code
    - 0 48
    - A 65
    - a 98
# Week6
- str
    ````PYTHON
    message="Hello, World!"
     #H e l l o ,   W o r l  d  !
     #0 1 2 3 4 5 6 7 8 9 10 11 12
     # flap: len-1-len
     
    #message[0]='H'
    #message[-13]='H'
    #Notice
    #message[-2:5] is empty
    # We can not modify the exist string,so message[0]='a' is wrong
    ````
