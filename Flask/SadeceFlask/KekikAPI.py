#!flask/bin/python
# -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from flask import Flask, jsonify, make_response, send_from_directory

from Kaziyicilar.korona import koronaSpatula
from Kaziyicilar.hurriyetEmlak import hurriyetSpatula
from Kaziyicilar.nobetciEczane import nobetciSpatula
from Kaziyicilar.iftarSaati import sahuraKalan, iftaraKalan

app = Flask(__name__)

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

@app.route('/', methods=['GET'])
def main():
    return jsonify(KekikAPI="Merhaba Dünya")

@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_from_directory(directory=app.root_path, filename='favicon.ico', mimetype='image/x-icon')

@app.errorhandler(404)
def dortYuzDort(error):
    return make_response(jsonify(KekikAPI="dortYuzDort", hata=hata), 404)

@app.errorhandler(500)
def besYuz(error):
    return make_response(jsonify(KekikAPI="besYuz", hata=hata), 500)


if __name__ == '__main__':
    app.config['JSON_SORT_KEYS'] = False
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True, host='0.0.0.0', port=5000)