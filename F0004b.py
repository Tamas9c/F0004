kor = input('És hány éves kend? ')
év = input('Milyen évet írunk? ')
kor = int(kor)
év = int(év)

maradék_év = 18 - kor
érettségi_év = év + maradék_év

print('Kend ', érettségi_év, '-ben fog érettségizni.')