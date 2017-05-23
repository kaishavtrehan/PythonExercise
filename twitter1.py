import urllib.request
import twurl
import json
import pymongo

#TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
#TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
TWITTER_URL = 'https://api.twitter.com/1.1/search/tweets.json'

#client = pymongo.MongoClient("localhost", 27017)
#Get DB Instance
#db = client.prototypedb
#print(db.name)

#Get Collection Instance
#collection = db.customer_application_mst
#print(collection)


while True:
	print ('')
	#acct = input('Enter Twitter Account:')
	acct = input('Enter HashTag: ')
	if ( len(acct) < 1 ) : break
	url = twurl.augment(TWITTER_URL,{'q': acct, 'count': '1'} )
	print ('Retrieving', url,'\n\n')
	connection = urllib.request.urlopen(url)
	data = connection.read().decode()
	#print (data[:],'\n\n')
	headers = connection.info()
	#print (headers['x-rate-limit-remaining'])
	print ('Remaining ',headers['x-rate-limit-remaining'],'\n\n')
	js=json.loads(data)
	print (json.dumps(js, indent=4))
	#print (js)
	#try:
	#	fout = open('Twitter_Friendlist.json','w')
	#except:
	#	print('File cannot be opened: ', 'Twitter_Friendlist.json')
	#fout.write(str(json.dumps(js, indent=4)))
	#fout.close()
	#for u in js['users'] :
	#	print (u['screen_name'])
	#	s = u['status']['text']
	#	print (' ',s[:])