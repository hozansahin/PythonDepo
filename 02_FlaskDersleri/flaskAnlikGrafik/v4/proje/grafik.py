from proje import app
from flask import render_template

@app.route('/grafik')
def grafik():
    return render_template('grafik.html', baslik="İşte Bunu Seviyorum")