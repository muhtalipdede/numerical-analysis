import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# Düzensiz noktalar (x, y) ve bu noktalardaki z değerleri
points = np.random.rand(20, 2) * 10  # 20 adet rastgele (x, y) noktası
values = np.sin(points[:, 0]) + np.cos(points[:, 1])  # Z değerleri

# Düzenli bir ızgara oluştur
grid_x, grid_y = np.mgrid[0:10:100j, 0:10:100j]

# GridData ile yüzey interpolasyonu
grid_z = griddata(points, values, (grid_x, grid_y), method='cubic')

# Görselleştirme
plt.figure(figsize=(10, 8))
plt.contourf(grid_x, grid_y, grid_z, levels=20, cmap='viridis')  # Renkli kontur haritası
plt.scatter(points[:, 0], points[:, 1], c=values, s=50, edgecolor='black', label='Original Points')  # Orijinal noktalar
plt.colorbar(label='Z Value')
plt.title("2D Surface Interpolation using GridData")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
