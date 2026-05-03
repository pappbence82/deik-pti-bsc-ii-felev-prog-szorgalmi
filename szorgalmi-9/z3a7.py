import sys
import math

class LZWBinFa:
    class Csomopont:
        def __init__(self, b='/'):
            self.betu = b
            self.balNulla = None
            self.jobbEgy = None

        def nullasGyermek(self):
            return self.balNulla

        def egyesGyermek(self):
            return self.jobbEgy

        def ujNullasGyermek(self, gy):
            self.balNulla = gy

        def ujEgyesGyermek(self, gy):
            self.jobbEgy = gy

        def getBetu(self):
            return self.betu

    def __init__(self):
        self.gyoker = self.Csomopont('/')
        self.fa = self.gyoker
        self.melyseg = 0
        self.atlagosszeg = 0
        self.atlagdb = 0
        self.szorasosszeg = 0.0
        self.maxMelyseg = 0
        self.atlag = 0.0
        self.szoras = 0.0

    def push(self, b):
        if b == '0':
            if not self.fa.nullasGyermek():
                uj = self.Csomopont('0')
                self.fa.ujNullasGyermek(uj)
                self.fa = self.gyoker
            else:
                self.fa = self.fa.nullasGyermek()
        else:
            if not self.fa.egyesGyermek():
                uj = self.Csomopont('1')
                self.fa.ujEgyesGyermek(uj)
                self.fa = self.gyoker
            else:
                self.fa = self.fa.egyesGyermek()

    def kiir(self, os=None, elem=None, melyseg=None):
        if os is None:
            os = sys.stdout
        if elem is None:
            elem = self.gyoker
            self.melyseg = 0
        if melyseg is None:
            melyseg = [0]
        if elem is not None:
            melyseg[0] += 1
            self.kiir(os, elem.egyesGyermek(), melyseg)
            os.write("---" * melyseg[0] + elem.getBetu() + "(" + str(melyseg[0] - 1) + ")\n")
            self.kiir(os, elem.nullasGyermek(), melyseg)
            melyseg[0] -= 1

    def getMelyseg(self):
        self.melyseg = 0
        self.maxMelyseg = 0
        self._rmelyseg(self.gyoker)
        return self.maxMelyseg - 1

    def getAtlag(self):
        self.melyseg = 0
        self.atlagosszeg = 0
        self.atlagdb = 0
        self._ratlag(self.gyoker)
        self.atlag = self.atlagosszeg / self.atlagdb
        return self.atlag

    def getSzoras(self):
        self.atlag = self.getAtlag()
        self.szorasosszeg = 0.0
        self.melyseg = 0
        self.atlagdb = 0
        self._rszoras(self.gyoker)
        if self.atlagdb - 1 > 0:
            self.szoras = math.sqrt(self.szorasosszeg / (self.atlagdb - 1))
        else:
            self.szoras = math.sqrt(self.szorasosszeg)
        return self.szoras

    def _rmelyseg(self, elem):
        if elem is not None:
            self.melyseg += 1
            if self.melyseg > self.maxMelyseg:
                self.maxMelyseg = self.melyseg
            self._rmelyseg(elem.egyesGyermek())
            self._rmelyseg(elem.nullasGyermek())
            self.melyseg -= 1

    def _ratlag(self, elem):
        if elem is not None:
            self.melyseg += 1
            self._ratlag(elem.egyesGyermek())
            self._ratlag(elem.nullasGyermek())
            self.melyseg -= 1
            if elem.egyesGyermek() is None and elem.nullasGyermek() is None:
                self.atlagdb += 1
                self.atlagosszeg += self.melyseg

    def _rszoras(self, elem):
        if elem is not None:
            self.melyseg += 1
            self._rszoras(elem.egyesGyermek())
            self._rszoras(elem.nullasGyermek())
            self.melyseg -= 1
            if elem.egyesGyermek() is None and elem.nullasGyermek() is None:
                self.atlagdb += 1
                self.szorasosszeg += (self.melyseg - self.atlag) ** 2


def usage():
    print("Usage: lzwtree in_file -o out_file")


def main():
    if len(sys.argv) != 4:
        usage()
        return -1

    in_file = sys.argv[1]

    if sys.argv[2][1] != 'o':
        usage()
        return -2

    try:
        be = open(in_file, 'rb')
    except:
        print(in_file + " nem letezik...")
        usage()
        return -3

    ki = open(sys.argv[3], 'w')

    binFa = LZWBinFa()

    for byte in iter(lambda: be.read(1), b''):
        if byte == b'\x0a':
            break

    kommentben = False

    for byte in iter(lambda: be.read(1), b''):
        b = byte[0]

        if b == 0x3e:
            kommentben = True
            continue

        if b == 0x0a:
            kommentben = False
            continue

        if kommentben:
            continue

        if b == 0x4e:
            continue

        for i in range(8):
            if b & 0x80:
                binFa.push('1')
            else:
                binFa.push('0')
            b = (b << 1) & 0xff

    binFa.kiir(ki)
    ki.write("depth = " + str(binFa.getMelyseg()) + "\n")
    ki.write("mean = " + str(binFa.getAtlag()) + "\n")
    ki.write("var = " + str(binFa.getSzoras()) + "\n")

    ki.close()
    be.close()


main()