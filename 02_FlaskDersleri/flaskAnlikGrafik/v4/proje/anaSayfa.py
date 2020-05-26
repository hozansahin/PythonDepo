from proje import app
from flask import make_response, jsonify
import psutil, os

@app.route('/')
def bilgi():
    cpu = dict(psutil.virtual_memory()._asdict())

    tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])

    return make_response(jsonify(cpu=cpu, ram={'total':tot_m, 'used':used_m, 'free':free_m}))