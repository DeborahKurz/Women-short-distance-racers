from bs4 import BeautifulSoup
import requests

headers = {'use-agent':'my-app/0.0.1'}
html = requests.get("https://worldathletics.org/world-rankings/100m/women?regionType=countries&region=usa&page=1&rankDate=2023-10-03", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')

breakpoint()