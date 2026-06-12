import numpy as np
# #create array 
# arr1d = np.array([1,2, 3, 4,5])
# arr2d = np.array([[85,90,78],[72,88,95],[91,76,83]])          #3students X 3subjects
# print(arr2d.shape)
# print(arr2d.dtype)


'''creating arrays differently'''
# import numpy as np

# zeros = np.zeros((3,4))
# # 3X44 array of 0s
# print(zeros)
# ones = np.ones((2,5))
# # 2X5 array of 1s
# print(ones)
# rng = np.arange(0,50,5)
# # [0,5,10,...,45]
# print(rng)
# lin = np.linspace(0,1,11)
# print(lin)

# random = np.random.randint(40,100,(5,3))
# print(random)


'''array operations'''
'''vectorized math - no loop needed'''
# arr = np.array([10,20,30,40,50])

# print(arr * 2)                 # [20 40 60 80 100]
# print(arr + 5)                 # [15 25 35 45 55]
# print(arr ** 2)                # [100 400 900 1600 2500]



'''statistics operations'''
# marks_2d = np.array([[85,90,78],[72,88,95],[91,76,83]])
# print(np.mean(marks_2d))               #overall mean
# print(np.mean(marks_2d, axis=1))        #mean per student (row) 
# print(np.mean(marks_2d,axis=0))          #mean per subject(column)
# print(np.max(marks_2d))                   #highest mark
# print(np.std(marks_2d))                    #standard deviation

# #boolean indexing(critical for data filtering)
# arr = np.array([55,82,43,91,67,78,35,88])
# print(arr[arr > 70])        #[82 91 78 88] - only values> 70





import pandas as pd

data = {
    'Name': ['Rahul','Priya','Amit','Sneha','Vikram'],
    'Age': [22, 21, 23, 20, 24],
    'Marks': [85, 92, 78, 88, 73],
    'City': ['Bhopal','Indore','Bhopal','Jabalpur','Indore']
}
df = pd.DataFrame(data)
print(df)
#explore the data
print(df.shape)                          #(5,4) - 5rows , 4columns
print(df.head(3))                       #first 3 rows
print(df.dtypes)                          #data type of each column
print(df.describe())                      #statistical summary
