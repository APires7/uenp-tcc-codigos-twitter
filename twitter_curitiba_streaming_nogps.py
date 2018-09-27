import sys
import tweepy
import csv  

consumer_key = "p8NtlIZGaQZ4dIdGXUizLCM6F"
consumer_secret = "SiPLBsJcc1GlMJVezvetN6j12KZwwXMe80FoJiSRfAnJt8OKuk"
access_key="98717714-Uz0ceKwIH7zDFxq5essAzuttlY0fyPR3RoXChXJGV"
access_secret="mn8kABOV7IeSoBDYpUpAOrDkuJtbw9nbXfiR76YIlRHQ9"

outfile = "output_curitiba_streaming_nogps.csv"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if '' in status.text.lower():
            user = status.user.screen_name
            text = status.text.encode(sys.stdout.encoding, errors='replace')
            coord = status.coordinates
            place = status.place.full_name.encode(sys.stdout.encoding, errors="replace")
            created = status.created_at

            if place == "Curitiba, Brasil" or place == "Curitiba, Brazil":
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
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream


sapi = tweepy.streaming.Stream(auth, CustomStreamListener())    
sapi.filter(locations=[-49.407632,-25.558305,-49.138358,-25.344269])
csvfile.close()
