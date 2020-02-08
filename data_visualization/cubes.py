import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [1, 8, 27, 64, 125]
x = list(range(5001))
y = [x**3 for x in x]

plt.scatter(x, y, c=y, cmap=plt.cm.Blues, s=40)

plt.title("Cubic Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cubic of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
