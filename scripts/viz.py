from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# data = pd.read_csv("")

y = np.array([531, 546, 602, 550, 964, 1008, 689, 503, 521, 824, 886, 964, 1200])
x = ['27/4', '28/4', '29/4', '30/4', '01/5', '02/5', '03/5', '04/5', '05/5', '06/5', '07/5', '08/5', '09/5']
fig = plt.plot(x, y, color="lightgreen", linewidth=3)
plt.scatter(x, y, color="green", alpha=0.7)
plt.ylabel("CO2e in kilogram")
plt.xlabel("Date (2023)")
plt.xticks(['27/4', '29/4', '01/5', '03/5','05/5', '07/5', '09/5'])
plt.title("""Day-wise carbon emissions of 
Carbon Stock Exchange""")
plt.grid(True, color="lightgrey")
plt.savefig("chart0.png")
plt.show()

#-------------------------------------

m = np.array([1008, 1300, 995, 845, 1565, 1155, 842, 600])
n = ["Byg Brew", "Bob's Bar", "Social", "Carbon SE", "Iron Hill", "Suzzy Q", "Plan B", "Amoeba"]

fig = plt.bar(n, m, align='center', color="lightgreen")
plt.xticks(rotation=90)
plt.title("CO2e Today compared to other restaurants")
plt.ylabel("CO2e in kilogram")
plt.bar_label(fig)
plt.grid(True, color="lightgray")
plt.tight_layout()
plt.savefig("chart1.png")
plt.show()

#-------------------------------------

c = ["beef", "lamb", "prawns", "fish", "pork", "chicken", "eggs"]
d = [7.9, 4.2, 2.7, 1.9, 1.8, 1.6, 0.6] 
e = ["beef 7.9", "lamb 4.2", "prawns 2.7", "fish 1.9", "pork 1.8", "chicken 1.6", "eggs 0.6"]
colors = ["darkgreen", "olivedrab", "mediumseagreen", "seagreen", "yellowgreen", "lightseagreen", "lightgreen"]

plt.pie(d, labels=e, labeldistance=1.1, center=(0, 0), frame=False, normalize=True, colors=colors, wedgeprops = {"edgecolor": "white", "linewidth": 1, "antialiased": True})
plt.title("Kilograms of CO2e per serving")
plt.tight_layout()
plt.savefig("chart2.png")
plt.show()

#-------------------------------------
