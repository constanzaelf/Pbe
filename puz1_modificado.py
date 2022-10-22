import time
import binascii
from pn532pi import Pn532, pn532
from pn532pi import Pn532Hsu
PN532_HSU = Pn532Hsu(Pn532Hsu.RPI_MINI_UART)
nfc = Pn532(PN532_HSU)

class Rfid:
    def read_uid(self):
	#vamos a establecer la conexion la placa de elechouse
        PN532_HSU = Pn532Hsu(Pn532Hsu.RPI_MINI_UART)
        nfc = Pn532(PN532_HSU)
	#usamos las funciones que me aportan las librerias
        nfc.begin()
        nfc.SAMConfig()

	#aproximacion de la tarjeta al lector
        print("ESPERANDO A QUE APROXIME LA TARJETA...")
        success, uid = nfc.readPassiveTargetID(pn532.PN532_MIFARE_ISO14443A_106KBPS)
	#en vez de usar una funcion loop  hacemos un while dentro de la misma funcion
        while(not success):
            success, uid = nfc.readPassiveTargetID(pn532.PN532_MIFARE_ISO14443A_106KBPS)

        txto= uid.hex().upper()
        print("Identificador de la tarjeta: \n")
        return txto

if __name__ == '__main__':
        rf = Rfid()
        uid = rf.read_uid()
        print(uid)
