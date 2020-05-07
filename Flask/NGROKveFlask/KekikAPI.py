from flask import Flask, jsonify, make_response, request, send_from_directory
from flask_ngrok import run_with_ngrok

from Kaziyicilar.korona import koronaSpatula
from Kaziyicilar.hurriyetEmlak import hurriyetSpatula
from Kaziyicilar.nobetciEczane import nobetciSpatula
from Kaziyicilar.iftarSaati import sahuraKalan, iftaraKalan

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False
run_with_ngrok(app)

hata = {
    'HATALI İSTEK!' : 'Aradığınız içerik mevcut değil. Lütfen isteğinizi kontrol edin.',
    'korona': '/korona',
    'hurriyetEmlak': {
        'istek > /dizin': '/hurriyetEmlak/Çanakkale/Merkez',
        'istek > ?argüman': '/hurriyetEmlak?il=Çanakkale&ilce=Merkez'
    },
    'nobetciEczane': {
        'istek > /dizin': '/nobetciEczane/Çanakkale/Merkez',
        'istek > ?argüman': '/nobetciEczane?il=Çanakkale&ilce=Merkez'
    },
    'vakitler': {
        'sahuraKalan': {
            'istek > /dizin' : '/sahuraKalan/Çanakkale',
            'istek > ?argüman' : '/sahuraKalan?il=Çanakkale'
        },
        'iftaraKalan': {
            'istek > /dizin': '/iftaraKalan/Çanakkale',
            'istek > ?argüman': '/iftaraKalan?il=Çanakkale'
        }
    }
}

@app.route('/korona', methods=['GET'])
def korona():
    return jsonify(koronaSpatula())

@app.route('/hurriyetEmlak', methods=['GET'])
def hurriyetEmlakArg():
    il = request.args.get('il')
    ilce = request.args.get('ilce')

    if not il or not ilce:
        return jsonify(hata)

    if hurriyetSpatula(il, ilce):
        return jsonify(KekikAPI=hurriyetSpatula(il, ilce))
    else:
        return jsonify(KekikAPI="jajajaja")

@app.route('/hurriyetEmlak/<il>/<ilce>', methods=['GET'])
def hurriyetEmlakDizin(il, ilce):
    if not il or not ilce:
        return jsonify(hata)

    if hurriyetSpatula(il, ilce):
        return jsonify(KekikAPI=hurriyetSpatula(il, ilce))
    else:
        return jsonify(KekikAPI="jajajaja")

@app.route('/nobetciEczane', methods=['GET'])
def nobetciEczaneArg():
    il = request.args.get('il')
    ilce = request.args.get('ilce')

    if not il or not ilce:
        return jsonify(hata)

    if nobetciSpatula(il, ilce):
        return jsonify(KekikAPI=nobetciSpatula(il, ilce))
    else:
        return jsonify(KekikAPI="jajajaja")

@app.route('/nobetciEczane/<il>/<ilce>', methods=['GET'])
def nobetciEczaneDizin(il, ilce):
    if not il or not ilce:
        return jsonify(hata)

    if nobetciSpatula(il, ilce):
        return jsonify(KekikAPI=nobetciSpatula(il, ilce))
    else:
        return jsonify(KekikAPI="jajajaja")

@app.route('/sahuraKalan', methods=['GET'])
def sahurArg():
    il = request.args.get('il')

    if not il:
        return jsonify(hata)

    if sahuraKalan(il):
        return jsonify(sahuraKalan=sahuraKalan(il), sunucuZamani=strftime('%d/%m %H:%M:%S'))
    else:
        return jsonify(sahuraKalan="jajajaja", sunucuZamani=strftime('%d/%m %H:%M:%S'))

@app.route('/sahuraKalan/<il>', methods=['GET'])
def sahurDizin(il):
    if not il:
        return jsonify(hata)

    if sahuraKalan(il):
        return jsonify(sahuraKalan=sahuraKalan(il), sunucuZamani=strftime('%d/%m %H:%M:%S'))
    else:
        return jsonify(sahuraKalan="jajajaja", sunucuZamani=strftime('%d/%m %H:%M:%S'))

@app.route('/iftaraKalan', methods=['GET'])
def iftarArg():
    il = request.args.get('il')

    if not il:
        return jsonify(hata)

    if sahuraKalan(il):
        return jsonify(iftaraKalan=iftaraKalan(il), sunucuZamani=strftime('%d/%m %H:%M:%S'))
    else:
        return jsonify(iftaraKalan="jajajaja")

@app.route('/iftaraKalan/<il>', methods=['GET'])
def iftarDizin(il):
    if not il:
        return jsonify(hata)

    if sahuraKalan(il):
        return jsonify(iftaraKalan=iftaraKalan(il), sunucuZamani=strftime('%d/%m %H:%M:%S'))
    else:
        return jsonify(iftaraKalan="jajajaja")

@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_from_directory(directory=app.root_path, filename='favicon.ico', mimetype='image/x-icon')

@app.errorhandler(404)
def dortYuzDort(error):
    return make_response(jsonify(hata), 404)

@app.errorhandler(500)
def besYuz(error):
    return make_response(jsonify(KekikAPI="jajajaja", hata=hata), 500)

if __name__ == '__main__':
    app.run()