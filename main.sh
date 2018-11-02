# usage: sh main.sh [facebook email] [facebook password]

FB_EMAIL=$email
FB_PASSWORD=$password

echo "retrieving facebook auth token... "
FB_AUTH_TOKEN=$(ruby fb_token_retriever.rb $FB_EMAIL $FB_PASSWORD)
echo $FB_AUTH_TOKEN

echo "running python tinder script..."
python tinder_swiper.py $FB_AUTH_TOKEN
