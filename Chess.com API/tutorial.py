from chessdotcom import get_leaderboards,get_player_stats,get_player_game_archives
import pprint
import requests

printer = pprint.PrettyPrinter()

def print_leaderboards():
	data = get_leaderboards().json
	# printer.pprint(data.json)
	# print(data.json['leaderboards']['daily'])
	categories = data['leaderboards'].keys()
	for category in categories:
		print('Category:',category)
		for idx,entry in enumerate(data['leaderboards'][category]):
			# print(entry)
			print(f'Rank: {idx + 1} | Username: {entry["username"]} | Rating: {entry["score"]}')


def get_player_rating(username):
	data = get_player_stats(username).json['stats']
	# printer.pprint(data)
	categories = ["chess_blitz","chess_rapid","chess_bullet"]
	for category in categories :
		print('Category:',category)
		print(f'Current:{data[category]["last"]["rating"]}')
		print(f'best:{data[category]["best"]["rating"]}')
		print(f'record:{data[category]["record"]}')

get_player_rating('timruscica')


def get_most_recnt_game(username):
	data = get_player_game_archives(username).json
	# print(data)
	url = data['archives'][-1]
	# print(url)
	games =requests.get(url).json()
	# print(games)
	game = games['games'][-1]
	# print(game)
	printer.pprint(game)

get_most_recnt_game('timruscica')





# print_leaderboards()