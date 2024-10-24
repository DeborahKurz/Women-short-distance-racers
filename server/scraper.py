from bs4 import BeautifulSoup
import requests

headers = {'use-agent':'my-app/0.0.1'}

#100m dash athlete information
html_100m = requests.get("https://worldathletics.org/world-rankings/100m/women?regionType=countries&region=usa&page=1&rankDate=2023-10-03", headers=headers)

doc_100m = BeautifulSoup(html_100m.text, 'html.parser')

athletes_100m_raw = doc_100m.select('.table-row--hover')[:5]
athletes_100m_data = []

for athlete in athletes_100m_raw:
    rank = athlete.select_one('td[data-th="Rank"]').get_text(strip=True)
    name = athlete.select_one('td[data-th="Competitor"]').get_text(strip=True)
    dob = athlete.select_one('td[data-th="DOB"]').get_text(strip=True)
    
    athlete_info = {
        'Rank': rank,
        'Name': name,
        'DOB': dob
    }
    
    athletes_100m_data.append(athlete_info)

#200m dash athlete information
html_200m = requests.get("https://worldathletics.org/world-rankings/200m/women?regionType=countries&region=usa&page=1&rankDate=2023-10-03", headers=headers)

doc_200m = BeautifulSoup(html_200m.text, 'html.parser')
athletes_200m_raw = doc_200m.select('.table-row--hover')[:5]
athletes_200m_data = []

for athlete in athletes_200m_raw:
    rank = athlete.select_one('td[data-th="Rank"]').get_text(strip=True)
    name = athlete.select_one('td[data-th="Competitor"]').get_text(strip=True)
    dob = athlete.select_one('td[data-th="DOB"]').get_text(strip=True)

    athlete_info = {
        'Rank': rank,
        'Name': name,
        'DOB': dob
    }

    athletes_200m_data.append(athlete_info)

#400m dash athlete information
html_400m = requests.get("https://worldathletics.org/world-rankings/400m/women?regionType=countries&region=usa&page=1&rankDate=2023-10-03", headers=headers)

doc_400m = BeautifulSoup(html_400m.text, 'html.parser')
athletes_400m_raw = doc_400m.select('.table-row--hover')[:5]
athletes_400m_data = []

for athlete in athletes_400m_raw:
    rank = athlete.select_one('td[data-th="Rank"]').get_text(strip=True)
    name = athlete.select_one('td[data-th="Competitor"]').get_text(strip=True)
    dob = athlete.select_one('td[data-th="DOB"]').get_text(strip=True)

    athlete_info = {
        'Rank': rank,
        'Name': name,
        'DOB': dob
    }

    athletes_400m_data.append(athlete_info)


#800m dash athlete information
html_800m = requests.get("https://worldathletics.org/world-rankings/800m/women?regionType=countries&region=usa&page=1&rankDate=2023-10-03", headers=headers)

doc_800m = BeautifulSoup(html_800m.text, 'html.parser')
athletes_800m_raw = doc_800m.select('.table-row--hover')[:5]
athletes_800m_data = []

for athlete in athletes_800m_raw:
    rank = athlete.select_one('td[data-th="Rank"]').get_text(strip=True)
    name = athlete.select_one('td[data-th="Competitor"]').get_text(strip=True)
    dob = athlete.select_one('td[data-th="DOB"]').get_text(strip=True)

    athlete_info = {
        'Rank': rank,
        'Name': name,
        'DOB': dob
    }

    athletes_800m_data.append(athlete_info)

breakpoint()