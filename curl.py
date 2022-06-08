import json
import requests
from types import SimpleNamespace

class Curl:
    cookies = {
        'popup_news_994151': '1',
        'msg-cep-invalido-994151': '1',
        '_fbp': 'fb.2.1654368262626.265639829',
        '_ga': 'GA1.3.5276339.1654368263',
        '_gid': 'GA1.3.88310297.1654368263',
        '__zlcmid': '1AJkybheDN0Pecw',
        'csrftoken': 'GlLMyALADcpgbDoYyJHi2InEnudTDnbVOGjxk6zWkym66YIrPNNpotE60xCs71ET',
        'sessionid': '33jzm9sy0xgvlfl9qimcejynh5dlp9ir',
        '_gcl_au': '1.1.1292545876.1654368400',
        '_pin_unauth': 'dWlkPU1ESTVaR1V4WVRZdFlXVTFNeTAwT1dZNExUbGxaRE10WkdNMVpqUmpPV05pT0RrMg',
        '_pin_unauth': 'dWlkPU1ESTVaR1V4WVRZdFlXVTFNeTAwT1dZNExUbGxaRE10WkdNMVpqUmpPV05pT0RrMg',
        '_hjSessionUser_218777': 'eyJpZCI6ImZhNDVmMDBmLTVkNTMtNTgyYy1iYzljLTc4MzljZDhlMDkyOCIsImNyZWF0ZWQiOjE2NTQzNjg0MDUwNTgsImV4aXN0aW5nIjp0cnVlfQ==',
        'panoramaId_expiry': '1654455290600',
        '_hjIncludedInSessionSample': '0',
        '_hjSession_218777': 'eyJpZCI6ImJjZTg1NjFmLTZkOGEtNDA5NC05Y2I5LWRhZWM4MjRmNDNlOCIsImNyZWF0ZWQiOjE2NTQzOTMzOTUxMjYsImluU2FtcGxlIjpmYWxzZX0=',
        'outbrain_cid_fetch': 'true',
        '_gat': '1',
        'shopper_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjdXN0b21lcklkIjo5OTQxNTEsImRldmljZVVVSUQiOiI1NmIxYTE2YS02MmI3LTQ2NTUtOTI2Yy05YWMxZTQwMWUxYTUiLCJpYXQiOjE2NTQzODI4NTd9.kFGh7znjtL8fn-9NKb9T96dhnd9F0Ga-svdLGYQ6L9k',
        'shopper_current_store': '1',
        'current_delivery_address': '[{%22store_id%22:1%2C%22cluster_id%22:1%2C%22address_id%22:1009202}]',
        'AWSALBTG': '6NgZx6CSbbAN7e0CKe1KXQwpL9cNVhWyZ8NH3LlLfoDs8QR0+Pc69gx3Mx9FXw9Sx2//EAgJ3QzmhShYc6RWKx8gxJO/XsxGFwFgpvwGuBB1jmmMYai8066Sve0GmHtz8KlcCUyS3Ol3gVnjP2kdx0Dl/a2dbPJZbim2txwA5vwY9FOZI1o=',
        'AWSALBTGCORS': '6NgZx6CSbbAN7e0CKe1KXQwpL9cNVhWyZ8NH3LlLfoDs8QR0+Pc69gx3Mx9FXw9Sx2//EAgJ3QzmhShYc6RWKx8gxJO/XsxGFwFgpvwGuBB1jmmMYai8066Sve0GmHtz8KlcCUyS3Ol3gVnjP2kdx0Dl/a2dbPJZbim2txwA5vwY9FOZI1o=',
    }

    headers = {
        'authority': 'programada.shopper.com.br',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjdXN0b21lcklkIjo5OTQxNTEsImRldmljZVVVSUQiOiI1NmIxYTE2YS02MmI3LTQ2NTUtOTI2Yy05YWMxZTQwMWUxYTUiLCJpYXQiOjE2NTQzODI4NTd9.kFGh7znjtL8fn-9NKb9T96dhnd9F0Ga-svdLGYQ6L9k',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        'cookie': 'popup_news_994151=1; msg-cep-invalido-994151=1; _fbp=fb.2.1654368262626.265639829; _ga=GA1.3.5276339.1654368263; _gid=GA1.3.88310297.1654368263; __zlcmid=1AJkybheDN0Pecw; csrftoken=GlLMyALADcpgbDoYyJHi2InEnudTDnbVOGjxk6zWkym66YIrPNNpotE60xCs71ET; sessionid=33jzm9sy0xgvlfl9qimcejynh5dlp9ir; _gcl_au=1.1.1292545876.1654368400; _pin_unauth=dWlkPU1ESTVaR1V4WVRZdFlXVTFNeTAwT1dZNExUbGxaRE10WkdNMVpqUmpPV05pT0RrMg; _pin_unauth=dWlkPU1ESTVaR1V4WVRZdFlXVTFNeTAwT1dZNExUbGxaRE10WkdNMVpqUmpPV05pT0RrMg; _hjSessionUser_218777=eyJpZCI6ImZhNDVmMDBmLTVkNTMtNTgyYy1iYzljLTc4MzljZDhlMDkyOCIsImNyZWF0ZWQiOjE2NTQzNjg0MDUwNTgsImV4aXN0aW5nIjp0cnVlfQ==; panoramaId_expiry=1654455290600; _hjIncludedInSessionSample=0; _hjSession_218777=eyJpZCI6ImJjZTg1NjFmLTZkOGEtNDA5NC05Y2I5LWRhZWM4MjRmNDNlOCIsImNyZWF0ZWQiOjE2NTQzOTMzOTUxMjYsImluU2FtcGxlIjpmYWxzZX0=; outbrain_cid_fetch=true; _gat=1; shopper_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjdXN0b21lcklkIjo5OTQxNTEsImRldmljZVVVSUQiOiI1NmIxYTE2YS02MmI3LTQ2NTUtOTI2Yy05YWMxZTQwMWUxYTUiLCJpYXQiOjE2NTQzODI4NTd9.kFGh7znjtL8fn-9NKb9T96dhnd9F0Ga-svdLGYQ6L9k; shopper_current_store=1; current_delivery_address=[{%22store_id%22:1%2C%22cluster_id%22:1%2C%22address_id%22:1009202}]; AWSALBTG=6NgZx6CSbbAN7e0CKe1KXQwpL9cNVhWyZ8NH3LlLfoDs8QR0+Pc69gx3Mx9FXw9Sx2//EAgJ3QzmhShYc6RWKx8gxJO/XsxGFwFgpvwGuBB1jmmMYai8066Sve0GmHtz8KlcCUyS3Ol3gVnjP2kdx0Dl/a2dbPJZbim2txwA5vwY9FOZI1o=; AWSALBTGCORS=6NgZx6CSbbAN7e0CKe1KXQwpL9cNVhWyZ8NH3LlLfoDs8QR0+Pc69gx3Mx9FXw9Sx2//EAgJ3QzmhShYc6RWKx8gxJO/XsxGFwFgpvwGuBB1jmmMYai8066Sve0GmHtz8KlcCUyS3Ol3gVnjP2kdx0Dl/a2dbPJZbim2txwA5vwY9FOZI1o=',
        'dnt': '1',
        'referer': 'https://programada.shopper.com.br/shop-cn/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Microsoft Edge";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.30',
    }

    def shopper_request(self):
        response = requests.get('https://siteapi.shopper.com.br/catalog/departments/22',
                                cookies=self.cookies,
                                headers=self.headers)
        print(response.json())
        return response.text


    def parse(self, response):
        teste = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
        print(teste.subdepartments[0])

