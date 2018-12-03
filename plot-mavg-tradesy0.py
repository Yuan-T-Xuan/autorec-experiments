import matplotlib.pyplot as plt

f = open("final-tradesy0")
lines = f.readlines()
f.close()

mavgs = list()
for line in lines:
    if "current moving average:" in line:
        mavgs.append(float(line.split()[-1]))

X = list(range(len(mavgs)))
plt.plot(X, mavgs)
plt.ylabel('Moving Average of AUC')
plt.xlabel('Number of Iterations')
#plt.axis([-1, 121, 0.5, 1.0])
plt.show()
