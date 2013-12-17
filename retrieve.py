from keys import API_TOKEN
import urllib2, json

url = ("http://data.adicu.com/courses/v2/courses?"
       "api_token={api_token}&"
       "department=coms&"
       "pretty=true&"
       "limit=1"
           .format(api_token = API_TOKEN))

res = urllib2.urlopen(url)
data = json.loads(res.read())
