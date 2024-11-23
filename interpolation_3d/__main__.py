import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, make_interp_spline

# 5 nokta (x, y, z) olarak tanımlanıyor
points = np.array([
    [1, 2, 1],  # Nokta 1 (x, y, z)
    [2, 3.5, 2],  # Nokta 2
    [3, 1, 3],  # Nokta 3
    [4, 4, 2],  # Nokta 4
    [5, 3, 1]   # Nokta 5
])

# Noktaları ayrıştır
t = np.linspace(0, 1, len(points))  # Parametrik değişken
x, y, z = points[:, 0], points[:, 1], points[:, 2]

# Lineer interpolasyon
linear_interp_x = interp1d(t, x, kind='linear')
linear_interp_y = interp1d(t, y, kind='linear')
linear_interp_z = interp1d(t, z, kind='linear')

# Polinomal interpolasyon (4. dereceden)
polynomial_coeff_x = np.polyfit(t, x, deg=4)
polynomial_coeff_y = np.polyfit(t, y, deg=4)
polynomial_coeff_z = np.polyfit(t, z, deg=4)

polynomial_interp_x = np.poly1d(polynomial_coeff_x)
polynomial_interp_y = np.poly1d(polynomial_coeff_y)
polynomial_interp_z = np.poly1d(polynomial_coeff_z)

# Spline interpolasyon
spline_interp_x = make_interp_spline(t, x)
spline_interp_y = make_interp_spline(t, y)
spline_interp_z = make_interp_spline(t, z)

# Daha fazla noktaya sahip yoğun aralık
t_dense = np.linspace(0, 1, 500)

# Her eksen için interpolasyon değerleri
x_linear, y_linear, z_linear = linear_interp_x(t_dense), linear_interp_y(t_dense), linear_interp_z(t_dense)
x_polynomial, y_polynomial, z_polynomial = polynomial_interp_x(t_dense), polynomial_interp_y(t_dense), polynomial_interp_z(t_dense)
x_spline, y_spline, z_spline = spline_interp_x(t_dense), spline_interp_y(t_dense), spline_interp_z(t_dense)

# Görselleştirme (3D Grafik)
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Orijinal noktaları çiz
ax.scatter(x, y, z, color='red', label='Original Points')

# Lineer interpolasyonu çiz
ax.plot(x_linear, y_linear, z_linear, label='Linear Interpolation', linestyle='--')

# Polinomal interpolasyonu çiz
ax.plot(x_polynomial, y_polynomial, z_polynomial, label='Polynomial Interpolation', linestyle=':')

# Spline interpolasyonu çiz
ax.plot(x_spline, y_spline, z_spline, label='Spline Interpolation', linestyle='-')

# Grafik ayarları
ax.set_title("3D Interpolation Methods")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
plt.show()
