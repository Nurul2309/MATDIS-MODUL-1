kuliah_online = True
kuliah_offline = False

pilihan = kuliah_online ^ kuliah_offline

if pilihan:
    print("Pilihan kegiatan VALID")
else:
    print("Pilihan kegiatan TIDAK VALID")