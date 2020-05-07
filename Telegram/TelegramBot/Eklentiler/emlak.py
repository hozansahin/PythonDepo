#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @BetikSonu için yazılmıştır.

from Kaziyicilar.hurriyetEmlak import hurriyetSpatula

from pyrogram import Client, Filters
from os import remove
import json

@Client.on_message(Filters.command(['emlak'],['!','.','/']))
def emlak(client, message):
    cevaplanan_mesaj = message.reply_to_message
    if cevaplanan_mesaj is None:
        kekik = message.reply("Bekleyin..")
    else:
        kekik = message.reply("Bekleyin..", reply_to_message_id=cevaplanan_mesaj.message_id)

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
    mesaj = f"Aranan : `{il}` / `{ilce}`\n"

    try:
        hurriyetSpatula(il, ilce)
        with open(f'Kaziyicilar/jsonDosyalari/Emlak/{il}-{ilce}.json', 'r+', encoding='utf-8') as dosya:
            jsonVerisi = json.load(dosya)
    except:
        jsonVerisi = json.loads(hurriyetSpatula(il, ilce))

    if jsonVerisi['hurriyetEmlak']:
        sayac = 1
        for bilgi in jsonVerisi['hurriyetEmlak']:
            mesaj += (f"""\n🏘 [{bilgi['ilanDetay']}]({bilgi['ilanLinki']})
                `{bilgi['ilanFiyati']}` | __{bilgi['ilanKonum']}__
                **{bilgi['odaSayisi']}** | **{bilgi['metreKare']}** | __{bilgi['binaYasi']}__ | __{bilgi['bulunduguKat']}__\n""")
            sayac += 1
            if sayac == 4: break
        try:
            message.reply_document(f'Kaziyicilar/jsonDosyalari/Emlak/{il}-{ilce}.json')
            remove(f'Kaziyicilar/jsonDosyalari/Emlak/{il}-{ilce}.json')
        except:
            pass
    else:
        kekik.edit("Veri Bulunamadı..")
        remove(f'Kaziyicilar/jsonDosyalari/Emlak/{il}-{ilce}.json')
        return

    try:
        kekik.edit(mesaj, disable_web_page_preview=True, parse_mode="Markdown")
    except Exception as hata_mesaji:
        kekik.edit(hata_mesaji)