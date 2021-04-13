#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print(
    """Vá para my.telegram.org
Faça login usando sua conta do Telegram
Clique em Ferramentas de Desenvolvimento de API
Crie um novo aplicativo, inserindo os detalhes necessários"""
)
APP_ID = int(input("Insira o ID do APP aqui: "))
API_HASH = input("Insira API HASH aqui: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
    client.send_message("me", client.session.save())
