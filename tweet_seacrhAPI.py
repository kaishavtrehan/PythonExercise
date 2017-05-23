import urllib.request
import twurl
import json
import pymongo

#	TWITTER_URL = 'https://api.twitter.com/1.1/search/tweets.json'
TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

#	Get DB Instance
client = pymongo.MongoClient("localhost", 27017)
db = client.prototypedb


#	Get Collection Instance, Here collection means table
collection = db.tweets_store
#	print(collection)

while True:
	input_txt = input('Enter your search, or quit: ')
	if (input_txt == 'quit') : 
		break
	url = twurl.augment(TWITTER_URL,{'screen_name': input_txt, 'count': '20'})
	print('Retrieving', url, '\n\n')
	connection = urllib.request.urlopen(url)
	data = connection.read().decode()
#	print (data[:],'\n\n')
	headers = connection.info()
#	print (headers['x-rate-limit-remaining'])
#	print ('Remaining ',headers['x-rate-limit-remaining'],'\n\n')
	tweets_json = json.loads(data)

	
#	print (json.dumps(js, indent=4))
#	print (js)
	

	for tweets in tweets_json:
#		print(tweets['user']['name'], '\n')
		default=tweets.get('retweeted_status',0)
		if default != 0:
			collection.insert_one({'name': tweets['user']['name'],
								   'screen_name': tweets['user']['screen_name'],
								   'tweetvalue': tweets['retweeted_status']['text'],
								   'retweet_count': tweets['retweet_count'],
								   'favorite_count': tweets['favorite_count'],
								   'tweetdate': tweets['created_at']}).inserted_id
		elif tweets['is_quote_status'] == 'true':
			collection.insert_one({'name': tweets['user']['name'],
								   'screen_name': tweets['user']['screen_name'],
								   'tweetvalue': tweets['quoted_status']['text'],
								   'retweet_count': tweets['retweet_count'],
								   'favorite_count': tweets['favorite_count'],
								   'tweetdate': tweets['created_at']}).inserted_id
		else:
			collection.insert_one({'name': tweets['user']['name'],
								   'screen_name': tweets['user']['screen_name'],
								   'tweetvalue': tweets['text'],
								   'retweet_count': tweets['retweet_count'],
								   'favorite_count': tweets['favorite_count'],
								   'tweetdate': tweets['created_at']}).inserted_id
#	for u in js['users'] :
#		print (u['screen_name'],'\n')
#		friend = u['screen_name']
#		try:
#			count = collection.find_one({'name': friend})['friends']
#			collection.update_one({'name': friend}, {'$inc': {'friends': count + 1}})
#			countold = countold + 1
#		except:
#			collection.insert_one({'name': friend,'retrieved': 0, 'friends': 1}).inserted_id
#			countnew = countnew + 1