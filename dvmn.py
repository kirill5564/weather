import requests


if __name__ == '__main__':
    url_london = 'https://wttr.in/london?nTqu&lang=en'
    response = requests.get(url_london)
    response.raise_for_status()
    print(response.text)
    url_sheremetyevo = 'https://wttr.in/svo?nTqu&lang=en'
    response = requests.get(url_sheremetyevo)
    response.raise_for_status()
    print(response.text)
    url_сherepovets = 'https://wttr.in/Череповец?nTqM&lang=ru'
    response = requests.get(url_сherepovets)
    response.raise_for_status()
    print(response.text)