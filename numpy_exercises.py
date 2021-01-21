#!/usr/bin/env python
# coding: utf-8

# ### Use the following code for the questions below:
# 
# `a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])`

# In[2]:


import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# ### 1. How many negative numbers are there?

# In[6]:


negatives = a[a < 0]
negatives


# ### 2. How many positive numbers are there?

# In[8]:


positives = a[a > 0]
positives


# ### 3. How many even positive numbers are there?

# In[10]:


even_positives = positives[positives % 2 == 0]
even_positives


# ### 4. If you were to add 3 to each data point, how many positive numbers would there be?

# In[12]:


add_three = a + 3
positives = add_three[add_three > 0]
positives


# ### 5. If you squared each number, what would the new mean and standard deviation be?

# In[13]:


squared = a ** 2
squared.mean(), squared.std()


# ### 6. A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.

# In[17]:


centered = a - a.mean()
centered, centered.mean()


# In[18]:


z_scores = (a - a.mean()) / a.std()
z_scores


# ### 8. Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.

# In[25]:


import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
print(f"sum_of_a:  {sum_of_a}")

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
print(f"min_of_a:  {min_of_a}")

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
print(f"max_of_a:  {max_of_a}")

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum_of_a / len(a)
print(f"mean_of_a:  {mean_of_a}")

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = 1
for num in a:
    product_of_a *= num
    
print(f"product_of_a:  {product_of_a}")

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = []
for num in a:
    squares_of_a.append(num ** 2)
    
print(f"squares_of_a:  {squares_of_a}")

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = [num for num in a if num % 2 != 0]
print(f"odds_in_a:  {odds_in_a}")

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = [num for num in a if num % 2 == 0]
print(f"evens_in_a:  {evens_in_a}")


# In[50]:


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
b = np.array(b)
sum_of_b = b.sum()
print(f"sum_of_b:  {sum_of_b}")

# Exercise 2 - refactor the following to use numpy. 
min_of_b = b.min()
print(f"min_of_b:  {min_of_b}")

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = b.max()
print(f"max_of_b:  {max_of_b}")

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = b.mean()
print(f"mean_of_b:  {mean_of_b}")

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = np.prod(b)
print(f"product_of_b:  {product_of_b}")

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = b ** 2
print(f"squares_of_b:  {squares_of_b}")

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = b[b % 2 != 0]
print(f"odds_in_b:  {odds_in_b}")

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = b[b % 2 == 0]
print(f"evens_in_b: {evens_in_b}")

# Exercise 9 - print out the shape of the array b.
print(f"shape of b:  {b.shape}")

# Exercise 10 - transpose the array b.
print(f"b transposed:  {np.transpose(b)}")

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
print(f"b reshaped 1x6:  {np.reshape(b, (1, 6))}")

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
print(f"b reshaped 6x1:  {np.reshape(b, (6, 1))}")


# In[64]:


## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
c = np.array(c)

# Exercise 1 - Find the min, max, sum, and product of c.
print(c.min(), c.max(), c.sum(), np.prod(c))

# Exercise 2 - Determine the standard deviation of c.
print(c.std())

# Exercise 3 - Determine the variance of c.
print(np.var(c))

# Exercise 4 - Print out the shape of the array c
print(c.shape)

# Exercise 5 - Transpose c and print out transposed result.
transposed_c = np.transpose(c)
print(transposed_c)

# Exercise 6 - Get the dot product of the array c with c. 
print(np.dot(c, c))

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
print(np.array(c * transposed_c).sum())

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
print(np.prod(np.array(c * transposed_c)))


# In[81]:


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

d = np.array(d)
# Exercise 1 - Find the sine of all the numbers in d
print(np.sin(d))

# Exercise 2 - Find the cosine of all the numbers in d
print(np.cos(d))

# Exercise 3 - Find the tangent of all the numbers in d
print(np.tan(d))

# Exercise 4 - Find all the negative numbers in d
print(d[d < 0])

# Exercise 5 - Find all the positive numbers in d
print(d[d > 0])

# Exercise 6 - Return an array of only the unique numbers in d.
print(np.unique(d))

# Exercise 7 - Determine how many unique numbers there are in d.
print(len(np.unique(d)))

# Exercise 8 - Print out the shape of d.
print(d.shape)

# Exercise 9 - Transpose and then print out the shape of d.
transpose_d = np.transpose(d)
print(transpose_d.shape)

# Exercise 10 - Reshape d into an array of 9 x 2
np.reshape(d, (9, 2))


# In[ ]:




