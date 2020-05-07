#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @BetikSonu için yazılmıştır.

from Kaziyicilar.nobetciEczane import nobetciSpatula

from pyrogram import Client, Filters
from os import remove
import json

@Client.on_message(Filters.command(['eczane'],['!','.','/']))
def eczane(client, message):
    kekik = message.edit("Bekleyin..")

    girilen_yazi = message.text
    if len(girilen_yazi.split()) == 1:
        kekik.edit("Arama yapabilmek için `il` ve `ilçe` girmelisiniz")
        return
    elif len(girilen_yazi.split()) == 2:
        kekik.edit("Arama yapabilmek için `ilçe` de girmelisiniz")
        return

    tr2eng = str.maketrans(" .,-*/+-ıİüÜöÖçÇşŞğĞ", "________iIuUoOcCsSgG")
    il = " ".join(girilen_yazi.split()[1:2]).translate(tr2eng)          # il'i komuttan ayrıştır (birinci kelime)
    ilce = " ".join(girilen_yazi.split()[2:3]).translate(tr2eng)        # ilçe'yi komuttan ayrıştır (ikinci kelime)
    mesaj = f"Aranan Nöbetçi Eczane : `{ilce}` / `{il}`\n"

    try:
        nobetciSpatula(il, ilce)
        with open(f'Kaziyicilar/jsonDosyalari/Eczane/{il}-{ilce}.json', 'r+', encoding='utf-8') as dosya:
            jsonVerisi = json.load(dosya)
    except:
        jsonVerisi = json.loads(nobetciSpatula(il, ilce))

    if jsonVerisi['nobetciEczaneler'] == []:
        kekik.edit("Veri Bulunamadı..")
        remove(f'Kaziyicilar/jsonDosyalari/Eczane/{il}-{ilce}.json')
        return
    else:
        for bilgi in jsonVerisi['nobetciEczaneler']:
            mesaj += (f"\n**{bilgi['eczane_adi']}**\n__{bilgi['eczane_adresi']}__\n`{bilgi['eczane_telefon']}`\n")
        remove(f'Kaziyicilar/jsonDosyalari/Eczane/{il}-{ilce}.json')

    try:
        kekik.edit(mesaj, disable_web_page_preview=True, parse_mode="Markdown")
    except Exception as hata_mesaji:
        kekik.edit(hata_mesaji)