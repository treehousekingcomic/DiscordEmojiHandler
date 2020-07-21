# discord-emoji-handler | **Updated for v1.6**
Work with messages that contain emojis that your bot can't see? Emoji Handler will take care of the problem.

## Installation
`pip install DiscordEmojiHandler`

## Available Functions & Usage 
To start you must initiate and get a EmojiHandlerObject from the EmojiHandler class.
You'll need to pass your bot's instance..

```py
import DiscordEmojiHandler as EHM
EHO = EHM.EmojiHandler(bot)
```
Now you can save `EHO` as a bot variable to use anywhere else.

- ```EmojiHandlerObject.check(text)``` | Returns True or False

Checks the text for any invalid emojis. Returns False if an invalid emoji is found, else retunrs True. You do not need to pass anything in check.

- ```EmojiHandlerObject.fix(content, colon=False)``` | Returns modified string

Checks the text for any invalid emojis and replaces found ones with just the emoji name (default) or with wrapped with `:` if `colon` is True.

- ```EmojiHandlerObject(content, text='🤔', invalid_only=True)``` | Returns modified string

Checks the text for invalid emojis and replaces found ones with `text` (default: '🤔'). By default only invalid emojis are replaced but you can set `invalid_only` to False to replace all emojis.
