import urllib.request
import twurl
import json
import pymongo

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
#	TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

client = pymongo.MongoClient("localhost", 27017)
#	Get DB Instance
db = client.prototypedb
#	print(db.name)

#	Get Collection Instance, Here collection means table
collection = db.customer_socialmedia_events
#	print(collection)

while True:
	acct = input('Enter a Twitter account, or quit: ')
	if (acct == 'quit') : 
		break
	if (len(acct) < 1) :
		try:
			acct = collection.find_one({"retrieved":0})['name']
		except:
			print('No unretrieved Twitter accounts found')
			continue
	
	url = twurl.augment(TWITTER_URL,{'screen_name': acct, 'count': '3'})
	print('Retrieving', url, '\n\n')
	connection = urllib.request.urlopen(url)
	data = connection.read().decode()
#	print (data[:],'\n\n')
	headers = connection.info()
#	print (headers['x-rate-limit-remaining'])
#	print ('Remaining ',headers['x-rate-limit-remaining'],'\n\n')
	js = json.loads(data)

#	update data into Collection Instance
	collection.update_one({'name':acct},{'$inc': {'retrieved':1}})
#	print(post_id)
	
#	print (json.dumps(js, indent=4))
#	print (js)
#	print(collection.find_one({"name":acct})['friends'])
	
	countnew = 0
	countold = 0
	for u in js['users'] :
		print (u['screen_name'],'\n')
		friend = u['screen_name']
		try:
			count = collection.find_one({'name': friend})['friends']
			collection.update_one({'name': friend}, {'$inc': {'friends': count + 1}})
			countold = countold + 1
		except:
			collection.insert_one({'name': friend,'retrieved': 0, 'friends': 1}).inserted_id
			countnew = countnew + 1
	print ('New accounts=', countnew, 'revisited=', countold)
#		post_id = collection.insert_one({"name":u['screen_name'],"details":u}).inserted_id
#		s = u['status']['text']
#		print (' ',s[:])