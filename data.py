import matplotlib.pyplot as plt

n = 0
y = 1
yaxis = []
xaxis = []

while y >0 :
    y = int(120 * ((0.7)** n))
    yaxis.append(y) 
    xaxis.append(n)
    n = n  + 1

plt.plot(xaxis, yaxis)
plt.xlabel("nth order")
plt.ylabel("no of share remain")
plt.title("share opposite n")

print(xaxis)
print(yaxis)

# plt.show()

