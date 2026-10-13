import numpy as np
import statistics

data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

total_sum = sum(data)
count = len(data)
min_val = min(data)
max_val = max(data)
mean_val = statistics.mean(data)
median_val = statistics.median(data)
stdev_val = statistics.stdev(data)

print("Sum:", total_sum)
print("Count:", count)
print("Min:", min_val)
print("Max:", max_val)
print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", round(stdev_val, 2))
