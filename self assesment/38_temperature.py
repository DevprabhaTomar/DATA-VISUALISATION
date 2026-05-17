import numpy as np
import matplotlib.pyplot as plt

temps = np.random.randint(20, 45, 100)

plt.hist(temps, bins=10)

plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")

plt.show()