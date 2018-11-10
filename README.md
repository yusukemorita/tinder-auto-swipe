# tinder-auto-swipe

Simple docker image that
- retrieves an auth token from facebook
- uses token to login to Tinder
- keeps swiping right until there are no users left

# Usage

```
docker build -t tinder_swiper .
docker run -e "email=YOUR_FACEBOOK_EMAIL" -e "password=YOUR_FACEBOOK_PASSWORD" tinder_swiper
```
