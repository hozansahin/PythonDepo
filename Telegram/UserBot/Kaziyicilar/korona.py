#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @BetikSonu için yazılmıştır.

import requests
from bs4 import BeautifulSoup
import json
from time import strftime

def koronaSpatula():
    url = f"https://www.worldometers.info/coronavirus/"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    istek = requests.get(url, kimlik)
    soup = BeautifulSoup(istek.text, "lxml")

    sozluk = {"koronaVerileri": [], "sunucu_saat": strftime('%d/%m %H:%M:%S')}

    dunya = soup.select("#maincounter-wrap > div")
    dunyaVaka = dunya[0].text.strip()
    dunyaOlu = dunya[1].text.strip()
    dunyaKurtulan = dunya[2].text.strip()

    turkiye = soup.select("#main_table_countries_today > tbody:nth-child(2) > tr:nth-child(15)")
    turkiye = turkiye[0].text.split()
    trVaka = turkiye[1]
    trOlu = turkiye[3]
    trKurtulan = turkiye[5]

    sozluk["koronaVerileri"].append({
        "vakaSayisi": {"TR": trVaka, "dunyaGeneli": dunyaVaka},
        "oluSayisi": {"TR": trOlu, "dunyaGeneli": dunyaOlu},
        "iyilesmeSayisi": {"TR": trKurtulan, "dunyaGeneli": dunyaKurtulan}
    })

    jsonKorona = json.dumps(sozluk, indent=2, sort_keys=False, ensure_ascii=False)
    with open(f'Kaziyicilar/jsonDosyalari/Korona/korona.json', "w+", encoding='utf8') as dosya: dosya.write(jsonKorona)

    return jsonKorona

#print(koronaSpatula())