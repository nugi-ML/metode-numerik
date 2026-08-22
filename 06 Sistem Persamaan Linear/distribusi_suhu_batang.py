import numpy as np
import matplotlib.pyplot as plt

# PARAMETER
L = 1.0         # panjang batang
T_kiri = 100.0  # suhu ujung kiri
T_kanan = 0.0   # suhu ujung kanan 

N = 10          # jumlah titk interior

# GRID
dx = L / (N + 1)

x = np.linspace(0, L, N + 2)

# MEMBUAT MATRIKS A
A = np.zeros((N, N))

for i in range(N):
    # diagonal utama
    A[i,i] = 2

    # diagonal bawah
    if i > 0:
        A[i, i - 1] = -1

    # diagonal atas
    if i < N - 1:
        A[i, i + 1] = -1

# MEMBUAT VEKTOR B
b = np.zeros(N)

# kontribusi batas kiri
b[0] += T_kiri

# kontribusi batas kanan
b[-1] += T_kanan

# SISTEM PERSAMAAN LIENAR
T_interior = np.linalg.solve(A, b)

# MEMASUKKAN SUHU BATAS
T = np.zeros(N + 2)

T[0] = T_kiri
T[-1] = T_kanan

T[1:-1] = T_interior

# MENGHITUNG SOLUSI ANALITIK
T_analitik = T_kiri + (T_kanan - T_kiri) * x

# MENAMPILKAN HASIL
print("Posisi (m)\tSuhu (c)\tSuhu Analitik (C)")
print("-------------------------------------------")

for i in range(len(x)):
    print(f"{x[i]:.3f}\t\t{T[i]:.3f}\t\t{T_analitik[i]:.3f}")

# MENGHITUNG ERROR
error = np.abs(T - T_analitik)

print(f"\nError maksimum: {np.max(error)}")

# VISUALISASI
plt.figure(figsize=(8,5))
plt.plot(x, T, 'o-', label="Metode Beda Hingga")
plt.plot(x, T_analitik, '--', label="Solusi Analitik")
plt.xlabel("Posisi x (m)")
plt.ylabel("Suhu T (C)")
plt.title("Distribusi Suhu pada Batang 1D")
plt.grid(True)
plt.legend()
plt.show()