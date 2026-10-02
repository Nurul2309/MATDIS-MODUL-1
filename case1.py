aktif = True
nilai_baik = True
tidak_melanggar = True

lulus = aktif and nilai_baik and tidak_melanggar

if lulus:
    print("Mahasiswa LULUS beasiswa")
else:
    print("Mahasiswa TIDAK LULUS beasiswa")