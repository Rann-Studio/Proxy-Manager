import requests
import random
from bs4 import BeautifulSoup


class ProxyManager:
    def __init__(self):
        self.proxies = []

    def setup(self, protocol=None):
        response = requests.get('https://free-proxy-list.net/')
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table')
        rows = table.find_all('tr')

        proxy_list = []
        for row in rows[1:]:
            columns = row.find_all('td')
            ip = columns[0].text
            port = columns[1].text
            anonymity = columns[4].text
            proxy_protocol = 'https' if columns[6].text.lower() == 'yes' else 'http'
            proxy_url = f'{proxy_protocol}://{ip}:{port}'

            proxy_info = {
                'ip': ip,
                'port': port,
                'anonymity': anonymity,
                'protocol': proxy_protocol,
                'proxy_url': proxy_url
            }

            if not protocol or proxy_protocol == protocol:
                proxy_list.append(proxy_info)

        self.proxies = proxy_list

    def check_proxy(self, proxy_url, timeout=5):
        protocol = proxy_url.split(':')[0]
        proxy = {protocol: proxy_url}

        try:
            response = requests.get('https://www.google.com', proxies=proxy, timeout=timeout)
            if response.status_code == 200:
                return True
        except (requests.ConnectionError, requests.Timeout):
            pass

        return False

    def get_proxies(self):
        return self.proxies

    def get_proxy(self):
        random_proxy = [proxy for proxy in self.proxies]
        return random.choice(random_proxy)
