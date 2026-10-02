memiliki_kartu_mahasiswa = True
memiliki_surat_izin = False

boleh_mendapat_bantuan = memiliki_kartu_mahasiswa or memiliki_surat_izin

if boleh_mendapat_bantuan:
    print("Dapat menerima bantuan akademik")
else:
    print("Tidak dapat menerima bantuan akademik")