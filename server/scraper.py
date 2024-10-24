from bs4 import BeautifulSoup
import requests

def athletes(race_distance):
    url = f"https://worldathletics.org/world-rankings/{race_distance}/women?regionType=countries&region=usa&page=1&rank"
    headers = {'use-agent':'my-app/0.0.1'}

    html = requests.get(url, headers = headers)

    doc = BeautifulSoup(html.text, 'html.parser')

    athletes_raw = doc.select('.table-row--hover')[:5]
    athletes_data = []

    for athlete in athletes_raw:
        rank = athlete.select_one('td[data-th="Rank"]').get_text(strip=True)
        name = athlete.select_one('td[data-th="Competitor"]').get_text(strip=True)
        dob = athlete.select_one('td[data-th="DOB"]').get_text(strip=True)

        athlete_info = {
        'Rank': rank,
        'Name': name,
        'DOB': dob
        }
    
        athletes_data.append(athlete_info)

    return athletes_data


athletes_100m_data = athletes('100m')
athletes_200m_data = athletes('200m')
athletes_400m_data = athletes('400m')
athletes_800m_data = athletes('8000m')


breakpoint()