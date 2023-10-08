palavras = ('programar', 'aprender', 'curso', 'gratis',
            'python', 'javascript', 'linguagem', 'praticar',
            'futuro', 'lógica', 'tuplas', 'variaveis')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos:', end=' ')
    for letra in p:
        if letra in 'aeiou':
            print(f'{letra.lower()}', end='')
