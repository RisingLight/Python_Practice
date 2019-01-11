# Python_Practice

## Prerequisites:
1.	Handling Input and Output
2.	Looping constructs
3.	Arrays, Lists, Sets and Dictionaries
4.	Modules and Functions
5.	File Handling
6.	Exception Handling
7.	Library Installation  -- pip install <name of the library> eg. pip install numpy
---------------------------------------------------------------------------------------------------------------------------------------

## Python Programming: Cycle 1:

**1. From a given list, find the second highest value from the list.**   
**Input:**   [6, 5, 2, 1, 6, 4]  
**Output:**   5  


**2. From the string input, count the special characters, alphabets, digits, lowercase and uppercase characters.   
Input:**   Sathyabama 2019 @   
**Output:**
		Digits: 			        4  
		Alphabets: 		        10  
		Special Characters: 	1  
		Lowercase: 		        9  
		Uppercase: 		        1  

**3. Input String (s) and Width (w). Wrap the string into a paragraph of width w.   
Input:**  
s = Sathyabama  
w = 3  
**Output:**  
	Sat  
	hya  
	bam  
	a  
**4. Print of the String "Welcome". Matrix size must be N X M. ( N is an odd natural number, and  M is 3 times N.). The design should have 'WELCOME' written in the center. The design pattern should only use |, . and - characters.   
Input:**   N = 7, M = 21  
**Output:** 
``` ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------     
 ```  
**5. Consider a function f(X) = X3. Input is ‘N’ list. Each list contains ‘M’ elements. From the list, find the maximum element. Compute: S = (f(X1) + f(X2) + f(X3) + … + f(XN)) Modulo Z   
Input:**  
N = 3  
Z = 1000  
N1 = 2 5 1  
N2 = 1 2 4 6 9  
N3 = 10 9 11 4 5  
Procedure:  
maxn1 = 5  
maxn2 = 9    
maxn3 = 11  
S = ((maxn1)3 + (maxn2)3 + (maxn3)3) % Z  
**Output:**  
	185  

**6. Validate the Credit numbers based on the following conditions:  
	Begins with 4, 5, or 6  
	Contain exactly 16 digits  
	Contains only numbers ( 0 to 9 )  
	For every 4 digits a hyphen (-) may be included (not mandatory). No other special character permitted.  
	Must not have 4 or more consecutive same digits.     
Input & Output:**  
```
4253625879615786		    Valid
4424424424442444		    Valid
5122-2368-7954-3214		   Valid
42536258796157867       	Invalid
4424444424442444        	Invalid
5122-2368-7954 - 3214   	Invalid
44244x4424442444        	Invalid
0525362587961578        	Invalid
61234-567-8912-3456 	    Invalid  
```

**7. Read a CSV File. Print column wise output.  
	Input:**   filename.csv  
  ```
    Col1	Col2	Col3	Col4
    r1c1	r1c2	r1c3	r1c4
    r2c1	r2c2	r2c3	r2c4  
    r3c1	r3c2	r3c3	r3c4
 ```
   **Output:**  
```
Col1	r1c1	r2c1	r3c1
Col2	r1c2	r2c2	r3c2
Col3	r1c3	r2c3	r3c3
Col4	r1c4	r2c4	r3c4 
    
```


