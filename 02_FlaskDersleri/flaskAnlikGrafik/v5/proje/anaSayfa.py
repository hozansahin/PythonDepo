from proje import app
from flask import render_template
import platform
from proje.islem import jsonVeri, anahtarlar

uname = platform.uname()

@app.route('/')
def grafik():
    return render_template('grafik.html', baslik="İşte Bunu Seviyorum",
        sistem = uname.system,
        kullanici = uname.node,
        surum = uname.release,
        versiyon = uname.version,
        makine = uname.machine,
        islemci = uname.processor,
        anahtarlar = anahtarlar,
        veriler = jsonVeri
    )