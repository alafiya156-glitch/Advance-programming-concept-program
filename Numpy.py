# Question 1: Create a 1D array of 10 integers and display its properties
import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("Array:", arr)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
print("Number of Dimensions:", arr.ndim)

# Question 2: Perform arithmetic operations on two NumPy arrays
import numpy as np
a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])
print("Array A:", a)
print("Array B:", b)
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

# Question 3: Find maximum, minimum, sum, and average
import numpy as np
arr = np.array([12, 25, 34, 45, 56, 67, 78, 89, 90, 100])
print("Array:", arr)
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))

# Question 4: Separate even and odd numbers from 1 to 20
import numpy as np
arr = np.arange(1, 21)
even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]
print("Array:", arr)
print("Even Numbers:", even)
print("Odd Numbers:", odd)

# Question 5: Reshape numbers from 1 to 12 into different matrices
import numpy as np
arr = np.arange(1, 13)
print("Original Array:", arr)
print("\n2 x 6 Matrix:")
print(arr.reshape(2, 6))
print("\n3 x 4 Matrix:")
print(arr.reshape(3, 4))
print("\n4 x 3 Matrix:")
print(arr.reshape(4, 3))

# Question 6: Add two 3 x 3 NumPy matrices
import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

b = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("Matrix A:\n", a)
print("Matrix B:\n", b)
print("Matrix Addition:\n", a + b)

# Question 7: Perform matrix multiplication using NumPy
import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[7, 8],
              [9, 10],
              [11, 12]])

print("Matrix A:\n", a)
print("Matrix B:\n", b)
print("Matrix Multiplication:\n", np.dot(a, b))

# Question 8: Display the transpose of a 3 x 4 matrix
import numpy as np
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print("Original Matrix:\n", arr)
print("Transpose:\n", arr.T)

# Question 9: Access elements of a 4 x 4 array
import numpy as np
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print("Original Matrix:\n", arr)
print("First Row:", arr[0])
print("Last Column:", arr[:, -1])
print("Diagonal Elements:", np.diag(arr))
print("Second and Third Rows:\n", arr[1:3])

# Question 10: Calculate the sum of each row and column
import numpy as np
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print("Matrix:\n", arr)
print("Sum of Each Row:", np.sum(arr, axis=1))
print("Sum of Each Column:", np.sum(arr, axis=0))

# Question 11: Display elements using NumPy slicing
import numpy as np
arr = np.arange(1, 21)
print("Original Array:", arr)
print("First 5 Elements:", arr[:5])
print("Last 5 Elements:", arr[-5:])
print("Alternate Elements:", arr[::2])
print("Reverse Order:", arr[::-1])

# Question 12: Replace values greater than 50 using Boolean indexing
import numpy as np
arr = np.array([10, 25, 55, 40, 65, 80, 35, 90, 45, 60])
print("Original Array:", arr)
arr[arr > 50] = 0
print("Modified Array:", arr)

# Question 13: Sort a NumPy array in ascending and descending order
import numpy as np
arr = np.array([45, 12, 78, 23, 56, 9, 34])
print("Original Array:", arr)
print("Ascending Order:", np.sort(arr))
print("Descending Order:", np.sort(arr)[::-1])

# Question 15: Concatenate two arrays horizontally and vertically
import numpy as np
a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print("Array A:\n", a)
print("Array B:\n", b)
print("Horizontal Concatenation:\n", np.hstack((a, b)))
print("Vertical Concatenation:\n", np.vstack((a, b)))

# Question 16: Calculate statistics for marks of 10 students
import numpy as np
marks = np.array([78, 85, 90, 66, 72, 88, 95, 60, 81, 75])
print("Student Marks:", marks)
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))

# Question 17: Calculate the class average and find above-average marks
import numpy as np
marks = np.array([
    78, 85, 90, 66, 72, 88, 95, 60, 81, 75,
    69, 92, 84, 73, 87, 55, 98, 79, 68, 91
])
average = np.mean(marks)
print("Student Marks:", marks)
print("Class Average:", average)
print("Marks Above Average:", marks[marks > average])

# Question 18: Create a 3D array of shape (2, 3, 4)
import numpy as np
arr = np.arange(1, 25).reshape(2, 3, 4)
print("3D Array:\n", arr)
print("Number of Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)

# Question 19: Access specified elements of a 3D array
import numpy as np
arr = np.arange(1, 25).reshape(2, 3, 4)
print("3D Array:\n", arr)
print("First Element:", arr[0, 0, 0])
print("Last Element:", arr[-1, -1, -1])
print("Element at Index [0, 1, 2]:", arr[0, 1, 2])
print("Element at Index [1, 2, 3]:", arr[1, 2, 3])

# Question 20: Calculate sums in a 3D array
import numpy as np
arr = np.arange(1, 25).reshape(2, 3, 4)
print("3D Array:\n", arr)
print("Sum of All Elements:", np.sum(arr))
print("Sum of Each Layer:\n", np.sum(arr, axis=(1, 2)))
print("Sum Along Rows:\n", np.sum(arr, axis=2))
print("Sum Along Columns:\n", np.sum(arr, axis=1))

# Question 21: Replace values greater than 50 with zero
import numpy as np
arr = np.random.randint(1, 101, size=(2, 3, 4))
print("Original 3D Array:\n", arr)
arr[arr > 50] = 0
print("Modified 3D Array:\n", arr)

# Question 22: Calculate statistics for a random 3D array
import numpy as np
arr = np.random.randint(1, 101, size=(3, 4, 5))
print("Random 3D Array:\n", arr)
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))

# Question 23: Flatten a 3D array into a 1D array
import numpy as np
arr = np.arange(1, 25).reshape(2, 3, 4)
flat = arr.flatten()
print("Original 3D Array:\n", arr)
print("Flattened 1D Array:", flat)

# Question 24: Flatten an array and calculate its statistics
import numpy as np
arr = np.arange(1, 28).reshape(3, 3, 3)
flat = arr.flatten()
print("Flattened Array:", flat)
print("Sum:", np.sum(flat))
print("Average:", np.mean(flat))
print("Maximum:", np.max(flat))
print("Minimum:", np.min(flat))

# Question 25: Display values greater than 50, even values, and values below average
import numpy as np
arr = np.random.randint(1, 101, size=(3, 4, 5))
flat = arr.flatten()
average = np.mean(flat)
print("Original 3D Array:\n", arr)
print("Flattened Array:", flat)
print("Average:", average)
print("Elements Greater Than 50:", flat[flat > 50])
print("Even Numbers:", flat[flat % 2 == 0])
print("Elements Less Than Average:", flat[flat < average])