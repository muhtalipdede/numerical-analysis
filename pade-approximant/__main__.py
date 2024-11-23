import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve
from scipy.special import factorial
np.math = type('math', (), {})()
np.math.factorial = factorial

def pade_approximation(func, x0, m, n):
    """
    Padé yaklaşımı ile bir fonksiyonu [m/n] derecesinde yaklaşıklar.
    
    :param func: Yaklaşılacak fonksiyon (örneğin: np.exp)
    :param x0: Taylor serisi genişleme noktası
    :param m: Paydaki polinomun derecesi
    :param n: Paydaydaki polinomun derecesi
    :return: Pay (P) ve payda (Q) polinomlarının katsayıları
    """
    # Taylor serisi katsayılarını hesapla
    taylor_coeffs = [func(x0 + i * 0j) / np.math.factorial(i) for i in range(m + n + 1)]
    
    # Lineer denklem sistemini kur
    A = np.zeros((n, n))
    b = -np.array(taylor_coeffs[n + 1:m + n + 1])
    
    for i in range(n):
        A[i, :i + 1] = taylor_coeffs[n - i:n + 1][::-1]
    
    # Q katsayılarını çöz (Payda polinomu)
    Q = solve(A, b)
    Q = np.concatenate(([1], Q))  # Q0 = 1
    
    # P katsayılarını hesapla (Pay polinomu)
    P = np.zeros(m + 1)
    for k in range(m + 1):
        P[k] = sum(taylor_coeffs[k - j] * Q[j] for j in range(max(0, k - n), min(k, n) + 1))
    
    return P, Q


def evaluate_pade(P, Q, x):
    """
    Padé yaklaşımını verilen x değerinde değerlendirir.
    
    :param P: Pay polinomu katsayıları
    :param Q: Payda polinomu katsayıları
    :param x: Değerler (numpy array)
    :return: Padé yaklaşımı sonuçları
    """
    numerator = np.polyval(P[::-1], x)  # Pay polinomunu değerlendir
    denominator = np.polyval(Q[::-1], x)  # Payda polinomunu değerlendir
    return numerator / denominator


def taylor_approximation(func, x0, degree, x):
    """
    Taylor serisi yaklaşımını hesaplar.
    
    :param func: Yaklaşılacak fonksiyon (örneğin: np.exp)
    :param x0: Taylor serisi genişleme noktası
    :param degree: Taylor serisi derecesi
    :param x: Değerler (numpy array)
    :return: Taylor serisi yaklaşımı sonuçları
    """
    taylor_coeffs = [func(x0 + i * 0j) / np.math.factorial(i) for i in range(degree + 1)]
    return sum(taylor_coeffs[i] * (x - x0) ** i for i in range(degree + 1))


# Örnek uygulama
if __name__ == "__main__":
    # Fonksiyon ve parametreler
    func = lambda x: np.exp(x)  # e^x fonksiyonu
    # func = lambda x: np.exp(2 * x) # e^(2x) fonksiyonu
    # func = lambda x: np.exp(-2 * x) # e^(-2x) fonksiyonu
    x0 = -2  # Taylor genişleme noktası
    m, n = 2, 2  # Padé yaklaşımı
    taylor_degree = 2  # Taylor serisi derecesi
    
    # Padé yaklaşımını hesapla
    P, Q = pade_approximation(func, x0, m, n)
    
    # Taylor ve Padé yaklaşımlarını hesapla
    x = np.linspace(-2, 2, 500)  # x aralığı
    y_exact = func(x)  # Gerçek değerler
    y_pade = evaluate_pade(P, Q, x)  # Padé yaklaşımı
    y_taylor = taylor_approximation(func, x0, taylor_degree, x)  # Taylor yaklaşımı

    # Grafik çiz
    plt.figure(figsize=(8, 6))
    plt.plot(x, y_exact, label="Gerçek", color="blue", linestyle="--")
    plt.plot(x, y_pade, label=f"Padé Yaklaşımı [{m}/{n}]", color="red")
    plt.plot(x, y_taylor, label=f"Taylor Yaklaşımı (Derece {taylor_degree})", color="green")
    plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
    plt.title("Padé ve Taylor Yaklaşımları")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.show()