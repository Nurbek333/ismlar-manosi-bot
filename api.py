from bs4 import BeautifulSoup
import requests 



# Ism ma'lumotlarini olish funksiyasi
def ism_manosi_funksiyasi(ism):
    url = f"https://ismlar.com/uz/name/{ism}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTP xatoliklarini tekshirish
        
        soup = BeautifulSoup(response.content, 'html.parser')
        natija_div = soup.find("div", attrs={"class": "space-y-4"})
        
        if natija_div and natija_div.p:
            natija_text = natija_div.p.text.strip()
        else:
            natija_text = "Ma'lumot topilmadi"
        
    except requests.exceptions.RequestException as e:
        natija_text = "So'rovda xatolik yuz berdi."
    
    return natija_text