import os
import shutil

def klasor_temizle(klasor_yolu):
    if not os.path.exists(klasor_yolu):
        print("Klasör bulunamadı.")
        return

    dosyalar = os.listdir(klasor_yolu)
    
    for dosya in dosyalar:
        isim, uzanti = os.path.splitext(dosya)
        uzanti = uzanti[1:].lower() 

        if not uzanti:
            continue

        hedef_klasor = os.path.join(klasor_yolu, uzanti)
        
        if not os.path.exists(hedef_klasor):
            os.makedirs(hedef_klasor)
        
        kaynak = os.path.join(klasor_yolu, dosya)
        hedef = os.path.join(hedef_klasor, dosya)
        
        shutil.move(kaynak, hedef)
        print(f"Taşındı: {dosya} -> {uzanti}/")
