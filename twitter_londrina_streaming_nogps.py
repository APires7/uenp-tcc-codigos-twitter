import sys
import tweepy
import csv  

consumer_key = "EFnIoq77AHgIo8SgTsD5Ypsch"
consumer_secret = "me8dIwSsNJ9J92FvDR9ZCQCtlZeIv1aQTnHrtzu6jtQiMlY7nj"
access_key="98717714-rk4eM3GOzBS47JXOw5BJewAcEwiWJ9uLnS1WAUBIg"
access_secret="7NtTXPwajoYOmmV52zUEt9sEaJqmEi4S9E8s6RvGgnI7l"

outfile = "output_londrina_streaming_nogps.csv"

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

            if place == 'Londrina, Brasil' or place == 'Londrina, Brazil':
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
sapi.filter(locations=[-51.237822,-23.401435,-51.092422,-23.241124])
csvfile.close()
