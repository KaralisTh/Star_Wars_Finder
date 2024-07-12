import argparse
import requests
import pickle
import os
from datetime import datetime

CACHE_FILE = 'cache.pkl'

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'rb') as f:
            return pickle.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, 'wb') as f:
        pickle.dump(cache, f)

def search_character(name, planet):
    cache = load_cache()
    if name in cache:
        character_data, timestamp = cache[name]
    else:
        response = requests.get(f'https://www.swapi.tech/api/people/?name={name}')
        if response.status_code != 200 or not response.json()['result']:
            print("The force is not strong within you")
            return
        character_data = response.json()['result'][0]['properties']
        timestamp = datetime.now()
        cache[name] = (character_data, timestamp)
        save_cache(cache)
    
    print(f"Name: {character_data['name']}")
    print(f"Height: {character_data['height']}")
    print(f"Mass: {character_data['mass']}")
    print(f"Birth Year: {character_data['birth_year']}")

    if planet:
        home_url = character_data['homeworld']
        home_response = requests.get(home_url)
        home_data = home_response.json()['result']['properties']
        print("\nHomeworld")
        print("----------------")
        print(f"Name: {home_data['name']}")
        print(f"Population: {home_data['population']}")
        earth_day = 24
        earth_year = 365
        rotation_period = float(home_data['rotation_period'])
        orbital_period = float(home_data['orbital_period'])
        print(f"On {home_data['name']}, 1 year on earth is {orbital_period / earth_year} years and 1 day {rotation_period / earth_day} days")
    print(f"cached: {timestamp}")

def clear_cache():
    if os.path.exists(CACHE_FILE):
        os.remove(CACHE_FILE)
        print("removed cache")

def show_cache():
    cache = load_cache()
    if not cache:
        print("Cache is empty.")
        return
    for name, (data, timestamp) in cache.items():
        print(f"Name: {data['name']}")
        print(f"Time of search: {timestamp}")
        print("Result:")
        print(f"  Height: {data['height']}")
        print(f"  Mass: {data['mass']}")
        print(f"  Birth Year: {data['birth_year']}")
        print("----------------")

def main():
    parser = argparse.ArgumentParser(description='Star Wars Character Search')
    subparsers = parser.add_subparsers(dest='command')

    search_parser = subparsers.add_parser('search', help='Search for a Star Wars character')
    search_parser.add_argument('name', type=str, help='Name of the character to search for')
    search_parser.add_argument('--world', action='store_true', help='Include homeworld information')

    cache_parser = subparsers.add_parser('cache', help='Manage cache')
    cache_parser.add_argument('--clean', action='store_true', help='Clean the cache')
    cache_parser.add_argument('--show', action='store_true', help='Show the cache')

    args = parser.parse_args()

    if args.command == 'search':
        search_character(args.name, args.world)
    elif args.command == 'cache':
        if args.clean:
            clear_cache()
        elif args.show:
            show_cache()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
