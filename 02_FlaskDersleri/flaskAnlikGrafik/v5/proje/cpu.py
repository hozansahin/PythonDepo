from proje import app
from flask import Response
import psutil, json, time

@app.route('/cpu')
def cpu():
    def veriUretim():
        while True:
            cpufreq = psutil.cpu_freq()

            json_data = json.dumps({
                'Maks.': f"{cpufreq.max:.2f}",
                'Geçerli' : f"{cpufreq.current:.2f}"
                }, sort_keys=False, ensure_ascii=False)
            
            yield f"data: {json_data}\n\n"
            time.sleep(1)

    return Response(veriUretim(), mimetype='text/event-stream')