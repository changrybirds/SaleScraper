from twilio.rest import Client
import requests
import json, urllib

account_sid = "placeholder"
auth_token = "placeholder"
client = Client(account_sid, auth_token)


def g_shorten_url(url):
  key = 'Google URL Shortener API key'
  post_url = 'https://www.googleapis.com/urlshortener/v1/url?key=' + key
  payload = {'longUrl': url}
  headers = {'content-type': 'application/json'}

  r = requests.post(post_url, data=json.dumps(payload), headers=headers)
  resp = json.loads(r.text)
  print(resp)
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