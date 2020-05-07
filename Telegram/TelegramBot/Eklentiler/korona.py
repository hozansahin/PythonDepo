#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @BetikSonu için yazılmıştır.

from Kaziyicilar.korona import koronaSpatula

from pyrogram import Client, Filters
from time import strftime
from os import remove
import json

@Client.on_message(Filters.command(['korona'],['!','.','/']))
def korona(client, message):
    cevaplanan_mesaj = message.reply_to_message
    if cevaplanan_mesaj is None:
        kekik = message.reply("Bekleyin..")
    else:
        kekik = message.reply("Bekleyin..", reply_to_message_id=cevaplanan_mesaj.message_id)

    girilen_yazi = message.text
    ilkMetin = " ".join(girilen_yazi.split()[1:2]).lower()

    if ilkMetin == 'update':
        kekik.edit('**Korona Verilerini Güncelliyorum...**\n\n\t__Bu işlem biraz uzun sürebilir.__')
        koronaSpatula()
        kekik.edit(f'__Korona Verileri Güncellendi__\n\n\t`{strftime("%d/%m %H:%M:%S")}`')
        return

    kekik.edit("Aranıyor...")

    mesaj = f"**Korona Verileri**\n"

    with open(f'Kaziyicilar/jsonDosyalari/Korona/korona.json', 'r+', encoding='utf-8') as dosya:
        jsonVerisi = json.load(dosya)

    if jsonVerisi['koronaVerileri'] == []:
        kekik.edit("Veri Bulunamadı..")
        return
    else:
        for bilgi in jsonVerisi['koronaVerileri']:
            mesaj += f"\n🌎`Dünya Geneli` ;\n__Vaka__: {bilgi['vakaSayisi']['dunyaGeneli']}\n__Ölü__: {bilgi['oluSayisi']['dunyaGeneli']}\nİyileşen__: {bilgi['iyilesmeSayisi']['dunyaGeneli']}\n"
            mesaj += f"\n🇹🇷`Türkiye` ;\n__Vaka__: {bilgi['vakaSayisi']['TR']}\n__Ölü__: {bilgi['oluSayisi']['TR']}\n__İyileşen__: {bilgi['iyilesmeSayisi']['TR']}\n"
        mesaj += f"\n\tGüncellenme Zamanı : `{jsonVerisi['sunucu_saat']}`"

    try:
        kekik.edit(mesaj, disable_web_page_preview=True, parse_mode="Markdown")
    except Exception as hata_mesaji:
        kekik.edit(hata_mesaji)