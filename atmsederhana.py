print('*'*25)
print('Selamat Datang di ATM BPK')
print('*'*25)
print('Silahkan pilih menu: ')
print(' 1. Check Saldo','\n 2. Tarik Saldo','\n 3. Setor Uang') #guna \n untuk memberikan baris baru dibawah

nilai = int(input('Masukkan pilihan Anda: '))
if nilai == 1:
    print('Saldo Anda 1.000.000')
    
elif nilai ==2:
    print('TARIK SALDO ','\n 1) 1.000.000','\n 2) 500.000', '\n 3) 200.000')
    print(' 4) Masukkan nominal')
    pilih = int(input('Silahkan Pilih: '))
    uang = 1000000
    if pilih == 1:
        print('Tarik Saldo sebesar 1.000.000 BERHASIL')
        print('Sisa Saldo Anda ',f'1.000.000 - 1.000.000 = {uang - 1000000}')
    elif pilih == 2:
        print('Tarik Saldo sebesar 500.000 BERHASIL')
        print('Sisa Saldo Anda ',f'1.000.000 - 500.000 = {uang - 500000}')
    elif pilih == 3:
        print('Tarik Saldo sebesar 200.000 BERHASIL')
        print('Sisa Saldo Anda ',f'1.000.000 - 200.000 = {uang - 200000}')
    elif pilih == 4:
        duit =int(input('Masukkan nominal (contoh 50000) : '))
        print(f'Tarik Saldo sebesar {duit} BERHASIL')
        print('Sisa Saldo Anda',f'1.000.000 - {duit} = {uang-duit}')
    else:
        print('ERROR SILAHKAN COBA LAIN KALI')    
        
elif nilai == 3:
    print('Masukkan jumlah yang akan Anda Setor')
    setor = int(input('Setor (contoh 50000) :'))
    print(f'Uang Anda bertambah menjadi {setor + 1000000}')  
    print(f'1000000 + {setor} = {setor + 1000000}')      

else:
    print('ERROR SILAHKAN KEMBALI LAIN WAKTU')            