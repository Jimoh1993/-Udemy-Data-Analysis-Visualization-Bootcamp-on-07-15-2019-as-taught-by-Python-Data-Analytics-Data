"""Section 1 & 2 lectures

This script comprise documentation of section 1 & 2 lectures
covered in udemy, each program is started with multi-line
docstrings signify the beginning of a program code example.

`numpy`, pandas has to be installed within the Python environment
they are require.

numpy or pandas must also be imported as modules for array manipulation.

NOTE:
    import keyword signify you are calling package to use on program script
    from keyword signify you are calling a built-ins function from a package
    print keyword signify you want to display information on console or on screen
"""

"""The documentation outline on numpy

Working with numpy package.
Scalar operations on array.
Indexing numpy arrays.
Universal array functions.
Saving and loading array.
Statistical & mathematical processing of arrays.
Conditional clauses & boolean operation on arrays.

"""

""""Working with numpy

Numpy provides:
An array object of arbitrary homogeneous items (i.e same datatype)
Fast mathematical operations over arrays
Linear Algebra, Random Number Generation etc.
"""
import numpy as np #imported numpy package
my_list1 = [1, 2, 3, 4] #initialize my_list1
my_list2 = [5, 6, 7, 8] #initialize my_list2
my_array = np.array([my_list1, my_list2]) #numpy array combination
print(my_array) #ouput my_array on console
print(my_array.shape) #print dimension of my array
print(my_array.dtype) #print datatype my_array
my_array1 = np.zeros(5) #initialize my_array1 to zeros elements
my_array1 = np.ones([5, 5]) #initialize my array2 elements to 1's
my_array1 = np.empty(5) #intitilize my_array3 to empty array
my_array1 = np.eye(5) #initialize my_array4 to identity elements
my_array1 = np.arange(5, 51, 3) #initialize my_array4 to interval value of 3 between 5 - 51
print(my_array1) #print elements of my_array4


"""Scalar operations on array

Array is a collection of data of the same type.
"""
from __future__ import division #import division module
import numpy as np #Numpy imported
print 5/2
array1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]]) #array1 initialization with 9 data
print(array1) #print array1

array2 = array1 * array1 #array1 multiplication by itself to generate array2
print(array2) #print array2

array3 = array1 ** 3 #array3 exponential multiplication by 3
print(array3) #print array3

array4 = array1 - array1 #array1 subtraction from itself to generate array4
print(array4) #output array4

array5 = array2 - array1 #array1 subtracted from array2 to generate array5
print(array5) #output array5

array4 = array1 - array1 #array1 subtracted from itself to generate array4
print(1/array1) #print reciprocal of array1


"""Indexing numpy arrays."""
import numpy as np #numpy imported
arr = np.arange(0, 12) #intialize arr to 0-12 integer value
print arr #output arr
print arr[0:6] #print arr data within 0-7
arr[0:5] = 20 #asigned 20 to index of 0-5
print arr #output arr
arr2 = arr[0:6] #asign data within index 0-6 to arr2
print arr2 #output arr2
arr2[:] = 29 #all element are of index 0-6 are replace by 29
print arr2 #output arr2
print arr #output arr
arrcopy = arr.copy() #creating new array with copy function
print arrcopy #output arrcopy


"""Universal array functions."""
import numpy as np #import numpy
A = np.arange(15) #nitialize array A with 15 elements
print A #print out array A
A = np.arange(1, 15, 2) #overwrite array A with elements of 2 interval
print "A is " #string
print A  #print out array A

B = np.sqrt(A) #find square root of array A
print "B is "
print B #print B

C = np.exp(A) #initialize C with elements of array A
print "C is "
print C #print out C

D = np.add(A, B) #sum of array A & B
print "D is " #string
print D #print out D

E = np.maximum(A, B) #find maximum element in A & B
print "E is " #string
print E #print out E


"""Saving and loading array."""
import numpy as np #import numpy
arr = np.arange(10) #initialize arr with 10 elements
print arr #print out arr

np.save('save_array', arr) #save array in memory with np.save function
new_array = np.load('save_array.npy') #new file is created save_array.npy
print new_array #print out new_array


array_1 = np.arange(25) #initialize array_1
array_2 = np.arange(30) #initialize array_2
np.savez('saved_archive.npz', x=array_1, y=array_2) #save multiple arrays
load_archive = np.load('saved_archive.npz') #load array out of memory
print load_archive['x'] #print array_1 by reference
print load_archive['y'] #print array_2 by reference

np.savetxt('notepadfile.txt', array_1, delimiter=',') #savetext file
load_txt_file = np.loadtxt('notepadfile.txt',  delimiter=',') #loading of txt file
print 'load_txt_file is' #string
print load_txt_file #print out text file


