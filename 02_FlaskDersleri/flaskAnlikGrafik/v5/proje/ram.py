from proje import app
from flask import Response
import os, json, time, psutil

def birimDonusturucu(bytes, sonEK="B"):
    """
    Baytları doğru biçimine ölçeklendirme
    örn:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    etken = 1024
    for birim in ["", "K", "M", "G", "T", "P"]:
        if bytes < etken:
            return f"{bytes:.2f} {birim}{sonEK}"
        bytes /= etken

@app.route('/ram')
def ram():
    def veriUretim():
        while True:
            svmem = psutil.virtual_memory()

            json_data = json.dumps({
                'Kullanılan': birimDonusturucu(svmem.used).split()[0],
                'Mevcut' : birimDonusturucu(svmem.available).split()[0]
                }, sort_keys=False, ensure_ascii=False)
            
            yield f"data: {json_data}\n\n"
            time.sleep(1)

    return Response(veriUretim(), mimetype='text/event-stream')