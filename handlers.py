from asyncio import sleep
from pyrogram import filters
from pyrogram.errors import FloodWait
from db import get_db_connection
from config import DEFAULT_USERNAME

your_username = DEFAULT_USERNAME

def add_rp_command(app):
    @app.on_message(filters.command("add_rp", prefixes=".") & filters.me)
    def handler(_, msg):
        try:
            parts = msg.text.split(maxsplit=3)
            conn = get_db_connection()
            cursor = conn.cursor()
            command = f".{parts[1]}"
            action = parts[2].replace('"', '').replace("'", '').strip()
            extra_text = parts[3].replace('"', '').replace("'", '').strip()
            template = f"{{your_username}} {action} {{name}} {extra_text}"
            cursor.execute("INSERT INTO rp_commands (command, description, template) VALUES (?, ?, ?)",
                           (command, f"RP-команда: {command}", template))
            conn.commit()
            msg.edit(f"✅ RP-команда `{command}` успешно добавлена!")
        except sqlite3.IntegrityError:
            msg.edit("❌ Такая команда уже существует!")
        finally:
            conn.close()

def delete_rp_command(app):
    @app.on_message(filters.command("del_rp", prefixes=".") & filters.me)
    def handler(_, msg):
        try:
            parts = msg.text.split(maxsplit=1)
            conn = get_db_connection()
            cursor = conn.cursor()
            command = parts[1]
            cursor.execute("DELETE FROM rp_commands WHERE command = ?", (command,))
            conn.commit()
            if cursor.rowcount > 0:
                msg.edit(f"✅ RP-команда `{command}` успешно удалена!")
            else:
                msg.edit("❌ Команда не найдена!")
        finally:
            conn.close()

def list_rp_commands(app):
    @app.on_message(filters.command("list_rp", prefixes=".") & filters.me)
    def handler(_, msg):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT command, description FROM rp_commands")
            commands = cursor.fetchall()
            if commands:
                text = "📜 **Список RP-команд:**\n" + "\n".join([f"- `{cmd}`: {desc}" for cmd, desc in commands])
            else:
                text = "❌ RP-команды не найдены!"
            msg.edit(text)
        finally:
            conn.close()

def handle_rp_command(app):
    @app.on_message(filters.text & filters.me)
    def handler(_, msg):
        try:
            command = msg.text.split()[0]
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT template FROM rp_commands WHERE command = ?", (command,))
            result = cursor.fetchone()
            if not result:
                return
            template = result[0]
            user = msg.reply_to_message.from_user
            name = user.first_name or user.username
            user_link = f'<a href="tg://user?id={user.id}">{name}</a>'
            txt = msg.text[len(command):].strip()
            action, extra_text = (txt.split(maxsplit=1) + [""])[:2] if txt else ("", "")
            action = action.replace('"', '').replace("'", '').strip()
            extra_text = extra_text.replace('"', '').replace("'", '').strip()
            text = f"{template}".format(
                your_username=your_username,
                action=action,
                name=user_link,
                extra_text=extra_text
            )
            msg.edit_text(text, disable_web_page_preview=True)
        finally:
            conn.close()
            
            
    @app.on_message(filters.command("type", prefixes=".") & filters.me)
    def type(_, msg):
        orig_text = msg.text.split(".type ", maxsplit=1)[1]
        text = orig_text
        tbp = ""
        typing_symbol = "/"

        while (tbp != orig_text):
            try:
                msg.edit(tbp + typing_symbol)
                sleep(0.05)  # 50 ms

                tbp = tbp + text[0]
                text = text[1:]

                msg.edit(tbp)
                sleep(0.05)

            except FloodWait as e:
                sleep(e.x)