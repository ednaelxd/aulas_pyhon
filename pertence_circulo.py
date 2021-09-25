xc = float ( input('Digite a coordenada x do centro da circunferência: '))
yc = float ( input('Digite a coordenada y do centro da circunferência: '))
raio = float ( input('Qual o tamanho do raio da circunferência:? '))

xp = float ( input('Digite a coordenada x ponto: '))
yp = float ( input('Digite a coordenada y ponto: '))

print('(',xc,',',yc,',',raio,')','dados da circunferencia')
print('(',xp,',',yp,')',"ponto testado")

if (xp<=(xc+raio) and xp>=(xc-raio)) and (yp<=(yc+raio) and yp>=(yc-raio)) :
    if ( abs(xp-xc)==raio and abs(yp-yc)==raio ) :
        print('O ponto (',xp,',',yp,')',"está na borda do círculo")
    print('O ponto (',xp,',',yp,')',"pertence ao círculo")
elif (xp>(xc+raio) or xp<(xc-raio)) or (yp>(yc+raio) or yp<(yc-raio)) :
    print('O ponto (',xp,',',yp,')',"não pertence ao círculo")
else:
    print ("Deu, zebra!")
