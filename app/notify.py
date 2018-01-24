from twilio.rest import Client
import requests
import json

# Twilio credentials
account_sid = "Twilio placeholder"
auth_token = "Twilio placeholder"
client = Client(account_sid, auth_token)

# Google URL shortener credentials
g_shorten_key = 'Google URL Shortener API key'

def g_shorten_url(url):
  post_url = 'https://www.googleapis.com/urlshortener/v1/url?key=' + g_shorten_key
  payload = {'longUrl': url}
  headers = {'content-type': 'application/json'}

  r = requests.post(post_url, data=json.dumps(payload), headers=headers)
  resp = json.loads(r.text)
  
  # print(resp)
  return resp['id']


def notify_sale(phone, vendor, url):
  short_url = g_shorten_url(url)
  client.api.account.messages.create(
    to=phone, 
    from_="twilio number here", 
    body="Your tracked item from " + vendor + " is on sale! Click to go to the product page: " + short_url)


def __main():
    short = g_shorten_url('http://www.nytimes.com')
    print(short)


if __name__ == '__main__':
    __main()