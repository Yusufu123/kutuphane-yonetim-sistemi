"""
İşlem kayıt (log) modülü
"""

import os
from datetime import datetime

LOG_DOSYASI = "logs/islemler.log"


def islem_kaydet(mesaj):
    os.makedirs("logs", exist_ok=True)
    zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    satir = f"[{zaman}] {mesaj}\n"
    with open(LOG_DOSYASI, "a", encoding="utf-8") as f:
        f.write(satir)
