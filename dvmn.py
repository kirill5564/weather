import requests


def main():
    locations = ['london', 'svo', 'Череповец']
    for location in locations:
        payload = {'nTqM': '', 'lang': 'ru'}
        response = requests.get('https://wttr.in/' + location, params=payload)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
