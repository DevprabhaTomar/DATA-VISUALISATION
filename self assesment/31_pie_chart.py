import matplotlib.pyplot as plt

brands = ["Samsung", "Apple", "Xiaomi", "Realme", "Others"]
share = [30, 25, 20, 15, 10]

explode = (0.1, 0, 0, 0, 0)  # highlight max (Samsung)

plt.pie(share, labels=brands, autopct="%1.1f%%", explode=explode)

plt.title("Smartphone Market Share")
plt.show()