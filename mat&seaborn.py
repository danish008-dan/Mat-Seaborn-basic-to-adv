# =======================
# 📊 DATA VISUALIZATION NOTES
# Libraries: Matplotlib & Seaborn
# From Basic ➝ Advanced
# =======================

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# -----------------------------------------------------------
# 🔹 1. MATPLOTLIB BASICS
# -----------------------------------------------------------

# Line Plot
x = np.linspace(0, 5, 11)
y = x ** 2
plt.plot(x, y, "r--", label="y = x^2")   # 'r--' → red dashed line
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
plt.legend()
plt.show()

# Multiple Lines
x = np.linspace(0, 5, 11)
plt.plot(x, x**2, "g--", label="y = x^2")
plt.plot(x, x**3, "b--", label="y = x^3")
plt.title("Multiple Line Plot")
plt.legend()
plt.show()

# Line Plot with Customization
x = np.linspace(0, 10, 10)
y = x ** 2
plt.plot(x, y, marker="o", markersize=10, color="purple", linewidth=2, alpha=0.7, linestyle="--")
plt.grid(True, linestyle="--", alpha=0.5)
plt.title("Customized Line Plot")
plt.show()

# Scatter Plot
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y, color="red", marker="*", s=100, alpha=0.7)
plt.title("Scatter Plot Example")
plt.show()

# Bar Chart
categories = ["A", "B", "C", "D"]
values = [4, 7, 1, 8]
plt.bar(categories, values, color="orange")
plt.title("Bar Chart Example")
plt.show()

# Histogram
data = np.random.randn(1000)
plt.hist(data, bins=30, color="skyblue", edgecolor="black", alpha=0.7)
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Pie Chart
sizes = [20, 30, 25, 25]
labels = ["Python", "Java", "C++", "HTML"]
colors = ["red", "green", "blue", "pink"]
plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", shadow=True)
plt.title("Pie Chart Example")
plt.show()

# Subplots (Multiple charts in one figure)
x = np.linspace(0, 5, 11)
y = x ** 2

plt.subplot(1, 2, 1)   # (rows, cols, index)
plt.plot(x, y, "r--")
plt.title("Left Plot")

plt.subplot(1, 2, 2)
plt.plot(x, y**2, "b--")
plt.title("Right Plot")

plt.suptitle("Subplots Example")
plt.show()


# -----------------------------------------------------------
# 🔹 2. SEABORN BASICS
# -----------------------------------------------------------

# Inbuilt datasets for practice
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

print(tips.head())
print(iris.head())

# Scatter Plot
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("Seaborn Scatter Plot")
plt.show()

# Line Plot
sns.lineplot(x="size", y="tip", data=tips)
plt.title("Seaborn Line Plot")
plt.show()

# Bar Plot (mean values)
sns.barplot(x="day", y="total_bill", data=tips, palette="Set2")
plt.title("Bar Plot Example")
plt.show()

# Histogram
sns.histplot(tips["total_bill"], bins=10, kde=True, color="orange")
plt.title("Histogram with KDE")
plt.show()

# Box Plot (detect outliers + median)
sns.boxplot(x="day", y="total_bill", data=tips, palette="coolwarm")
plt.title("Box Plot Example")
plt.show()

# Violin Plot (distribution + median)
sns.violinplot(x="day", y="total_bill", data=tips, palette="muted")
plt.title("Violin Plot Example")
plt.show()

# Swarm Plot (shows individual data points)
sns.swarmplot(x="day", y="total_bill", data=tips, color="black")
plt.title("Swarm Plot Example")
plt.show()

# Count Plot (like bar chart but counts categories)
sns.countplot(x="day", data=tips, palette="Set1")
plt.title("Count Plot Example")
plt.show()

# Joint Plot (combines scatter + histogram)
sns.jointplot(x="total_bill", y="tip", data=tips, kind="scatter")
plt.show()

# Pair Plot (multiple variables comparison)
sns.pairplot(iris, hue="species")
plt.show()

# Heatmap (correlation matrix)
corr = tips.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Heatmap Example")
plt.show()

# Regression Plot (line of best fit)
sns.regplot(x="total_bill", y="tip", data=tips, scatter_kws={"color":"blue"}, line_kws={"color":"red"})
plt.title("Regression Plot Example")
plt.show()

# Categorical Plot (high-level interface)
sns.catplot(x="day", y="total_bill", hue="sex", kind="bar", data=tips)
plt.show()

