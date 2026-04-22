import requests

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

f = open("texto.txt", "w", encoding="utf-8")

texto = "nuevo para el archivo"
f.write(texto)
f.close()