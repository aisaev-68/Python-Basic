import json
import collections
import requests
from typing import Any

res_episode: Any = dict()

if __name__ == '__main__':

    req_death = requests.get('https://www.breakingbadapi.com/api/deaths')
    all_death = req_death.json()

    req_episodes = requests.get('https://www.breakingbadapi.com/api/episodes')
    all_episodes = req_episodes.json()

    count_deaths = collections.Counter()
    for death in all_death:
        count_deaths[(death['season'], death['episode'])] += death['number_of_deaths']

    season_episode, max_number_deaths = max(count_deaths.items(), key=lambda x: x[1])
    num_season, num_episode = season_episode

    lst_deaths = [death['death'] for death in all_death
                  if death['season'] == num_season and death['episode'] == num_episode]

    id_episode = None
    for episode in all_episodes:
        if episode["series"] == 'Breaking Bad' and episode["season"] == str(num_season) \
                and episode["episode"] == str(num_episode):
            id_episode = episode['episode_id']
            break

    res_episode["episode_id"] = id_episode
    res_episode["season"] = str(num_season)
    res_episode["episode"] = str(num_episode)
    res_episode['number_of_deaths'] = max_number_deaths
    res_episode['list_deaths'] = lst_deaths

    print(f"Больше всего смертей случилось в {str(num_episode)} "
          f"эпизоде {str(num_season)} сезона и составляет: {max_number_deaths}")

    with open('max_count_deaths.json', 'w') as f_json:
        json.dump(res_episode, f_json, indent=4)

    with open('max_count_deaths.json', 'r') as f_json:
        print(f_json.read())
