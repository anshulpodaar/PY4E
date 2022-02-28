####################################################################################################################
#   In this assignment you will read through and parse a file with text and numbers. 
#   You will extract all the numbers in the file and compute the sum of the numbers.
#      Data Files:
#        We provide two files for this assignment. One is a sample file where we give you the sum for your testing 
#        and the other is the actual data you need to process for the assignment.

#   Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
#   Actual data: http://py4e-data.dr-chuck.net/regex_sum_37412.txt (There are 71 values and the sum ends with 830)

###############################################
##### Created by: Anshul Podaar, 08-May-2018
####################################################################################################################
fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print('File name invalid.')
    quit()

import re
sum_nums = 0
for line in fh:
    nums = re.findall('[0-9]+', line.strip())
    print(nums)
    for num in nums:
       sum_nums = sum_nums + int(num)
print('Final sum = ', sum_nums)

### import re
### print(sum([line in fh('[0-9]+',fh.read())]))


### import re
### print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )



####################
#   Optional: Just for Fun
#   There are a number of different ways to approach this problem. While we don't recommend trying to write the most compact code possible, it can sometimes be a fun exercise. Here is a a redacted version of two-line version of this program using list comprehension:

#   Python 2
#   import re
#   print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )

#   Python 3:
#   import re
#   print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
#   Please don't waste a lot of time trying to figure out the shortest solution until you have completed the homework. List comprehension is mentioned in Chapter 10 and the read() method is covered in Chapter 7.
####################