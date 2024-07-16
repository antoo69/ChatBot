#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/YukkiChatBot >.
#
# This file is part of < https://github.com/TeamYukki/YukkiChatBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiChatBot/blob/master/LICENSE >
#
# All rights reserved.
#

from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("28518520"))
API_HASH = getenv("c858cde56cb2b2050a64df7e65de567b")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("7360542256:AAG5noO24YrY4jSoJs75UtqzMO6TBpbdlF8")

# SUDO USERS
SUDO_USER = list(
    map(int, getenv("6681099028", "").split())
)  # Input type must be interger

# You'll need a Private Group ID for this.
LOG_GROUP_ID = int(getenv("-1002079962899"))

# Message to display when someone starts your bot
PRIVATE_START_MESSAGE = getenv(
    "PRIVATE_START_MESSAGE",
    "Hello! Welcome to my Personal Assistant Bot",
)

# Database to save your chats and stats... Get MongoDB:-  https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/mongodb#4.-youll-see-a-deploy-cloud-database-option.-please-select-shared-hosting-under-free-plan-here
MONGO_DB_URI = getenv("mongodb+srv://jarij2216:buburayam1@cluster0.uueck7c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)
