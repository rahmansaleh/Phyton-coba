# Tugas input data mahasiswa
"""
NIM : 1811600541
Nama : Muhammad Rahman Saleh
"""
def get_nilai_akhir(nilai_absen = 0, nilai_tugas = 0, nilai_uts = 0, nilai_uas = 0):
    return (0.1 * nilai_absen) + (0.2 * nilai_tugas) + (0.3 * nilai_uts) + (0.4 * nilai_uas)

def get_grade_by_nilai_akhir(nilai_akhir = 0):
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

jml_mahasiswa = int(input("\nMasukkan jumlah mahasiswa yang ingin dihitung : "))
list_mahasiswa = []

i = 0;
while i < jml_mahasiswa:

    print("\nUntuk Mahasiswa ke", i+1)
    nim = int(input("NIM : "))
    nilai_absen = int(input("Nilai absen : "))
    nilai_tugas = int(input("Nilai Tugas : "))
    nilai_uts = int(input("Nilai UTS  : "))
    nilai_uas = int(input("Nilai UAS : "))
    nilai_akhir = int(get_nilai_akhir(nilai_absen, nilai_tugas, nilai_uts, nilai_uas))
    grade  = get_grade_by_nilai_akhir(nilai_akhir)

    data = {
        "nim":nim,
        "absen":nilai_absen, 
        "tugas":nilai_tugas, 
        "uts":nilai_uts, 
        "uas":nilai_uas,
        "nilai_akhir":nilai_akhir,
        "grade":grade
        }

    list_mahasiswa.append(data)
    i = i + 1

print('\n\n----------------------------------------------------')
print('Nim \t: 1811600541')
print('Nama \t: Muhammad Rahman Saleh')
print('----------------------------------------------------')
print('Data seluruh mahasiswa\n')
print('|\tNo\t|\tNIM\t|\tAbsen\t|\tTugas\t|\tUTS\t|\tUAS\t|\tNilai Akhir\t|\tGrade\t|')
i = 0
while i < len(list_mahasiswa):
    print('|\t', i+1, '\t|\t', list_mahasiswa[i]['nim'], '\t|\t', list_mahasiswa[i]['absen'], '\t|\t', list_mahasiswa[i]['tugas'], '\t|\t', list_mahasiswa[i]['uts'], '\t|\t', list_mahasiswa[i]['uas'], '\t|\t', list_mahasiswa[i]['nilai_akhir'], '\t|\t', list_mahasiswa[i]['grade'], '\t|' )
    i = i + 1
