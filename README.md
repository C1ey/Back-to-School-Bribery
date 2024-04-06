# Back-to-School-Bribery
Write a program to count the number of ways that a teacher could purchase two chocolates and ensure that all her students would get the same number of pieces, if they all came to school every day.


A teacher anticipates that after the initial excitement of resuming face to face classes,
 her students will soon start wishing to stay home from school again. 
 So, she decides to buy some chocolate treats, which she will hand out to each of her k students,
  each day that they come to school, in order to incentivise them. 
  She looks online for novelty packages of chocolate and is happy to find that there are n options,
  but the amount available for each option is exactly 1. Thankfully, she finds that with her budget, she can buy any two of the options that she has found. The number of pieces of chocolate vary from package to package. Mindful that no child should appear to be more or less favoured, 
  she wants to ensure that the total number of pieces in her purchase is a perfect multiple of k.


Given a list of the number of pieces in each package on offer: p1, ..., p_n, 
write a program to count the number of ways that the teacher could purchase two of them and ensure that all her students would get the same number of pieces,
if they all came to school every day.


Input Format

Line 1: k n
The next n lines each contain a single integer p_i

Constraints

2<=n<=10^6
1<=p_i<=10^9
1<=k<=10^5

Output Format

A single integer indicating the number of compatible pairs among the n given options.

Sample Input 0

10 7
15
7
15
19
81
23
41
Sample Output 0

4
Explanation 0

The table below illustrates the total number of pieces the teacher would obtain if she were to purchase the corresponding options in the given list. 
(The order of the values being added is irrelevant, 
so we show only the upper triangular part of the table).


n_i+n_j 15	7	15	19	81	23	41
15		    22	30	34	96	38	56
7			    22	26	88	30	48
15				    34	96	38	56
19					    100	42	60
81						    104	122
23							    64

Examining the total number of pieces for each possible pair, we see that only 4 of them (highlighted) are divisible by the number of students, 10, namely (15, 15), (7, 23), (19, 81), (19, 41), so we return 4 as our answer.

Sample Input 1

5 20
75
95
3
38
99
45
28
17
46
5
34
79
44
50
58
22
7
85
62
45


Sample Output 1

41