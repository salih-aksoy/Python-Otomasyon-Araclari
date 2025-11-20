import platform
import psutil

def get_system_info():
    print("-" * 25)
    print("Sistem Bilgisi")
    print("-" * 25)
    
    print(f"İşletim Sistemi: {platform.system()} {platform.release()}")
    print(f"İşlemci: {platform.processor()}")
    
    # RAM bilgisini GB'a çevir
    ram_gb = round(psutil.virtual_memory().total / (1024.0 **3), 2)
    print(f"Toplam RAM: {ram_gb} GB")

if __name__ == "__main__":
    get_system_info()
