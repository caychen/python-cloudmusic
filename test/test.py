import requests

from common.Constant import headers, song_detail_url
from encrypt.Encrypt import encrypted_request

if __name__ == '__main__':
    session = requests.session()

    req_text = {
        'ids': [25643258]
    }

    data = encrypted_request(req_text)
    response = session.post(song_detail_url, data=data, headers=headers)
    response.encoding = 'UTF-8'
    r = response.json()

    print(r)
