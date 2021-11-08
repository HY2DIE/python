# soal 1


jaminput = int(input("Mulai Acara Jam = "))
menitinput = int(input("Mulai Acara Menit = "))
durasiinput = int(input("Durasi Acara = "))
AcaraMulaijam = int(round(jaminput + durasiinput / 60))
AcaraMulaimenit= int((menitinput + durasiinput) % 60) 
print(f"Acara akan selesai pukul = {AcaraMulaijam}:{AcaraMulaimenit}")






 



 
