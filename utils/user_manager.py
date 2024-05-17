from .dice_game import DiceGame
import time
import os


class UserManager:
	def __init__(self):
		self.user_folder = "user_data"
		self.user_file = os.path.join(self.user_folder, "users.txt")
		
		if not os.path.exists(self.user_folder):
			os.makedirs(self.user_folder)
		
	def load_users(self):
		users = {}
		if os.path.exists(self.user_file):
			with open(self.user_file, "r") as file:
				for line in file:
					username, password = line.strip().split(",")
					users[username] = password
		return users	

	def save_users(self, users):
			with open(self.user_file, "w") as file:
				for username, password in users.items():
					file.write(f"{username},{password}\n")

	def validate_username(self, username):
		users = self.load_users()
		if username in users:
			print("Username already exists.\n")
			time.sleep(1)
			return
		else:
			while True:
				password = input("Enter password (at least 8 characters), or leave blank to cancel: ")
				if not password:
					break
				if len(password) < 8:
					print("Password must be at least 8 characters long.\n")
					time.sleep(1)
				else:
					self.validate_password(username, password)

	def validate_password(self, username, password):
			users = self.load_users()
			users[username] = password
			self.save_users(users)
			print("Registration successful.")
			time.sleep(1)
			return

	def register(self):
		while True:
			os.system('cls')
			print("Registration:")
			username = input("Enter username (at least 4 characters), or leave blank to cancel: ")
			if not username:
				time.sleep(0.5)
				break
			if len(username) < 4:
				print("Username must be at least 4 characters long.")
				time.sleep(1)
			else:
				self.validate_username(username)
				break

	def login(self):
		users = self.load_users()
		while True:
			os.system('cls')
			if not users:
				print("Unable to login. No registered account.")
				input("\nPress ENTER to continue.")
				break
			else:
				users = self.load_users()
				print("Login:")
				username = input("Enter username, or leave blank to cancel: ")
				if not username:
					break
				if username in users:
					while True:
						password = input("Enter password, or leave blank to cancel: ")
						if not password:
							break
						if password == users[username]:
							print("Login successful.")
							time.sleep(1)
							DiceGame(username).menu()
						else:
							print("Incorrect Password. Please try again.\n")
							time.sleep(1)
				else:
					print("Username not found. Please try again.\n")
					time.sleep(1)