import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, make_interp_spline

# 5 nokta (x, y) olarak tanımlanıyor
x = np.array([1, 2, 3, 4, 5])
y = np.array([12.0, 0.5, 4.0, 11.0, 3.0])

# Lineer interpolasyon
linear_interp = interp1d(x, y, kind='linear')

# Polinomal interpolasyon (4. dereceden, çünkü 5 nokta var)
coefficients = np.polyfit(x, y, deg=4)
polynomial_interp = np.poly1d(coefficients)

# Spline interpolasyon
spline_interp = make_interp_spline(x, y)

# Daha fazla nokta ile çizim için aralık belirleniyor
x_dense = np.linspace(x.min(), x.max(), 500)

# Interpolasyon fonksiyonlarının sonuçları
y_linear = linear_interp(x_dense)
y_polynomial = polynomial_interp(x_dense)
y_spline = spline_interp(x_dense)

# Görselleştirme
plt.figure(figsize=(10, 6))
plt.plot(x_dense, y_linear, label='Linear Interpolation', linestyle='--')
plt.plot(x_dense, y_polynomial, label='Polynomial Interpolation', linestyle=':')
plt.plot(x_dense, y_spline, label='Spline Interpolation', linestyle='-')
plt.scatter(x, y, color='red', label='Original Points')  # Orijinal noktalar

# Grafik ayarları
plt.title("Interpolation Methods Comparison")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()
