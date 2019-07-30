# largestprimefactor
This python code calculates the largest factor of a number that is also a prime number. 
The code was inspired by an exercise from the website projecteuler.net. 
The idea behind this code is that any factor of a large number that is bigger that its square root will have to be multiplied by a number smaller than its square root. Leveraging this, the code calculates every pair of numbers that multiplied by each other result in the number being evaluated. Then a simple prime evaluation is run on those numbers to obtain the largest prime factor. 
It has been tested with numbers in the range of billions.
