import pynder
import sys

def main():
    token = sys.argv[1]
    session = pynder.Session(token)
    swipe_count = 0

    for user in session.nearby_users():
        try:
            print(user.name)
            swipe_result = user.like()
            ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
            print(f'{ordinal(swipe_count + 1)} person liked')
            if swipe_result == True:
                print("---------- IT'S A MATCH!!!----------")
            print("")
            swipe_count += 1
        except:
            print("unexpected error, skipping")

main()
