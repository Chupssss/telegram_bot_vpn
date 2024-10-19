import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import paramiko
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)

with open("servers.json", "r") as servers_list:
    servers = json.load(servers_list)

with open("user_data.json", "r") as users_data_file:
    users_data = json.load(users_data_file)


bot = telebot.TeleBot(config["API_token"])


def is_admin(message):
    if message.from_user.id in config["admins"]:
        return True
    else:
        return False

def save_user_data