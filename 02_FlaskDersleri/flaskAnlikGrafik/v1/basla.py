from flask import Flask, Response, render_template, make_response, jsonify
from flask_sitemap import Sitemap
import os, psutil
import json, time
from datetime import datetime

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
ext = Sitemap(app=app)

@app.route('/')
def bilgi():
    cpu = dict(psutil.virtual_memory()._asdict())

    tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])

    return make_response(jsonify(cpu=cpu, ram={'total':tot_m, 'used':used_m, 'free':free_m}))

@app.route('/veri')
def veri():
    def veriUretim():
        while True:
            tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])

            json_data = json.dumps({
                'Zaman': datetime.now().strftime('%H:%M:%S'),
                'Veri': used_m
                })
            
            yield f"data: {json_data}\n\n"
            time.sleep(1)

    return Response(veriUretim(), mimetype='text/event-stream')

@app.route('/grafik')
def grafik():
    return render_template('index.html', baslik="İşte Bunu Seviyorum")

@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), filename='img/favicon.ico', mimetype='image/x-icon')

if __name__ == '__main__':
    app.config['JSON_SORT_KEYS'] = False
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.config['JSON_AS_ASCII'] = False
    app.config['SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS'] = True
    #app.run(debug = True, host = '0.0.0.0', port = port)
    from waitress import serve
    serve(app, host = "0.0.0.0", port = port)