#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @BetikSonu için yazılmıştır.

from pyrogram import Client, Filters
from time import time, sleep
from os import listdir

betikUserBot = Client(
    api_id=XXXXXX,                                  # my.telegram.org/apps
    api_hash="XXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXX",    # my.telegram.org/apps
    session_name = "@betikUserBot",                # Fark Etmez
    plugins=dict(root="Eklentiler")
)

@betikUserBot.on_message(Filters.me & Filters.command(['yardim'], ['!','.','/']))
def yardim_mesaji(client, message):
    message.edit("Bekleyin..")
    basla = time()
    message.edit("Aranıyor...")                                           # Mesajı Düzenle

    mesaj = f"""Merhaba, [{message.from_user.first_name}](tg://user?id={message.from_user.id})!\n
    Ben @BetikSonu'nda yaratıldım.\n
    Kaynak kodlarım [Burada](https://github.com/BetikSonu/BetikSonuRobot)
    Kullanabileceğim komutlar ise eklentilerimde gizli..\n\n"""

    mesaj += "Eklentilerim;\n"                                          # Mesaja Ekle
    for dosya in listdir("./Eklentiler/"):
        if not dosya.endswith(".py"): continue
        mesaj += f"📂 `{dosya.replace('.py','')}`\n"

    bitir = time()
    sure = bitir - basla
    mesaj += f"\nTepki Süresi : `{str(sure)[:4]} sn`"                   # Mesaja Ekle

    try:                                                                # Dene
        message.edit(mesaj, disable_web_page_preview=True, parse_mode="Markdown")
    except Exception as hata_mesaji:                                    # Başaramazsan
        message.edit(hata_mesaji)                                         # Hatayı Söyle

@betikUserBot.on_message(Filters.me & Filters.command(['eklenti'], ['!','.','/']))
def eklenti_gonder(client, message):
    message.edit("Bekleyin..")                          # Mesaj'ı Başlatıyoruz
    girilen_yazi = message.text                                 # komut ile birlikle mesajı tut

    if len(girilen_yazi.split()) == 1:                          # eğer sadece komut varsa
        message.edit("`DosyaAdı` Girmelisin!")                    # uyarı ver
        return                                                  # geri dön

    dosya = " ".join(girilen_yazi.split()[1:2])                 # dosyayı komuttan ayır (birinci kelime)

    if f"{dosya}.py" in listdir("Eklentiler"):
        message.delete()
        message.reply_document(f"./Eklentiler/{dosya}.py")
    else : message.edit('Dosya Bulunamadı!')

if __name__ == '__main__':
    betikUserBot.run()