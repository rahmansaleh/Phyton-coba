# Tugas input data mahasiswa
"""
                                        1811600632 - Sulfiana Dewi - XM
                                        Data Sains - Tugas Data Mahasiswa
"""

def get_nilai_akhir(nilai_absen = 0, nilai_tugas = 0, nilai_uts = 0, nilai_uas = 0):
    return (0.1 * nilai_absen) + (0.2 * nilai_tugas) + (0.3 * nilai_uts) + (0.4 * nilai_uas) # Rumus untuk mendapatkan nilai akhir

def get_grade_by_nilai_akhir(nilai_akhir = 0): # Metode untuk mendapakan Grade dari Nilai Akhir
    if nilai_akhir >= 85:
        return "A"
    elif nilai_akhir >= 80:
        return "A-"
    elif nilai_akhir >= 75:
        return "B+"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 65:
        return "B-"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 45:
        return "D"
    else:
        return "E"

jml_mahasiswa = int(input("\nMasukkan jumlah mahasiswa yang ingin dihitung : ")) # soal nomor 1 : Input Jumlah Mahasiswa
list_mahasiswa = []
total_nilai = 0

i = 0;
while i < jml_mahasiswa:

    print("\nUntuk Mahasiswa ke", i+1)
    nim = int(input("NIM : ")) # Input data NIM
    nilai_absen = int(input("Nilai absen : ")) # Input data Absen
    nilai_tugas = int(input("Nilai Tugas : ")) # Input data Tugas
    nilai_uts = int(input("Nilai UTS  : ")) # Input data UTS
    nilai_uas = int(input("Nilai UAS : ")) # Input data UAS
    nilai_akhir = int(get_nilai_akhir(nilai_absen, nilai_tugas, nilai_uts, nilai_uas)) # Proses penghitungan Nilai Akhir
    grade  = get_grade_by_nilai_akhir(nilai_akhir) # Proses mendapatkan Grade dari Nilai Akhir

    data = {
        "nim":nim,
        "absen":nilai_absen, 
        "tugas":nilai_tugas, 
        "uts":nilai_uts, 
        "uas":nilai_uas,
        "nilai_akhir":nilai_akhir,
        "grade":grade
        }

    total_nilai = total_nilai + nilai_akhir
    list_mahasiswa.append(data)
    i = i + 1

print('\n\n----------***----------***----------')
print('NIM \t: 1811600632')
print('Nama \t: Sulfiana Dewi')
print('Kelas \t: XM')
print('Matakuliah \t: Data Sains')
print('----------***----------***----------')
print('\nData seluruh mahasiswa')
print('- Nilai rata-rata kelas : ', (total_nilai/len(list_mahasiswa))) # Soal nomor 6 : Perhitungan nilai rata-rata 
print('- Grade rata-rata kelas : ', get_grade_by_nilai_akhir((total_nilai/len(list_mahasiswa)))) # Soal nomor 6 : Perhitungan nilai rata-rata 
print('\n|\tNo\t|\t\tNIM\t|\tAbsen\t|\tTugas\t|\tUTS\t|\tUAS\t|\tNilai Akhir\t|\tGrade\t|')
i = 0
while i < len(list_mahasiswa): # Soal nomor 5 : Cetak seluruh data mahasiswa
    print('|\t', i+1, '\t|\t', list_mahasiswa[i]['nim'], '\t|\t', list_mahasiswa[i]['absen'], '\t|\t', list_mahasiswa[i]['tugas'], '\t|\t', list_mahasiswa[i]['uts'], '\t|\t', list_mahasiswa[i]['uas'], '\t|\t', list_mahasiswa[i]['nilai_akhir'], '\t|\t', list_mahasiswa[i]['grade'], '\t|' )
    i = i + 1