"""Statistical & mathematical processing of arrays."""
import numpy as np #import numpy
import matplotlib.pyplot as plt #import matplotlib for graph plotting
axes_values = np.arange(-100, 100, 10) #initialize axes_values
dx, dy = np.meshgrid(axes_values, axes_values) #set coordinate as dx, dy
function1 = 2*dx+3*dy #linear function
function2 = np.cos(dx)+np.cos(dy)#cos function

print function1 #print function1
plt.imshow(function1) #image show function
plt.title('function1 of plot 2*dx+3*dy') #graph title
plt.colorbar() #graph color bar
plt.savefig('myfig.png') #save image with .png format

print function2 #print fucntion2
plt.imshow(function2) #image show function
plt.title('function2 cos plot ') #graph title
plt.colorbar() #graph color bar
plt.savefig('myfig2.png') #save image


"""Conditional clauses & boolean operation on arrays."""
import numpy as np #import numpy
x = np.array([100, 400, 500, 600]) #initialize array x
y = np.array([10, 15, 20, 25]) #initialize array y
condition = np.array([True, True, False, False]) #condition clause

z = [a if cond else b for a, cond, b in zip(x, condition, y)] #loop use indirectly to perform this
print z #print out z

z2 = np.where(condition, x, y) #return boolean value Yes or No
print z2 #print z2

z3 = np.where(x > 0, 0, 1) #modify aarray z3
print z3
print x.sum() #summation of x
n = np.array([[1, 2], [3, 4]]) #initialize n with 2D array
print n.sum(0)#column sum
print x.mean() #find mean of x
print x.std() #find standard deviation of x
print x.var() #find variance of x

condition2 = np.array([True, False, True]) #logical operator
print condition2.any()  #or operator
print condition2.all()  #and operator

unsorted_array = np.array([1, 2, 8, 10, 7, 3]) #initialize unsorted numpy array
unsorted_array.sort() #sort array
print unsorted_array #print sorted array

arr2 = np.array(['solid', 'solid', 'liquid', 'liquid', 'gas', 'gas']) #initialize array with strings elements
print np.unique(arr2) #print unique array element

print np.in1d(['solid', 'gas', 'plasma'], arr2) #print array in 1 dimension



"""Pandas  package for data manipulation and analysis

Data collection structures in pandas are series and dataframe.
"""

"""The documentation outline on pandas

Object creation (Series, & Dataframe).
Indexing. and Reindexing object.
Dropping entries from data types.
Handling Null data in pandas.
Selecting and modifying data in pandas.
Coordinate and regulate data.
Ranking and sorting characteristics.
Statistics and graph sketches with pandas.
"""

"""Object creation with Series"""

from pandas import Series #import series from pandas package
import numpy as np #import numpy

object = Series([5, 10, 15, 20]) #series object creation by passing a list
print object
print object.value
print object.index

data_array = np.array(['a', 'b', 'c']) #numpy_arrays
s = Series(data_array) #use numpy_arrays to create series
print s


s = Series(data_array, index=[100, 101, 102]) #asign series to s variable
print s
s = Series(data_array, index=['index1', 'index2', 'index3']) #custom index
print s


"""Object creation with Dataframe"""
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

revenue_df = pd.read_clipboard() #dataframe object creation from web page
print revenue_df

print revenue_df.columns #print columnns of dataframe
print revenue_df['Rank'] #print Rank column of dataframe
print DataFrame(revenue_df, columns=['Rank', 'Name', 'Industry'])#print multiple columns of dataframe

print revenue_df.head(2) #print first 2 data in datframe
print revenue_df.tail(2) #print last 2 data in dataframe

array1 = np.array([1, 2, 3, 4, 5, 6]) #numpy array
revenue_df['Profit'] = array1 #assign values to dataframe
print revenue_df


"""Indexing object."""
from pandas import Series
series1 = Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd']) #initialize series1
print series1

index1 = series1.index #print series by index
print index1

print index1[2:] #slicing out index data


"""Reindexing object"""
from pandas import Series, DataFrame
from numpy.random import randn
series1 = Series([1, 2, 3, 4], index=['e', 'f', 'g', 'h']) #Create new series series1
print "Series1 output"
print series1

series2 = series1.reindex(['e', 'f', 'g', 'h', 'i']) #creating new indexes using reindex
print "Series2 Output"
print series2

series2 = series2.reindex(['e', 'f', 'g', 'h', 'i', 'j'], fill_value=10) #using fillvalue function
print "Series2 after reindexing"
print series2

