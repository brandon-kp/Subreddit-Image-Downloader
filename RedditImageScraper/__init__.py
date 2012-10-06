import json
import requests
import re
import urllib
import datetime
import os
now = datetime.datetime.now()

class RedditImageScraper(object):
    def __init__(self, subreddit, download_path):
        self.subreddit     = subreddit
        self.today         = "%s-%d-%d" %(subreddit, now.month, now.year)
        self.download_path = download_path+"/reddit_"+self.today
        self.image_links   = []

        self.download_all()

    def get_json(self):
        r = requests.get('http://reddit.com/r/'+self.subreddit+'/.json')
        print "Downloading submission list from reddit..."
        return r.text
        
    def parse_json(self):
        subreddit_json = self.get_json()
        data           = json.loads(subreddit_json)

        return data["data"]["children"]

    def get_image_links(self):
        json    = self.parse_json()
        pattern = re.compile('.*?(jpg)', re.IGNORECASE|re.DOTALL)

        for subs in json:
            subs    = subs["data"]
            matches = pattern.search(subs["url"])

            if matches:
                self.image_links.append({
                    'file_name': subs["id"],
                    'file_url' : subs["url"]
                })

    def download_image(self, url, path):
        image = urllib.URLopener()
        image.retrieve(url, path)

    def download_all(self):
        self.get_image_links()

        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)
            print "Created today's folder"

        for image in self.image_links:
            path = "%s/%s.jpg" %(self.download_path, image['file_name'])

            if os.path.exists(path):
                print "Skipped %s, it already exists." %path
            else:
                self.download_image(image['file_url'],path)
                print "Successfully downloaded %s" %path