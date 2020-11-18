név = input('Hogy híjják kendet? ')
kor = input('És hány éves kend? ') # itt még stringet kapunk
év = input('Milyen évet írunk? ')
kor = int(kor) # átalakítjuk egész számmá, azaz int-té
év = int(év)
születési_év = év - kor
print(név, ', kend ', születési_év, '-ben született.')