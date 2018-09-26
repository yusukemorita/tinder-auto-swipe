# usage: sh main.sh [facebook email] [facebook password]

FB_EMAIL=$1
FB_PASSWORD=$2

echo "retrieving facebook auth token... "
FB_AUTH_TOKEN=$(ruby fb_token_retriever.rb $FB_EMAIL $FB_PASSWORD)

echo "running python tinder script..."
python tinder_swiper.py $FB_AUTH_TOKEN
