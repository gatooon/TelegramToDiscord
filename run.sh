#!/bin/bash

function ctrl_c() {
    pidof python3 | cut -d " " -f 1 | xargs kill -9
    exit 2
}

trap "ctrl_c" SIGINT

python3 source/DiscordSide.py &
python3 source/TelegramSide.py