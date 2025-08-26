kuhan_pituus = input('Syötä kuhan pituus (cm): ')

if float(kuhan_pituus) < 37:
    print('Kuha on alamittainen. Laske takaisin järveen.')
    print(f'Kuhan täytyy olla {37 - float(kuhan_pituus):.2f}cm pidempi.')

else: print('Onneksi olkoon! Sait tarpeeksi suuren kuhan.')
