#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Import necessary libraries for data visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the student performance dataset
data = pd.read_csv("StudentsPerformance.csv")

# Visualization 1: Scatter plot for math score vs. reading score
plt.scatter(data["math_score"], data["reading_score"], alpha=0.5)
plt.xlabel("Math Score")
plt.ylabel("Reading Score")
plt.title("Math Score vs. Reading Score")
plt.savefig("videos/math_vs_reading.png")
plt.show()

# Visualization 2: Bar chart for gender distribution
sns.countplot(x="gender", data=data)
plt.title("Gender Distribution")
plt.savefig("videos/gender_distribution.png")
plt.show()



# Visualization 3: Histogram of math scores
plt.hist(data["math_score"], bins=20)
plt.xlabel("Math Score")
plt.ylabel("Frequency")
plt.title("Distribution of Math Scores")
plt.savefig("videos/math_score_distribution.png")
plt.show()

# Visualization 4: Box plot of writing scores by gender
sns.boxplot(x="gender", y="writing_score", data=data)
plt.title("Writing Score by Gender")
plt.savefig("videos/writing_score_by_gender.png")
plt.show()

# Visualization 5: sunflower plot for test preparation course completion
count_data = data['test_preparation_course'].value_counts().reset_index()
count_data.columns = ['test_preparation_course', 'count']
# Load the student performance dataset
plt.figure(figsize=(8, 6))
sns.scatterplot(data=count_data, x='test_preparation_course', y='count', s=1000, marker='o', color='blue')
plt.title("Sunflower-like Count Plot")
plt.xlabel("Test Preparation Course")
plt.ylabel("Count")
plt.grid(True)
plt.savefig("videos/sunflower_count_plot.png")
plt.show()

