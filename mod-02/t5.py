leiviska = input('Anna leiviskät: ')
naula = input('Anna naulat: ')
luoti = input('Anna luodit: ')

naulat = float(leiviska) * 20 + float(naula)
luodit = naulat * 32 + float(luoti)
grammat_yhteensa = luodit * 13.3

kilot = grammat_yhteensa // 1000
grammat = grammat_yhteensa - kilot * 1000

print(f'Kilogrammat: {kilot:.0f}')
print(f'Grammat: {grammat:.2f}')