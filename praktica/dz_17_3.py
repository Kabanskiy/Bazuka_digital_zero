# Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в веденном с клавиатуры слове.
# (Пример HjkLM- 1 пара нижнего, 1 пара верхнего), а также сколько всего букв в слове, сколько гласных и согласных.


st = input('Введи текст контрастного регистра: ')

alph_niz_gl = 'ёуеыаоэяию'
alph_verhn_gl = 'ЁУЕЫАОЭЯИЮ'
alph_niz_sog = 'йцкннгшщзхфвпрлджчсмтб'
alph_verh_sog = 'ЙЦКНГШЩЗХФВПРЛДЖЧСМТБ'
gl_niz = 0
gl_verh = 0
sog_niz = 0
sog_verh = 0
c = 0

for i in st:
    if st.count(i) >= 2:
        gl_niz += 1
        c += gl_niz // 2
    elif st.count(i) >= 2:
        gl_verh += 1
        c += gl_verh // 2
    elif st.count(i) >= 2:
        sog_niz += 1
        c += sog_niz // 2
    elif st.count(i) >= 2:
        sog_verh += 1
        c += sog_verh // 2
    else:
        print('хуйня, переделывай')
print('Всего пар: ', c//2)
print('Всего букв: ', len(st))





