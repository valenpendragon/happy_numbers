
# coding: utf-8

# s_it = iter('hello') # sufficient to make in iterator

# In[1]:

from __future__ import print_function

def test_sum(num):
    '''
    This function takes a string composed of integers, converts them
    individually into integers, squares these numbers, and sums up the squares.
    This function assumes that num represents a base10 integer.
    INPUT: num: a string composed of integers between 0 and 9
    OUTPU: integer sum of the numerals in num
    '''
    s = iter(num)  # Converts the string num into a generator
    return sum(int(char) ** 2 for char in s)


# In[2]:

# Initialize the counters and sets we need for this process.
happy_ctr = 150        # This is the total number of happy numbers to find.
test_num = 1           # This counter is produces the actual numbers to be
                       # tested, starting with 1.
max_iter = 50          # This controls how many times to call test_sum before
                       # concluding the number is not happy.
happy_nums = set()     # Empty set to store the happy numbers found
sad_nums = set()       # Empty set to store sad numbers to make the checking
                       # process more efficient.
# Additional variables that do not need to be initialized:
#   num_sum: stores the test_sum result from the most recent test so that
#            it can be looped back if it is not equal to one.
#   iter_ctr: tracks number of times test_sum has been called on the current
#            number being tested.

# This loop tracks the numbers tested. It will sort them into happy and sad
# as it goes through them. It will end when the set of happy_nums exceeds the
# number of happy numbers to be found.
while happy_ctr > len(happy_nums):
    
    # This loop actually runs the testing process on the current number,
    # test_num. We cannot expect the first pass for a fairly large integer
    # to produce a value of 1 on the first few passes. For sad numbers, it
    # will never converge on zero. We have to set the iteration counter, 
    # iter_ctr to zero before each number is tested. We also run our first
    # check of test_num with test_sum ahead of the loop.
    iter_ctr = 0
    num_sum = test_sum(str(test_num))    
    while iter_ctr < max_iter:
        
        # First, we need to check if the last test_sum equals 1. If so, we
        # have a happy number, print a message about it, and it to the set of 
        # happy numbers. Then, we skip to the next number by breaking out
        # of this loop.
        if num_sum == 1:
            #print("The following number is a 'happy number': ", test_num)
            happy_nums.add(test_num)
            test_num += 1
            break
        
        # At this point, test_num has yet to produce a 1 from test_sum on
        # the current pass. We have not yet exceeded the number of iterations
        # before considering it to be sad either. So, first we need to see if
        # num_sum from the current pass is matches known happy numbers. If so,
        # we can print a message, add it to the set, increment the counter,
        # break out of the loop.
        if num_sum in happy_nums:
            #print("The following number is a 'happy number': ", test_num)
            happy_nums.add(test_num)
            test_num += 1
            break

        # Next, we need to see num_sum matches a number in the sad_nums set.
        # If so, test_num must be a sad number as well. We can print a message
        # to that effect, add the number to the sad_nums, increment test_num.
        # and break out of the loop.
        if num_sum in sad_nums:
            #print("The following number is a 'sad number': ", test_num)
            sad_nums.add(test_num)
            test_num += 1
            break

        # At this point, the num_sum is not 1, but it is also not recognized
        # as either sad or happy yet. So, we need to run a new test_sum on the
        # result from the last run, num_sum. We will also increment iter_ctr
        # and continue.
        num_sum = test_sum(str(num_sum))
        iter_ctr += 1
        continue
    
    # Now, we have to deal with the moment that iterations have exceeded the 
    # maximum iteration limit. The else statement below handles that
    # possibility. It is connected to the iter_ctr while loop, not the while
    # loop that checks to see if we have found enough happy numbers.
    # Exceediing the max iterations makes it highly likely that this number
    # is a sad number, since larger numbers resolve to smaller ones that have
    # already been categorized normally.
    else:
        #print("${0} is a sad number because it did not resolve to happy or sad after ${1} iterations.".format(test_num, max_iter))
        sad_nums.add(test_num)
        test_num += 1

# Now that all of the numbers have been processed, we can print the results.
# First, we need to order the sets.
ord_happy_nums = sorted(happy_nums)
ord_sad_nums = sorted(sad_nums)
print("The set of happy numbers is:")
print(ord_happy_nums)
print("The set of sad numbers appears to be:")
print(sad_nums)

