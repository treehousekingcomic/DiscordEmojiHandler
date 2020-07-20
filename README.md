# discord-emoji-handler
Work with messages that contain emojis that your bot can't see? Emoji Handler will take care of the problem.

## Available Functions & Usage
To start you must initiate and get a EmojiHandlerObject from the EmojiHandler class.
You'll need to pass your bot's instance (or client) and the text to work with (string).

```py
import EmojiHandlerModule as EHM
EHO = EHM.EmojiHandler(bot, text)
```

• EmojiHandlerObject.check()

Checks the text for any invalid emojis. Returns False if an invalid emoji is found, else retunrs True. You do not need to pass anything in check.

`safe = EHO.check()`

• EmojiHandlerObject.fix(colon=False)

Checks the text for any invalid emojis and replaces found ones with just the emoji name (default) or with wrapped with `:` if `colon` is True.

`safe = EHO.fix(colon=True)` 

• EmojiHandlerObject(text='🤔', invalid_only=True)

Checks the text for invalid emojis and replaces found ones with `text` (default: '🤔'). By default only invalid emojis are replaced but you can set `invalid_only` to False to replace all emojis.
