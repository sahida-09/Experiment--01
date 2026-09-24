import numpy as np
marks = np.array([72, 85, 68, 91, 77, 88, 65, 95, 80, 74])

mean = np.mean(marks)
median = np.median(marks)
std = np.std(marks)
maximum = np.max(marks)
minimum = np.min(marks)

print("Internal Marks:", marks)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std)
print("Maximum:", maximum)
print("Minimum:", minimum)
