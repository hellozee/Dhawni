"""
Function: 
* To take string input fro mstt
* To convert all the compound statements into simple statements.
* For each simple sentences, characterise verb, adjective and noun
* Send the tokenized sentence to the sentiment analyzer
* Pair all the verb and noun as (action, target)

python -m textblob.download_corpora
"""

from textblob import TextBlob
from textblob.np_extractors import ConllExtractor

extractor = ConllExtractor()
#text = "open the browser"
text = str(input())

# Commands that Dhwani can handle and their respective targets
commands = ['open', 'close', 'play', 'start', 'pause', 'stop', 'increase', 'increment', 'decrease', 'decrement', 'set', 'shutdown']
actions = ['door', 'browser', 'song', 'music', 'player', 'brightness', 'volume']
attributes = []

blob = TextBlob(text.lower(), np_extractor=extractor)
token_string = blob.words
mood = token_string.sentiment.polarity
e = 0.005 # To set range for the neutral mood.

for index in range(len(token_string)):
	if token_string[index] in commands:
		#Command found and look for the target
		for ahead in range(index, len(token_string)):
			if token_string[ahead] in actions:
				# Call the execution function for (command, action)
				# Update the index with ahead + 1
				print("Add the execute command function");
				index = ahead + 1
				if token_string[ahead] == 'brightness' or 'volume':
					# If Brightness and volume, look for third attribute
	elif mood in (-1, 0 - e):
		# Bad mood. Call function to cheer him/her up. Songs/jokes
		print("Call the mood cheerer man!")
	elif mood in (0 + e, 1):
		# happy mood. Say, "looks like you are enjoying your day!"
		print("Enjoy the party man!")
	elif token_string.sentiment.polarity in (0 - e, 0 + e):
		# Neutral sentiment output. Make a pun joke
	else:
		# Invalid input. Say, "Can you rephrase your words?"
		
