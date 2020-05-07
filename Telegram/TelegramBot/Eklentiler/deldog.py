#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @BetikSonu için yazılmıştır.

from pyrogram import Client, Filters
from time import time, sleep
import requests

@Client.on_message(Filters.command(['deldog'], ['!','.','/']))
def deldog(client, message):
    kekik = message.reply("Bekleyin..")

    deldog = "https://del.dog"
    
    cevaplanan_mesaj = message.reply_to_message
    if cevaplanan_mesaj is None:
        kekik.edit('Mesaj Yanıtlaman Gerekli!')
        return
    kekik.delete()

    sonuc = requests.post(f"{deldog}/documents", data=cevaplanan_mesaj.text.encode("utf-8")).json()

    message.reply(f'{deldog}/{sonuc["key"]}.py',
                  disable_web_page_preview=True,
                  reply_to_message_id=cevaplanan_mesaj.message_id)