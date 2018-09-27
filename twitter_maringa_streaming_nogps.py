import sys
import tweepy
import csv
from unicodedata import normalize  

consumer_key = ""
consumer_secret = ""
access_key=""
access_secret=""

outfile = "output_maringa_streaming_nogps.csv"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)



#def goto(linenum):
#    global line
#    line = linenum

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if '' in status.text.lower():
            user = status.user.screen_name
            text = status.text.encode(sys.stdout.encoding, errors='replace')
            coord = status.coordinates
            #place = status.place.full_name.encode(sys.stdout.encoding, errors="replace")
            place = normalize('NFKD', status.place.full_name).encode('ASCII', 'ignore').decode('ASCII')
            created = status.created_at

            if place == 'Maringa, Brasil' or place == 'Maringa, Brazil':
		csvfile = open(outfile, "a")
		csvwriter = csv.writer(csvfile, delimiter = ';')
                row = [user, text, coord, place, created]
                csvwriter.writerow(row)
		csvfile.close()
                print user
                print text
                print coord
                print place
                print created
                
    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        csvfile.close()
        #goto(12)
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())    
sapi.filter(locations=[-52.016274,-23.473954,-51.856711,-23.360538])
csvfile.close()
