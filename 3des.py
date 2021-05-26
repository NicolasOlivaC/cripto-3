from Crypto.Cipher import DES3

llave = ''
iv = ''
while True:
    llave = input('Ingresar llave de 16 o 24 bytes: ')
    if (len(llave) == 16 or len(llave) == 24) : break
while True:
    iv = input('Ingresar IV de 8 bytes: ')
    if (len(iv) == 8) : break
textoPlano = input('Ingresar texto que debe ser cifrado: ')
#representarlo a bytes
keyb = bytes(llave, 'Utf-8')
text1 = bytes(iv, 'Utf-8')

encriptar = DES3.new(keyb, DES3.MODE_CFB, text1)
text = bytes(textoPlano, 'Utf-8')

ciphertext = encriptar.encrypt(text)
textocifrado = ciphertext.hex()
print(f'texto cifrado en bytes: {ciphertext}')
print(f'texto cifrado en hexadecimal: {textocifrado}')


html=open("index.html","w")
html.write('''<!DOCTYPE html>
    <html>
        <head></head>
        <title>Pagina generada desde python</title>
        <body>
            <p>Vista que contiene un mensaje secreto.</p>
            <div class="3des" id= "%s">%s</div>
            <div class="iv" id= "%s"></div>
        </body>
    </html>
        '''% (textocifrado, textocifrado, iv))

html.close()

