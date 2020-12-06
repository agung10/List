# Nama : Agung Mubarok
# NIM  : 0110120196
# Kelas: Sistem Informasi - 05

def jumlah_batas(nums, batas):
  # Variabel hasil yang menampung nilai awal 0
  hasil = 0
  # Membuat perulangan apakah i terdapat di dalam parameter nums
  for i in nums:
    # Jika i/isi dari parameter nums lebih besar dari parameter batas
    if i > batas:
      # Maka variabel hasil akan melakukan penambahan 1 di setiap perulangannya
      hasil += i
    # Jika tidak
    else:
      # Akan melanjutkan nilai
      continue
  # Mengembalikan nilai hasil
  return hasil

# ==========================================================
# ==========================================================

def list_nonvokal(s):
  # Variabel yang berisikan list huruf vokal
  huruf_vokal = ["A", "I", "U", "E", "O"]
  # Membuat variabel hasil yang menampung array kosong
  hasil = []
  # Membuat perulangan dengan jarak dari 0 hingga sebelum 1 nilai dari banyaknya nilai di dalam parameter s
  for i in range(0, len(s)):
    # Jika nilai parameter s yang sudah di konvesikan menjadi huruf besar berada di dalam variabel huruf vokal
    if s[i].upper() in huruf_vokal:
      # Maka akan melanjutkan ke nilai berikutnya (ngeskip)
      continue
    # Jika tidak
    else:
      # Variabel hasil akan ditambahkan nilai parameter s dengan i di dalam array 
      hasil.append(s[i])
  # Mengembalikan nilai hasil
  return hasil

# ==========================================================
# ==========================================================

def list_modify(alist, command, position, value=None):
  # Jika parameter command sama dengan add dan posisi sama dengan end
  if command == "add" and position == "end":
    # Maka akan menambahkan value dari belakang
    alist.append(value)
    # Mengembalikan nilai alist
    return alist

  # Jika parameter command sama dengan add dan posisi sama dengan start
  elif command == "add" and position == "start":
     # Maka akan menyisipkan nilai value di index 0 / di nilai yang pertama
    alist.insert(0,value)
    # Mengembalikan nilai alist
    return alist

  # Jika parameter command sama dengan remove dan posisi sama dengan start
  elif command == "remove" and position == "start":
    # Maka akan menghapus nilai pada list berdasarkan urutannya yaitu index 0
    alist.pop(0)
    # Mengembalikan nilai alist
    return alist

  # Jika parameter command sama dengan remove dan posisi sama dengan end
  elif command == "remove" and position == "end":
    # Maka akan menghapus nilai pada list berdasarkan urutannya
    alist.pop()
    # Mengembalikan nilai alist
    return alist

# ==========================================================
# ==========================================================

# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya.
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  r = jumlah_batas([8, 7, 6, 10, 1], 5)
  print(f"jumlah_batas([8, 7, 6, 10, 1], 5) = {r} \n(solusi: 31)")
  print()
  r = jumlah_batas([1, -7, -10, 1], -5)
  print(f"jumlah_batas([1, -7, -10, 1], -5) = {r} \n(solusi: 2)")
  print()
  r = list_nonvokal('Halo')
  print(f"list_nonvokal('Halo') = {r} \n(solusi: ['H', 'l'])")
  print()
  r = list_nonvokal('AAAAAooooo')
  print(f"list_nonvokal('AAAAAooooo') = {r} \n(solusi: [])")
  print()
  r = list_nonvokal('Saya cinta programming')
  print(f"list_nonvokal('Saya cinta programming') = {r} \n(solusi: ['S', 'y', ' ', 'c', 'n', 't', ' ', 'p', 'r', 'g', 'r', 'm', 'm', 'n', 'g'])")
  print()
  r = list_modify(['ayam', 'ikan', 'kucing'], 'add', 'start', 'bebek')
  print(f"list_modify(['ayam', 'ikan', 'kucing'], 'add', 'start', 'bebek') = {r} \n(solusi: ['bebek', 'ayam', 'ikan', 'kucing'])")
  print()
  r = list_modify(['ayam', 'ikan', 'kucing'], 'add', 'end', 'bebek')
  print(f"list_modify(['ayam', 'ikan', 'kucing'], 'add', 'end', 'bebek') = {r} \n(solusi: ['ayam', 'ikan', 'kucing', 'bebek'])")
  print()
  r = list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'start')
  print(f"list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'start') = {r} \n(solusi: ['ikan', 'kucing'])")
  print()
  r = list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'end')
  print(f"list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'end') = {r} \n(solusi: ['ayam', 'ikan'])")
  print()

if __name__ == '__main__':
  test()