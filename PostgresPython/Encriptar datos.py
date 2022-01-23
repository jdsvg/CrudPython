from django.contrib.auth.password_validation import validate_password
from Crypto.Cipher import AES
import scrypt, os, binascii
import string, random
from django.contrib.auth.hashers import make_password

class Encriptar_Datos:

    def encrypt_AES_GCM(self,password):
        #Generando codigo de secuencia
        x_cod_seg = ""
        for i in range(5): x_cod_seg += random.choice(string.ascii_letters)+str(random.randint(0,9))
        code_sec = bytes(x_cod_seg, 'utf-8')
        kdfSalt = os.urandom(16)#Genera la sal (binario bytes)
        secretKey = scrypt.hash(code_sec, kdfSalt, N=16384, r=8, p=1, buflen=32)#Genera la llave secreta (binario bytes)
        aesCipher = AES.new(secretKey, AES.MODE_GCM)#Aplica el algoritmo AES (Obj Class)
        ciphertext, authTag = aesCipher.encrypt_and_digest(password)#Encriptando password con el obj AES en base a la secretKey
        #nonce pasa de objeto a binario
        return (kdfSalt, aesCipher.nonce, authTag, code_sec, ciphertext)
    
    def decrypt_AES_GCM(self, llave):
        # kdfSalt*: llave[:32]
        # aesCipher*: llave[32:64]
        # authTag*: llave[64:96]
        # code_sec**: llave[96:116]
        # ciphertext*: llave[116:]
        secretKey = scrypt.hash(binascii.unhexlify(((llave[96:116]).encode('utf-8'))) , binascii.unhexlify(((llave[:32]).encode('utf-8'))), N=16384, r=8, p=1, buflen=32)
        aesCipher = AES.new(secretKey, AES.MODE_GCM, binascii.unhexlify(((llave[32:64]).encode('utf-8'))))
        plaintext = aesCipher.decrypt_and_verify(binascii.unhexlify(((llave[116:]).encode('utf-8'))) , binascii.unhexlify(((llave[64:96]).encode('utf-8'))) )
        return plaintext
#
#Obj Encriptar_Datos
obj_Encriptar_Datos = Encriptar_Datos()
#Simulacion de data
validate_data = {
    'password':"unacontraseñamuysecreta"
}
#
#
#Encriptando datos
encryptedMsg = obj_Encriptar_Datos.encrypt_AES_GCM(bytes(validate_data['password'], 'utf-8'))
#
#from_bin_to_hex = binascii.hexlify(encryptedMsg[0])#From bin to hex
#from_hexBytes_to_str = binascii.hexlify(encryptedMsg[0]).decode("utf-8")#From hex to str
#
llave = ""
for indice in encryptedMsg:#Convtirtiendo datos
    llave += binascii.hexlify(indice).decode("utf-8")#From bin to hex to str
#
##Orden de formateo
#Pasar de binario a hexadecimal
#Pasar de hexadecimal a str
#Concadenar
#
#
#Odern de desformato
#Desconcatenar
#Pasar de str a hexadecimal
#Pasar de hexadecimal a binario
#
decryptedMsg = obj_Encriptar_Datos.decrypt_AES_GCM(llave)
#
#
##El deber ser:
#Optener datos
#Encriptar
#Pasar a str
#Luego, en la desencriptacion
#Traer datos
#Pasar a bytes
#Desencriptar
... 