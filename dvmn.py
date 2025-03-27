import requests


if __name__ == '__main__':
    urls = ['https://wttr.in/london',
           'https://wttr.in/svo',
           'https://wttr.in/Череповец']
    for url in urls:
        payload = {"nTqM": "", "lang": "ru"}
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)
