import requests
from bs4 import BeautifulSoup
import json

def nobetciSpatula(il, ilce):
    url = f"https://www.eczaneler.gen.tr/nobetci-{il}-{ilce}"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    istek = requests.get(url, kimlik)
    soup = BeautifulSoup(istek.text, "lxml")

    sozluk = {"nobetciEczaneler": []}

    for table in soup.findAll("table", {"class": "table table-striped mt-2"}):
        #print(table)
        #print(table.tr.text)
        eczane_adi = table.findAll("td", {"style": "width:20%"})
        eczane_adresi = table.findAll("td", {"style": "width:50%"})
        eczane_telefon = table.findAll("td", {"style": "width:30%"})

        for adet in range(len(eczane_adi)):
            sozluk["nobetciEczaneler"].append({"eczane_adi": eczane_adi[adet].text})
            sozluk["nobetciEczaneler"][adet]["eczane_adresi"] = eczane_adresi[adet].text
            sozluk["nobetciEczaneler"][adet]["eczane_telefon"] = eczane_telefon[adet].text

    jsonEczane = json.dumps(sozluk, indent=2, sort_keys=False, ensure_ascii=False)
    with open(f'Kaziyicilar/jsonDosyalari/Eczane/{il}-{ilce}.json', "w+", encoding='utf8') as dosya: dosya.write(jsonEczane)

    return jsonEczane

#print(nobetciSpatula('canakkale', 'merkez'))