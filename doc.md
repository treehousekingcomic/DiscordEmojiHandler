# EmojiHandler

A emoji handler that handles the emojis

- ## Arguments

  - **`bot`**: `discord.Client or commands.Bot` —
    the bot the handle the emojis from

- ## Example

   ```py
   import discord
   from discord.ext import commands
   import DiscordEmojiHandler as EHM
   
   bot = commands.Bot(command_prefix="!")
   emoji_handler = EHM.EmojiHandler(bot)

   @bot.command()
   async def say(ctx, *, text):
      """Command that says what you tell the bot to say"""
      fixed_text = emoji_handler.fix(text)
      await ctx.send(fixed_text)

   bot.run("TOKEN")
      
   ```

### Method

--------------------------------
>
> ```python
> check(content: str)
> ```
>
Return True if all emojis in the text are available to the bot, False if not.

- ## Parameters

  - **`content`**: `str` — the text to get the emojis from

- ## Returns

  - `bool` —
True if all emojis in the text are available to the bot, False if not.

### Method

--------------------------------
>
> ```python
> fix(content: str, colon=False)
> ```
>
Get the original content with the emojis that the bot can't see replaced with their name only.

- ## Parameters

  - **`content`**: `str` — the text to fix the emojis from

  - **`colon`**: `Optional[bool]` — If this is True, invalid emojis have a colon (eg. :name:), by default `False`

- ## Returns

   `str` — the text with the emojis fixed

### Method

--------------------------------
>
> ```python
> replace(content: str, text: str = "🤔", invalid_only=True)
> ```
>
Get the original content with invalid emojis replaced with text.

- ## Parameters

  - **`content`** `str` — the content to replace the original emojis from

  - **`text`** `Optional[str]` — the text that the content should be replaced with, by default "🤔"
  - **`invalid_only`** `Optional[bool]` — whether to only replace invalid or not, passing False will replace all emojis, by default `True`

- ## Returns

   `str` —
The original content with invalid emojis replaced with text

--------------------------------
<p align="center">Docs made with ❤️ by Wasi Master<p/>
