terdaftar = True
hadir_minimal = True
sudah_mengerjakan_tugas = False

boleh_ujian = terdaftar and hadir_minimal and sudah_mengerjakan_tugas

if boleh_ujian:
    print("Mahasiswa BOLEH mengikuti ujian")
else:
    print("Mahasiswa TIDAK BOLEH mengikuti ujian")