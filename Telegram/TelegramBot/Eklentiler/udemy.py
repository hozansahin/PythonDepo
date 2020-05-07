#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @BetikSonu için yazılmıştır.

from pyrogram import Client, Filters
from time import strftime
import json
from Kaziyicilar.discUdemy import TR, EN

@Client.on_message(Filters.command(['udemy'],['!','.','/']))
def udemy(client, message):
    cevaplanan_mesaj = message.reply_to_message
    if cevaplanan_mesaj is None:
        kekik = message.reply("Bekleyin..")
    else:
        kekik = message.reply("Bekleyin..", reply_to_message_id=cevaplanan_mesaj.message_id)
    
    girilen_yazi = message.text                                         # komut ile birlikle mesajı tut
    if len(girilen_yazi.split()) == 1:                                  # eğer sadece komut varsa
        kekik.edit("`TR` veya `EN` belirtmeniz gerekir.")
        return
    
    dil = " ".join(girilen_yazi.split()[1:2]).lower()                   # dil'i komuttan ayrıştır (birinci kelime)
    
    if str(dil) == "tr":
        mesaj = f"Taranan Adres : `discudemy.com/language/Turkish/1`\n\n"

        try:
            veri = json.load(open("Kaziyicilar/jsonDosyalari/Udemy/TR.json", "r+", encoding='utf8'))
        except FileNotFoundError:
            print("\tTR.json | Dosya Bulunamadı!")
            raise

        for bilgi in veri['udemyTR']:
            mesaj += f"📼 [{bilgi['kurs_adi']}]({bilgi['kurs_linki']})\n"
        mesaj += f"\n\tGüncellenme Zamanı : `{veri['sunucu_saat']}`"

    elif str(dil) == "en":
        mesaj = f"Taranan Adres : `discudemy.com/language/English/1`\n\n"
        
        try:
            veri = json.load(open("Kaziyicilar/jsonDosyalari/Udemy/EN.json", "r+", encoding='utf8'))
        except FileNotFoundError:
            print("\tEN.json | Dosya Bulunamadı!")
            raise

        for bilgi in veri['udemyEN']:
            mesaj += f"📼 [{bilgi['kurs_adi']}]({bilgi['kurs_linki']})\n"
        mesaj += f"\n\tGüncellenme Zamanı : `{veri['sunucu_saat']}`"

    elif str(dil) == "update":
        kekik.edit('**Udemy Kupon Listesini Güncelliyorum...**\n\n\t__Bu işlem biraz uzun sürebilir.__')
        TR(1); EN(1)
        kekik.edit(f'__Kupon Listesi Güncellendi :)__\n\n\t`{strftime("%d/%m %H:%M:%S")}`')
        return
    
    else: mesaj = "`TR` veya `EN` belirtmeniz gerekir.!"

    try:
        kekik.edit(mesaj, disable_web_page_preview=True, parse_mode="Markdown")
    except Exception as hata_mesaji:
        kekik.edit(hata_mesaji)