import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

N = 1000
ds = [2 ** i for i in range(1, 15)]

figure_path = "figure.png"

ratios = []
for d in ds:
    q = np.random.random(size=(d))
    X = np.random.random(size=(N, d))
    dists = np.linalg.norm(X - q, axis=1)
    mi, mx = np.min(dists), np.max(dists)
    ratio = round((mx - mi) / mi, 3)
    ratios.append(ratio)
    print(f"dim = {d}, ratio = {ratio}")

plt.figure(figsize=(10, 8), dpi=120)
plt.title(
    f"Relative difference between the distances of the the nearest neighbor and the farthest neighbor")
plt.xlabel("Dimensionality")
plt.ylabel("Relative difference of distances")
plt.xscale('log', base=2)
plt.yscale('log')
plt.plot(ds, ratios, linestyle='dashdot', marker='D')
plt.savefig(figure_path)