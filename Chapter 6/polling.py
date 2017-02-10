favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'rudy',
	'phil': 'python',
	}

should_poll = ['melo', 'james', 'jen', 'phil']

for polled in should_poll:
	if polled in favorite_languages.keys():
		print(polled + " , thank you for polling.")
	else:
		print(polled + " , can you take a poll?")
