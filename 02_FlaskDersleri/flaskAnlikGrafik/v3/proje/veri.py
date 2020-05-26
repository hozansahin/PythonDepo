from proje import app
from flask import Response
import os, json, time
from datetime import datetime

@app.route('/veri')
def veri():
    def veriUretim():
        while True:
            tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])

            json_data = json.dumps({
                'Kullanılan': used_m,
                'Boşta' : free_m
                })
            
            yield f"data: {json_data}\n\n"
            time.sleep(1)

    return Response(veriUretim(), mimetype='text/event-stream')