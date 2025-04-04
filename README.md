# UserBot

A simple Telegram UserBot built with [Pyrogram](https://docs.pyrogram.org/).

## Features

- Add, delete, and list RP commands.
- Use RP commands in chats by replying to messages.

## Requirements

- Python 3.7 or higher
- `pyrogram` library
- Telegram API credentials (`api_id` and `api_hash`)

## Installation

1. Clone the repository or download the files.
2. Install dependencies:
   ```bash
   pip install pyrogram
   ```
3. Replace `API_ID` and `API_HASH` in `main.py` with your credentials from [my.telegram.org](https://my.telegram.org/).

## Running the Bot

### On Linux/Windows
Run the bot using Python:
```bash
python main.py
```

### On Termux
1. Install Python:
   ```bash
   pkg install python
   ```
2. Install dependencies:
   ```bash
   pip install pyrogram
   ```
3. Run the bot:
   ```bash
   python main.py
   ```

## Usage

### Adding an RP Command
```bash
.add_rp <command> <template>
```
Example:
```bash
.add_rp hello "{name}, welcome to the chat!"
```

### Deleting an RP Command
```bash
.del_rp <command>
```
Example:
```bash
.del_rp hello
```

### Listing RP Commands
```bash
.list_rp
```

### Using an RP Command
Reply to a message and type the command:
```bash
.hello
```
Result:
```bash
<name>, welcome to the chat!
```

## Notes

- Templates can include `{name}` to mention the user you are replying to.
- Ensure you have the correct API credentials before running the bot.
