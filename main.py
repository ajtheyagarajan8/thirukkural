import json
import random

filepath = 'static/thirukkural.json'

def get_random_thirukkural():
    with open(filepath, 'r') as f:
        data = json.load(f)

    # length will be 1330
    length = len(data['kural'])

    # Index goes from 0 to 1329
    index = random.randint(0, length - 1)

    thirukkural = data['kural'][index]
    
    return thirukkural

if __name__ == "__main__":
    thirukkural = get_random_thirukkural()
    
