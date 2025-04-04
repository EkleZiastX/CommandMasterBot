from pyrogram import Client
from db import initialize_db
from handlers import add_rp_command, delete_rp_command, list_rp_commands, handle_rp_command
from config import API_ID, API_HASH

initialize_db()

app = Client("my_account", api_id=API_ID, api_hash=API_HASH)

add_rp_command(app)
delete_rp_command(app)
list_rp_commands(app)
handle_rp_command(app)

app.run()