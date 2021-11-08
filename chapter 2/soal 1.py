# soal 1


jaminput = int(input("Mulai Acara Jam = "))
menitinput = int(input("Mulai Acara Menit = "))
durasiinput = int(input("Durasi Acara = "))

AcaraMulaimenit= int((menitinput + durasiinput) % 60)
AcaraMulaijam = int(round(jaminput +( (menitinput + durasiinput )/ 60))) 
print(f"Acara akan selesai pukul = {AcaraMulaijam}:{AcaraMulaimenit}")






 



 
