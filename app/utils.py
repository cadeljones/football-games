import requests
from datetime import datetime


NFL_BASE_URL = "https://delivery.chalk247.com/"
STANDINGS_URL = "team_rankings/NFL.json"


def generate_scoreboard_url(start_date, end_date):
    return f'{NFL_BASE_URL}scoreboard/NFL/{start_date}/{end_date}.json'


def retrive_team_standings(nfl_api_key):
    params = {"api_key": nfl_api_key}
    url = NFL_BASE_URL + STANDINGS_URL
    r = requests.get(url, params=params)

    r_json = r.json()
    team_standings_data = r_json['results']['data']

    return team_standings_data


def retrive_scoreboard(start_date, end_date, nfl_api_key):
    params = {"api_key": nfl_api_key}
    url = generate_scoreboard_url(start_date, end_date)
    r = requests.get(url, params=params)

    r_json = r.json()
    days_dict = r_json['results']

    return days_dict


def get_team_stading_info(team_id, standings):
    for team in standings:
        if team["team_id"] == team_id:
            return team


def get_events(start_date, end_date, nfl_api_key):
    team_standings_data = retrive_team_standings(nfl_api_key)
    days_dict = retrive_scoreboard(start_date, end_date, nfl_api_key)

    all_events = []
    for day in days_dict:
        if type(days_dict[day]) is dict:
            events = days_dict[day]['data']
            for k, event in events.items():
                event_dict = {}

                away_team = get_team_stading_info(
                    event['away_team_id'],
                    team_standings_data
                )

                home_team = get_team_stading_info(
                    event['home_team_id'],
                    team_standings_data
                )

                event_date = datetime.strptime(
                    event['event_date'],
                    '%Y-%m-%d %H:%M'
                )

                event_dict['event_id'] = event['event_id']
                event_dict['event_date'] = event_date.strftime("%d-%m-%Y")
                event_dict['event_time'] = event_date.strftime("%H:%M")
                event_dict['away_team_id'] = event['away_team_id']
                event_dict['away_nick_name'] = event['away_nick_name']
                event_dict['away_city'] = event['away_city']
                event_dict['away_rank'] = away_team['rank']
                event_dict['away_rank_points'] = str(round(
                    float(away_team['adjusted_points']), 2
                ))
                event_dict['home_team_id'] = event['home_team_id']
                event_dict['home_nick_name'] = event['home_nick_name']
                event_dict['home_city'] = event['home_city']
                event_dict['home_rank'] = home_team['rank']
                event_dict['home_rank_points'] = str(round(
                    float(home_team['adjusted_points']), 2
                ))

                all_events.append(event_dict)

    return all_events
