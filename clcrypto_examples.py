import clcrypto

bazowy_tekst = 'Ala ma kota'
print(bazowy_tekst)

zahashowane = clcrypto.hash_password(bazowy_tekst)

print(zahashowane)

print(clcrypto.check_password(bazowy_tekst, zahashowane))
