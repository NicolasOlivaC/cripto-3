from Crypto.Cipher import DES3

llave = '12345678secretos12345678'
iv = '13245678'
#representarlo a bytes
keyb = bytes(llave, 'Utf-8')
text1 = bytes(iv, 'Utf-8')

encriptar = DES3.new(keyb, DES3.MODE_CFB, text1)
textoPlano = 'un mensaje que deberia ser secreto'
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
            <div class="key" id= "%s"></div>
            <div class="iv" id= "%s"></div>
        </body>
    </html>
        '''% (textocifrado, textocifrado,llave, iv))

html.close()

