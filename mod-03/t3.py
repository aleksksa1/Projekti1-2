sukupuoli = input('Syötä biologinen sukupuolesi (mies/nainen): ')

hemoglobiini = float (input('Syötä hemoglobiini arvosi (g/l): '))

if sukupuoli == 'nainen' and hemoglobiini < 117:
    print('Alhainen hemoglobiini')

elif sukupuoli == 'nainen' and  117 < hemoglobiini < 175:
    print('Normaali hemoglobiini')

elif sukupuoli == 'nainen' and hemoglobiini > 175:
    print('Korkea hemoglobiini')


if sukupuoli == 'mies' and hemoglobiini < 134:
    print('Alhainen hemoglobiini')

elif sukupuoli == 'mies' and  134 < hemoglobiini < 195:
    print('Normaali hemoglobiini')

elif sukupuoli == 'mies' and hemoglobiini > 195:
    print('Korkea hemoglobiini')
