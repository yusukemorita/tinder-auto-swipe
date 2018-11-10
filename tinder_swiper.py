import pynder
import sys
import requests
import json
import os

def main():
    token = sys.argv[1]
    session = pynder.Session(token)
    swipe_count = 0
    match_count = 0
    message = ''

    try:
        send_to_slack('Starting automatic swiping.')
        for user in session.nearby_users():
            try:
                swipe_result = user.like()
                swipe_count += 1
                if swipe_result == True: match_count += 1
                print(f'{swipe_count} {user.name}')
            except:
                print('unexpected error inside for loop, skipping')
    except pynder.errors.RecsTimeout:
        message += 'Finished swiping!'
    except:
        message += 'Unexpected error.'
    finally:
        message += f'\n{swipe_count} users swiped, {match_count} matches found.'
        send_to_slack(message)

def send_to_slack(string):
    WEBHOOK_URL = os.environ['webhook_url']
    requests.post(WEBHOOK_URL, data = json.dumps({
        'text'      : string,
        'username'  : u'Tinder-Swiper',
        'icon_emoji': u':tinder:'
    }))

main()
