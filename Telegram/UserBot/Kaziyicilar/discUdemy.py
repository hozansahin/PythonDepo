#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @BetikSonu için yazılmıştır.

import requests, re
from bs4 import BeautifulSoup
import json
from time import strftime

def TR(hangi_sayfa):
    udemy_baslik = []
    udemy_link = []

    link = f'https://www.discudemy.com/language/Turkish/{hangi_sayfa}'
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.97 (Edition Campaign 34)'}
    istek = requests.get(link)
    kaynak = BeautifulSoup(istek.text, 'lxml')

    for baslik in kaynak.findAll('a',{'class': 'card-header'}):
        baslik = baslik
        udemy_baslik.append(baslik.text)    # ~~

    for discudemy_linkler in kaynak.findAll('a', attrs={'href': re.compile("^https://www.discudemy.com/Turkish/")}):
        gelen_discudemy = discudemy_linkler['href']
        discudemy_go_html = requests.get(gelen_discudemy)
        discudemy_go_kaynak = BeautifulSoup(discudemy_go_html.text, 'lxml')

        for discudemy_go_linkler in discudemy_go_kaynak.findAll('a', attrs={'href': re.compile("^https://www.discudemy.com/go/")}):
            gelen_discudemy_go = discudemy_go_linkler['href']
            udemy_html = requests.get(gelen_discudemy_go)
            udemy_kaynak = BeautifulSoup(udemy_html.text, 'lxml')

            for udemy_linkler in udemy_kaynak.findAll('a', attrs={'href': re.compile("^https://www.udemy.com/")}):
                gelen_udemy = udemy_linkler['href']
                udemy_link.append(gelen_udemy)  # ~~

    sozluk = {"udemyTR": [], "sunucu_saat": strftime('%d/%m %H:%M:%S')}
    for adet in range(0, len(udemy_baslik)):
        sozluk["udemyTR"].append({
            "kurs_adi": udemy_baslik[adet],
            "kurs_linki": udemy_link[adet]
        })

    jsonUdemyTR = json.dumps(sozluk, indent=2, sort_keys=False, ensure_ascii=False)
    with open(f'Kaziyicilar/jsonDosyalari/Udemy/TR.json', "w+", encoding='utf8') as dosya: dosya.write(jsonUdemyTR)
    return jsonUdemyTR

def EN(hangi_sayfa):
    udemy_baslik = []
    udemy_link = []

    link = f'https://www.discudemy.com/language/English/{hangi_sayfa}'
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.97 (Edition Campaign 34)'}
    istek = requests.get(link)
    kaynak = BeautifulSoup(istek.text, 'lxml')

    for baslik in kaynak.findAll('a',{'class': 'card-header'}):
        baslik = baslik
        udemy_baslik.append(baslik.text)    # ~~

    for discudemy_linkler in kaynak.findAll('a', attrs={'href': re.compile("^https://www.discudemy.com/English/")}):
        gelen_discudemy = discudemy_linkler['href']
        discudemy_go_html = requests.get(gelen_discudemy)
        discudemy_go_kaynak = BeautifulSoup(discudemy_go_html.text, 'lxml')

        for discudemy_go_linkler in discudemy_go_kaynak.findAll('a', attrs={'href': re.compile("^https://www.discudemy.com/go/")}):
            gelen_discudemy_go = discudemy_go_linkler['href']
            udemy_html = requests.get(gelen_discudemy_go)
            udemy_kaynak = BeautifulSoup(udemy_html.text, 'lxml')

            for udemy_linkler in udemy_kaynak.findAll('a', attrs={'href': re.compile("^https://www.udemy.com/")}):
                gelen_udemy = udemy_linkler['href']
                udemy_link.append(gelen_udemy)  # ~~

    sozluk = {"udemyEN": [], "sunucu_saat": strftime('%d/%m %H:%M:%S')}
    for adet in range(0, len(udemy_baslik)):
        sozluk["udemyEN"].append({
            "kurs_adi": udemy_baslik[adet],
            "kurs_linki": udemy_link[adet]
        })

    jsonUdemyEN = json.dumps(sozluk, indent=2, sort_keys=False, ensure_ascii=False)
    with open(f'Kaziyicilar/jsonDosyalari/Udemy/EN.json', "w+", encoding='utf8') as dosya: dosya.write(jsonUdemyEN)
    return jsonUdemyEN