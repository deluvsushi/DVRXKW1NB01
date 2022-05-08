from library import durakonline
print("""
Script by deluvsushi
Github : https://github.com/deluvsushi
╭━━━┳╮╱╱╭┳━━━┳━╮╭━┳╮╭━┳╮╭╮╭╮╭╮╭━╮╱╭┳━━╮╭━━━╮╭╮
╰╮╭╮┃╰╮╭╯┃╭━╮┣╮╰╯╭┫┃┃╭┫┃┃┃┃┣╯┃┃┃╰╮┃┃╭╮┃┃╭━╮┣╯┃
╱┃┃┃┣╮┃┃╭┫╰━╯┃╰╮╭╯┃╰╯╯┃┃┃┃┃┣╮┃┃╭╮╰╯┃╰╯╰┫┃┃┃┣╮┃
╱┃┃┃┃┃╰╯┃┃╭╮╭╯╭╯╰╮┃╭╮┃┃╰╯╰╯┃┃┃┃┃╰╮┃┃╭━╮┃┃┃┃┃┃┃
╭╯╰╯┃╰╮╭╯┃┃┃╰┳╯╭╮╰┫┃┃╰╋╮╭╮╭╋╯╰┫┃╱┃┃┃╰━╯┃╰━╯┣╯╰╮
╰━━━╯╱╰╯╱╰╯╰━┻━╯╰━┻╯╰━╯╰╯╰╯╰━━┻╯╱╰━┻━━━┻━━━┻━━╯
""")

main_token = input("-- Account token::: ")

def main_process():
	main_client, bot_client = durakonline.Client(token=main_token, tag="[main_client]"), durakonline.Client(tag="[bot_client]")
	count = int(input("-- Count::: "))
	for i in range(count):
		bot_token = ""
		while not bot_token:
			print("-- [bot_client] Receiving captcha..")
			captcha_url, captcha_answer = bot_client.get_captcha()["url"], ""
			if captcha_url:
				print(f"-- [bot_client] Captcha::: {captcha_url}")
				captcha_answer = str(input("-- Captcha-Answer::: "))
			print("-- [bot_client] Trying to register account...")
			try: bot_token = bot_client.register(name="deluvsushi", captcha=captcha_answer).token
			except Exception as e: print(f"-- Error::: {e}"); continue
		print("-- [bot_client] Account is succesfully registered!")
		bot_client.signin_by_access_token(token=bot_token)
		bot_client._get_data(type="tour")
		bot_client.send_friend_request(user_id=main_client.uid)
		main_client._get_data(type="fl_update")
		print("-- [bot_client] sent friendship request...")
		main_client.friend_accept(friend_id=bot_client.uid)
		print("-- [main_client] accepted a friendship request...")
		bot_client.create_game(bet=100, password="zxc", players=2, deck=36)
		print("-- [bot_client] Created a room with a rate of::: 100 credits...")
		bot_client.invite_to_game(user_id=main_client.uid)
		game_id = main_client._get_data(type="invite_to_game")["game_id"]
		print("-- [bot_client] Invited to the room...")
		main_client.join_to_game(password="zxc", game_id=game_id)
		print("-- [main_client] accepted invite and joined to the room...")
		main_client._get_data(type="game")
		for i in range(49):
			main_client.ready(); bot_client.ready()
			main_client._get_data(type="ready_on")
			bot_client.surrender()
			bot_client._get_data(type="game_over")
			print(f"-- [{i+1}][bot_client]::: gave up!")
		main_client.friend_delete(friend_id=bot_client.uid)
		print("-- Done!")
		
main_process()
