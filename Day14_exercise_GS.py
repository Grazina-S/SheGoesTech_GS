# 1. plot a graph of x and y
# x would be values from -10 to 10 (21 values)
# y would be the cube of x + 5

# you could use a different library than matplotlib but it is the most popular one
# will will explore other ones later on in the course
from  matplotlib import pyplot as plt

x = list(range(-10, 11))
y = [(i+5)**3 for i in x]
fig, ax = plt.subplots()
ax.scatter(x, y)
plt.show()
