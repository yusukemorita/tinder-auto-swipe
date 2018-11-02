FROM python:3.6

# install pinder
RUN pip install git+https://github.com/charliewolf/pynder.git

# install ruby and mechanize
RUN apt-get update && apt-get install -y software-properties-common
RUN apt-add-repository ppa:brightbox/ruby-ng
RUN apt-get install ruby2.3 ruby2.3-dev -y
RUN gem install mechanize

WORKDIR /app

COPY . .

CMD ["sh","main.sh"]
