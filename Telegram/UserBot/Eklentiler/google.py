#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @BetikSonu için yazılmıştır.

from pyrogram import Client, Filters
from time import time, sleep
from google_search_client.search_client import GoogleSearchClient
import ast

@Client.on_message(Filters.command(['google'], ['!','.','/']))
def google(client, message):
    kekik = message.edit("Bekleyin..")
    
    girilen_yazi = message.text
    if len(girilen_yazi.split()) == 1:
        kekik.edit("Arama yapabilmek için kelime girmelisiniz..")
        return
    kekik.edit("Aranıyor...")
    
    basla = time()
    girdi = " ".join(girilen_yazi.split()[1:])
    mesaj = f"Aranan Kelime : `{girdi}`\n\n"
    
    istek = GoogleSearchClient()
    sonuclar = istek.search(girdi).to_json()
    
    if sonuclar:
        i = 1
        for sonuc in ast.literal_eval(sonuclar):
            mesaj += f"🔍 [{sonuc['title']}]({sonuc['url']})\n"
            i += 1
            if i == 5:
                break
        
        bitir = time()
        sure = bitir - basla
        mesaj += f"\nTepki Süresi : `{str(sure)[:4]} sn`"
        
        try:
            kekik.edit(mesaj, disable_web_page_preview=True, parse_mode="Markdown")
        except Exception as hata:
            kekik.edit(hata)
    else:
        kekik.edit("Hatalı bişeyler var, daha sonra tekrar deneyin..")