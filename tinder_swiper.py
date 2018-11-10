import pynder
import sys

def main():
    token = sys.argv[1]
    session = pynder.Session(token)
    swipe_count = 0
    match_count = 0

    try:
        for user in session.nearby_users():
            try:
                swipe_result = user.like()
                swipe_count += 1
                if swipe_result == True: match_count += 1
                print(f'{swipe_count} {user.name}')
            except:
                print("unexpected error inside for loop, skipping")
    except pynder.errors.RecsTimeout:
        print("There are no more users left!")
    except:
        print("unexpected error, skipping")
    finally:
        print(f'{swipe_count} users swiped, {match_count} matches found')

main()
