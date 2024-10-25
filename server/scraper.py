from bs4 import BeautifulSoup
import requests
from config import db, app
from models import Athlete

def athletes(race_distance, distance):
    url = f"https://worldathletics.org/world-rankings/{race_distance}/women?regionType=countries&region=usa&page=1&rank"
    headers = {'user-agent':'my-app/0.0.1'}

    html = requests.get(url, headers = headers)

    doc = BeautifulSoup(html.text, 'html.parser')

    athletes_raw = doc.select('.table-row--hover')[:5]
    athletes_data = []

    for athlete in athletes_raw:
        rank = athlete.select_one('td[data-th="Rank"]').get_text(strip=True)
        name = athlete.select_one('td[data-th="Competitor"]').get_text(strip=True)
        dob = athlete.select_one('td[data-th="DOB"]').get_text(strip=True)

        athlete_id = f"{name.replace(' ', '_').lower()}_{rank}"

        athlete_info = {
            'id': athlete_id,
            'name': name,
            'rank': int(rank),
            'dob': dob,
            'distance': int(distance)
        }
    
        athletes_data.append(athlete_info)
    return athletes_data

def send_athletes_to_db(athletes_data):
    with app.app_context():
        for athlete in athletes_data:
            existing_athlete = Athlete.query.filter_by(id=athlete['id']).first()
            if existing_athlete is None:
                new_athlete = Athlete(
                    id=athlete['id'],
                    name=athlete['name'],
                    rank=athlete['rank'],
                    dob=athlete['dob'],
                    distance=athlete['distance']
                )
                db.session.add(new_athlete)
        db.session.commit()

if __name__ == "__main__":
    athletes_100m_data = athletes('100m', 100)
    send_athletes_to_db(athletes_100m_data)

    athletes_200m_data = athletes('200m', 200)
    send_athletes_to_db(athletes_200m_data)

    athletes_400m_data = athletes('400m', 400)
    send_athletes_to_db(athletes_400m_data)

    athletes_800m_data = athletes('800m', 800)
    send_athletes_to_db(athletes_800m_data)

