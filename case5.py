for mahasiswa_ti, asisten_lab in data_pengujian:
    boleh_menggunakan = mahasiswa_ti or asisten_lab

    if boleh_menggunakan:
        print("Boleh menggunakan komputer")
    else:
        print("Tidak boleh menggunakan komputer")
