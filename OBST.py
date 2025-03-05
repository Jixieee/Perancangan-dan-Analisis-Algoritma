def obst(kunci, frekuensi, n):
    # Matriks untuk menyimpan biaya minimum
    biaya = [[0 for _ in range(n)] for _ in range(n)]
    # Matriks untuk menyimpan akar subpohon optimal
    akar = [[0 for _ in range(n)] for _ in range(n)]
    
    # Inisialisasi untuk kunci tunggal
    for i in range(n):
        biaya[i][i] = frekuensi[i]
        akar[i][i] = i
    
    # Panjang subpohon dari 2 hingga n
    for panjang in range(2, n + 1):
        for i in range(n - panjang + 1):
            j = i + panjang - 1
            biaya[i][j] = float('inf')  # Gunakan float('inf') untuk mendefinisikan nilai tak hingga
            
            # Hitung total frekuensi dari i hingga j
            bobot = sum(frekuensi[i:j+1])
            
            # Coba setiap k sebagai akar
            for k in range(i, j + 1):
                biaya_kiri = biaya[i][k - 1] if k > i else 0
                biaya_kanan = biaya[k + 1][j] if k < j else 0
                total_biaya = biaya_kiri + biaya_kanan + bobot
                
                if total_biaya < biaya[i][j]:
                    biaya[i][j] = total_biaya
                    akar[i][j] = k
    
    return biaya[0][n - 1], akar

# Contoh Penggunaan
kunci = [10, 20, 30, 40]
frekuensi = [3, 3, 1, 1]
n = len(kunci)

biaya_minimum, matriks_akar = obst(kunci, frekuensi, n)
print("Biaya minimum untuk Pohon Pencarian Biner Optimal:", biaya_minimum)
print("Matriks Akar:")
for baris in matriks_akar:
    print(baris)
