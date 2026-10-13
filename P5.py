import matplotlib.pyplot as plt

# Sample linear data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a simple line plot
plt.figure(figsize=(6, 4))
plt.plot(x, y, marker='o', linestyle='-', color='g', label='y = 2x')

# Add labels and title
plt.title('Simple Linear Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.show()

import matplotlib.pyplot as plt

# Datasets
x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]

x2 = [1, 2, 3, 4, 5]
y2 = [2, 5, 8, 11, 14]

# Plotting both datasets
plt.figure(figsize=(8, 5))
plt.plot(x1, y1, marker='o', linestyle='-', color='g', label='Dataset 1 (y = 2x)')
plt.plot(x2, y2, marker='s', linestyle='--', color='b', label='Dataset 2 (y = 3x - 1)')

# Labels, Title and Legend
plt.title('Comparison of Two Linear Datasets')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.show()

import matplotlib.pyplot as plt

# Sample Data: Study Hours vs Marks
study_hours = [1.5, 2.0, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0]
marks = [40, 45, 50, 58, 60, 65, 68, 72, 75, 78, 83, 85, 90, 92, 95]

# Creating the scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(study_hours, marks, color='darkorange', marker='o', edgecolor='black', s=80, label='Student Data')

# Adding titles and labels
plt.title('Study Hours vs Marks Obtained')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.show()

import matplotlib.pyplot as plt

# Marks data from previous cell
marks = [40, 45, 50, 58, 60, 65, 68, 72, 75, 78, 83, 85, 90, 92, 95]

# Creating the histogram
plt.figure(figsize=(8, 5))
plt.hist(marks, bins=6, color='skyblue', edgecolor='black', alpha=0.7)

# Adding labels and title
plt.title('distribution of marks')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Displaying the plot
plt.show()

import matplotlib.pyplot as plt

# Sample Data: Subjects and Marks
subjects = ['Maths', 'Science', 'English', 'History', 'Geography']
subject_marks = [85, 90, 78, 88, 82]

# Creating the bar chart
plt.figure(figsize=(8, 5))
plt.bar(subjects, subject_marks, color='mediumpurple', edgecolor='black', alpha=0.8, width=0.6)

# Adding labels and title
plt.title('Subject-wise Marks')
plt.xlabel('Subjects')
plt.ylabel('Marks Obtained')
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Displaying the values on top of each bar
for i, v in enumerate(subject_marks):
    plt.text(i, v + 1, str(v), ha='center', fontweight='bold')

# Displaying the plot
plt.show()

import matplotlib.pyplot as plt

# Datasets
x_line = [1, 2, 3, 4, 5]
y_line = [2, 4, 6, 8, 10]

study_hours = [1.5, 2.0, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0]
marks = [40, 45, 50, 58, 60, 65, 68, 72, 75, 78, 83, 85, 90, 92, 95]

# Creating subplots using plt.subplot
plt.figure(figsize=(14, 5))

# Left plot: Line Plot
plt.subplot(1, 2, 1)
plt.plot(x_line, y_line, marker='o', linestyle='-', color='g', label='y = 2x')
plt.title('Simple Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

# Right plot: Scatter Plot
plt.subplot(1, 2, 2)
plt.scatter(study_hours, marks, color='darkorange', marker='o', edgecolor='black', s=80, label='Student Data')
plt.title('Study Hours vs Marks')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Data: Subjects and Marks from previous steps
subjects = ['Maths', 'Science', 'English', 'History', 'Geography']
subject_marks = [85, 90, 78, 88, 82]

# Creating the pie chart
plt.figure(figsize=(8, 8))
plt.pie(
    subject_marks,
    labels=subjects,
    autopct='%1.1f%%',
    startangle=140,
    colors=['skyblue', 'lightgreen', 'lightcoral', 'gold', 'mediumpurple'],
    wedgeprops={'edgecolor': 'black', 'linewidth': 1, 'antialiased': True}
)

# Adding a title
plt.title('Distribution of Marks by Subject')

# Displaying the plot
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Create the dataset
data = {
    'Student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'],
    'Study_Hours': [2, 3, 4, 5, 6, 7, 8, 9, 3, 4, 6, 7, 8, 2, 5],
    'Attendance': [65, 70, 75, 80, 82, 85, 90, 92, 68, 72, 78, 88, 91, 60, 76],
    'Marks': [45, 50, 58, 65, 70, 75, 82, 88, 48, 55, 68, 78, 85, 40, 62],
    'Assignments': [5, 6, 7, 8, 8, 9, 10, 10, 5, 6, 8, 9, 10, 4, 7],
    'Gender': ['F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F']
}

df = pd.DataFrame(data)
display(df)

# Create subplots to show all forms of applicable graphs
fig = plt.figure(figsize=(16, 18))

# 1. Scatter Plot: Study Hours vs Marks
plt.subplot(3, 2, 1)
plt.scatter(df['Study_Hours'], df['Marks'], s=df['Attendance'], c='purple', alpha=0.6, edgecolors='black')
plt.title('Study Hours vs Marks (Size bubble = Attendance)')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.grid(True, linestyle='--', alpha=0.5)

# 2. Line Plot: Attendance vs Marks (sorted to show trend)
df_sorted = df.sort_values(by='Attendance')
plt.subplot(3, 2, 2)
plt.plot(df_sorted['Attendance'], df_sorted['Marks'], marker='o', color='teal', linestyle='-', linewidth=2)
plt.title('Attendance vs Marks Trend')
plt.xlabel('Attendance (%)')
plt.ylabel('Marks')
plt.grid(True, linestyle='--', alpha=0.5)

# 3. Bar Chart: Average Marks by Gender
gender_marks = df.groupby('Gender')['Marks'].mean().reset_index()
plt.subplot(3, 2, 3)
plt.bar(gender_marks['Gender'], gender_marks['Marks'], color=['pink', 'lightblue'], edgecolor='black', width=0.4)
plt.title('Average Marks by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Marks')
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.5)
for idx, val in enumerate(gender_marks['Marks']):
    plt.text(idx, val + 2, f"{val:.1f}", ha='center', fontweight='bold')

# 4. Histogram: Distribution of Marks
plt.subplot(3, 2, 4)
plt.hist(df['Marks'], bins=5, color='orange', edgecolor='black', alpha=0.7)
plt.title('Distribution of Marks')
plt.xlabel('Marks Bin')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.5)

# 5. Pie Chart: Proportion of Gender in Class
gender_counts = df['Gender'].value_counts()
plt.subplot(3, 2, 5)
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=['pink', 'lightblue'], wedgeprops={'edgecolor': 'black'})
plt.title('Gender Distribution')

plt.tight_layout()
plt.show()

