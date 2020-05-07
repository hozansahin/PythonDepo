#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @BetikSonu için yazılmıştır.

import requests
from bs4 import BeautifulSoup
import json

def hurriyetSpatula(il, ilce):
    url = f'https://www.hurriyetemlak.com/{il}-kiralik?counties={ilce}'
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    istek = requests.get(url, kimlik)
    corba = BeautifulSoup(istek.text, 'lxml')

    sozluk = {"hurriyetEmlak": []}

    for ilanlar in corba.findAll('div', class_='list'):

        link = ilanlar.findAll('div', class_='links')
        #print('Link :', 'https://www.hurriyetemlak.com' + link[0].a['href'])

        fiyat = ilanlar.findAll('div', class_='list-view-price')
        #print('Fiyat : ', fiyat[0].text.strip())

        ilanTarihi = ilanlar.findAll('div', class_='list-view-date')
        #print('Tarih : ', ilanTarihi[0].text.strip())

        odaSayisi = ilanlar.findAll('span', class_='celly houseRoomCount')
        #print('Oda Sayısı : ', odaSayisi[0].text.strip())

        ebat = ilanlar.findAll('span', class_='celly squareMeter list-view-size')
        #print('MereKare : ', ebat[0].text.strip())

        yas = ilanlar.findAll('span', class_='celly buildingAge')
        #print('Yaş : ', yas[0].text.strip())

        kat = ilanlar.findAll('span', class_='celly floortype')
        #print('Kat : ', kat[0].text.strip())

        aciklama = ilanlar.findAll('div', class_='list-view-header')
        #print('Açıklama : ', aciklama[0].text.strip())

        ilanNo = ilanlar.findAll('span', class_='phone-listing-id')
        #print('İlan Numarası : ', ilanNo[0].text.split(':')[1].strip())

        ilgiliAd = ilanlar.findAll('span', class_='phone-consultant-name')
        #print('İlgili Adı : ', ilgiliAd[0].text.strip())

        ilgiliNo = ilanlar.findAll('ul', class_='list-phone-numbers')
        #print('İlgili No : ', ilgiliNo[0].text.strip().replace('\n','').replace(' ',''))

        konum = ilanlar.findAll('div', class_='list-view-location')
        #print('Konum : ', konum[0].text.strip())

        for say in range(len(ilanNo)):
            try:
                sozluk["hurriyetEmlak"].append({
                    "id": say,
                    "ilanLinki": 'https://www.hurriyetemlak.com' + link[say].a['href'],
                    "ilanNo": ilanNo[say].text.split(':')[1].strip(),
                    "ilanDetay": aciklama[say].text.strip(),
                    "ilanKonum": konum[say].text.strip(),
                    "ilanFiyati": fiyat[say].text.strip(),
                    "ilanTarihi": ilanTarihi[say].text.strip(),
                    "odaSayisi": odaSayisi[say].text.strip(),
                    "metreKare": ebat[say].text.strip(),
                    "binaYasi": yas[say].text.strip(),
                    "bulunduguKat": kat[say].text.strip(),
                    "ilgiliAdi": ilgiliAd[say].text.strip(),
                    "ilgiliNo": ilgiliNo[say].text.strip().replace('\n','').replace(' ','')[:11]
                })
            except:
                continue        # örneğin ilan'da "Bulunduğu Kat" bilgisi yoksa o ilanı kaydetme

    jsonEmlak = json.dumps(sozluk, indent=2, sort_keys=False, ensure_ascii=False)
    with open(f'Kaziyicilar/jsonDosyalari/Emlak/{il}-{ilce}.json', "w+", encoding='utf8') as dosya: dosya.write(jsonEmlak)

    return jsonEmlak

#print(hurriyetSpatula('canakkale', 'merkez'))