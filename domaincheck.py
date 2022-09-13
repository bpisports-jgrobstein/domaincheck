import requests, whois
from requests_html import HTMLSession

session = HTMLSession()

with open('myDomains.csv', 'r') as domains:
    names = domains.read().split('\n')
    for domain in names:
        whois_info = whois.whois(domain)
        if isinstance(whois_info.expiration_date, list):
            exp = str(whois_info.expiration_date[1])
        else:
            exp = str(whois_info.expiration_date)
        reg = str(whois_info.registrar)
        try:
            res = session.get("http://" + domain)
            if res.html.find('title', first=True):
                title =  res.html.find('title', first=True).text
            else:
                title= ""
            print(domain + ";" + str(res.status_code) + ";" + title + ";" + exp + ";" + reg)
        except requests.ConnectionError:
            print(domain + ";Failed to connect" + ";Connection Error;" + exp + ";" + reg)
        except requests.exceptions.InvalidURL:
            print(domain + ";Invalid URL" + ";Unreachable;" + exp + ";" + reg)