cars = Series(['Audi', 'Merc','BMW'], index=[0, 4, 8]) #using reindex method => ffill
print "Cars series output"
print cars

df_1 = DataFrame(randn(25).reshape(5, 5), index=['a', 'b', 'c', 'd', 'e'], columns=['c1', 'c2', 'c3', 'c4', 'c5']) #create new dataframe using randn
print "create dataframe using randn"
print df_1

df_3 = df_2.reindex(columns=['c1', 'c2', 'c3', 'c4', 'c5', 'c6']) #reindex columns of dataframe
print "reindex column of dataframe"
print df_3

df_4 = df_1.ix[['a', 'b', 'c', 'd', 'e', 'f'], ['c1', 'c2', 'c3', 'c4', 'c5', 'c6']] #using .ix[] to reindex
print df_4


""""Dropping entries from data types."""
import numpy as np
from pandas import Series, DataFrame #import  series & dataframe
cars = Series(['BMW', 'Audi', 'Merc'], ['a', 'b', 'c']) #series as cars
print cars
cars = cars.drop('a') #remove BMW with a index
print cars

cars_df = DataFrame(np.arange(9).reshape(3, 3), index=['BMW', 'Audi', 'Merc'], columns=['rev', 'pro', 'exp']) #Datataframe
print cars_df
cars_df = cars_df.drop('BMW', axis=0)  #remove BMW from dataframe
print cars_df
cars_df = cars_df.drop('pro', axis=1) #remove pro column
print cars_df


"""Handling Null data in pandas."""
import  numpy as np
from pandas import Series, DataFrame
series1 = Series(['A', 'B', 'C', np.nan])

print series1.isnull() #validate series1
print series1.dropna() #remove nan value from series

df1 = DataFrame([[1, 2, 3], [5, 6, np.nan], [7, np.nan, 10], [np.nan, np.nan, np.nan]]) #initialize df1 dataframe
print df1
print df1.dropna() #remove nan value from dataframe


"""Selecting and modifying data in pandas."""
import numpy as np
from pandas import Series, DataFrame
series1 = Series([500, 600, 700], index=['A', 'B', 'C']) #initialize series1
print series1

print series1['A'] #print out 500 by index A
print series1['B'] #print out 600 by index B
print series1[['A', 'B']] #print out 500 & 600 by index A & B

df1 = DataFrame(np.arange(9).reshape(3,3), index=['car', 'bike', 'cycle'], columns=['A', 'B', 'C']) #initialize df1
print df1
print df1['A'] #print out column data in A
print df1[['A', 'B']] #print out column data in A & B


"""Coordinate and regulate data."""
import numpy as np
from pandas import Series, DataFrame
ser_a = Series([100, 200, 300], index=['a', 'b', 'c']) #initialize ser_a
ser_b = Series([300, 400, 500, 600], index=['a', 'b', 'c', 'd']) #initialize ser_b
print ser_a+ser_b #print summation of series

df1 = DataFrame(np.arange(4).reshape(2, 2), columns=['a', 'b'], index=['car', 'bike']) #initialize dataframe
print df1
df2 = DataFrame(np.arange(9).reshape(3, 3), columns=['a', 'b', 'c'], index=['car', 'bike', 'cycle']) #initialize dataframe
print df2
print df1+df2 #print summation of dataframe df1 + df2

df1 = df1.add(df2, fill_value=0) #sum df1 with add() method
print df1


"""Ranking and sorting characteristics."""
from pandas import Series, DataFrame
from numpy.random import randn
ser1 = Series([500, 1000, 1500], index=['a', 'b', 'c']) #initialize series
print ser1

print ser1.sort_index() #sorting by index
print ser1.sort_values() #sort by values
print ser1.rank() #ranking of series ser1

ser2 = Series(randn(10)) #initialize series with randn numpy
ser3 = ser2 #aliasing technique
print ser2

print "sort by values and Rank"
ser2 = ser2.sort_values()
print ser2.rank()

print "sort by index and Rank "
ser3 = ser3.sort_index()
print ser3.rank()


""""Statistics and graph sketches with pandas."""
from pandas import Series, DataFrame
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt #import matplotlib for graph plotting
array1 = np.array([[10, np.nan, 20], [30, 40, np.nan]]) #initialize array1
print array1
df1 = DataFrame(array1, index=[1, 2], columns=list('ABC')) #initialize df1
print df1

df2 = DataFrame(randn(9).reshape(3, 3), index=[1, 2, 3], columns=list('ABC')) #initialize df2
print df2

plt.plot(df2)n #plot df2
plt.legend(df2.columns, loc="lower right") #apply legend
plt.savefig('samplepic.png') #save plotted graph with .png format
plt.show() #display plotted graph