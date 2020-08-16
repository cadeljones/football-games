import requests
from datetime import datetime


NFL_BASE_URL = "https://delivery.chalk247.com/"
STANDINGS_URL = "team_rankings/NFL.json"


def generate_scoreboard_url(start_date, end_date):
    return f'{NFL_BASE_URL}scoreboard/NFL/{start_date}/{end_date}.json'


def retrieve_team_standings(nfl_api_key):
    params = {"api_key": nfl_api_key}
    url = NFL_BASE_URL + STANDINGS_URL
    r = requests.get(url, params=params)

    r_json = r.json()
    error = r_json['results'].get("error", False)
    if error:
        return False, error

    return True, r_json['results']['data']


def retrieve_scoreboard(start_date, end_date, nfl_api_key):
    params = {"api_key": nfl_api_key}
    url = generate_scoreboard_url(start_date, end_date)
    r = requests.get(url, params=params)

    r_json = r.json()
    error = r_json['results'].get("error", False)
    if error:
        return False, error

    return True, r_json['results']


def get_team_standings_info(team_id, standings):
    for team in standings:
        if team["team_id"] == team_id:
            return team


def generate_events(standings, scoreboard):
    team_standings_data = standings
    days_dict = scoreboard

    all_events = []
    for day in days_dict:
        if type(days_dict[day]) is dict:
            events = days_dict[day]['data']
            for k, event in events.items():

                away_team = get_team_standings_info(
                    event['away_team_id'],
                    team_standings_data
                )
                home_team = get_team_standings_info(
                    event['home_team_id'],
                    team_standings_data
                )
                event_date = datetime.strptime(
                    event['event_date'],
                    '%Y-%m-%d %H:%M'
                )

                event_dict = {
                    'event_id': event['event_id'],
                    'event_date': event_date.strftime("%d-%m-%Y"),
                    'event_time': event_date.strftime("%H:%M"),
                    'away_team_id': event['away_team_id'],
                    'away_nick_name': event['away_nick_name'],
                    'away_city': event['away_city'],
                    'away_rank': away_team['rank'],
                    'away_rank_points': str(round(
                        float(away_team['adjusted_points']), 2
                    )),
                    'home_team_id': event['home_team_id'],
                    'home_nick_name': event['home_nick_name'],
                    'home_city': event['home_city'],
                    'home_rank': home_team['rank'],
                    'home_rank_points': str(round(
                        float(home_team['adjusted_points']), 2
                    )),
                }
                all_events.append(event_dict)

    return all_events


def get_events(start_date, end_date, nfl_api_key):
    team_standings_success, team_standings_data = retrieve_team_standings(nfl_api_key)
    scoreboard_success, scoreboard_data = retrieve_scoreboard(start_date, end_date, nfl_api_key)

    if team_standings_success and scoreboard_success:
        return {"results": {"data": generate_events(team_standings_data, scoreboard_data) }}

    elif not team_standings_success:
        return {"results": {"error": team_standings_data }}
    else:
        return {"results": {"error": scoreboard_data }}

