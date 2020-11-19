#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import pyttsx3
import os
from time import sleep
import demoji  # TODO

# Simple tg voice announcement chats reader
# https://github.com/Kosat/telegram-messages-dump # used for dump tg chat
# before run as daemon exec:
# telegram-messages-dump -c "<telegram_chat_name>" -p "<phone_number_full>" -o "log_file>" -cl


LOG_FILE = "glash_dump"
MOBILE_NUMBER = "+XXXXXXXXXXXX"
REFRESH_TIME_SECONDS = 300


def convert_record(log_record: str) -> str:
    name = log_record.split()[3]
    message = log_record.split(": ")[-1]
    try:
        message = message.encode('Windows-1251').decode('utf-8')  # РїС‘СЃ РїС‘СЃ РїС‘СЃ -> пёс пёс пёс
    except UnicodeDecodeError:
        pass
    to_announce = f"говорит {name}: {message}"
    return to_announce


def spell(phrase: str) -> None:
    hui = pyttsx3.init()
    hui.say(phrase)
    hui.runAndWait()


def get_state(file):
    with open(file, errors='ignore') as f:
        state = f.readlines()
        return state


def main():
    # demoji.download_codes()
    while True:
        prev = get_state(LOG_FILE)
        os.system(f"telegram-messages-dump -p {MOBILE_NUMBER} -o {LOG_FILE} -cl --continue")
        post = get_state(LOG_FILE)
        if post != prev:
            new_records_list = [item for item in post if item not in prev]
            for record in new_records_list:
                statement = convert_record(record)
                print(statement)
                spell(statement)
        sleep(REFRESH_TIME_SECONDS)


if __name__ == '__main__':
    main()
