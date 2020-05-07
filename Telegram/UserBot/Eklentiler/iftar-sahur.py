#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @BetikSonu için yazılmıştır.

from Kaziyicilar.iftarSaati import sahuraKalan, iftaraKalan

from pyrogram import Client, Filters

@Client.on_message(Filters.command(['iftar'],['!','.','/']))
def iftar(client, message):
    kekik = message.edit("Bekleyin..")

    girilen_yazi = message.text
    if len(girilen_yazi.split()) == 1:
        kekik.edit("Arama yapabilmek için `il` girmelisiniz")
        return

    il = " ".join(girilen_yazi.split()[1:2]).lower().capitalize().replace('I', 'İ')
    mesaj = f'**{il}** __ili için__ '

    try:
        mesaj += iftaraKalan(il)
    except:
        kekik.edit('Bulunamadı..')
        return

    try:
        kekik.edit(mesaj, disable_web_page_preview=True, parse_mode="Markdown")
    except Exception as hata_mesaji:
        kekik.edit(hata_mesaji)

@Client.on_message(Filters.command(['sahur'],['!','.','/']))
def sahur(client, message):
    kekik = message.edit("Bekleyin..")

    girilen_yazi = message.text
    if len(girilen_yazi.split()) == 1:
        kekik.edit("Arama yapabilmek için `il` girmelisiniz")
        return

    il = " ".join(girilen_yazi.split()[1:2]).lower().capitalize().replace('I', 'İ')
    mesaj = f'**{il}** __ili için__ '

    try:
        mesaj += sahuraKalan(il)
    except:
        kekik.edit('Bulunamadı..')
        return

    try:
        kekik.edit(mesaj, disable_web_page_preview=True, parse_mode="Markdown")
    except Exception as hata_mesaji:
        kekik.edit(hata_mesaji)