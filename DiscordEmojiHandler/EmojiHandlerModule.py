import re

class EmojiHandlerError(Exception):
    pass
class EmojiHandler_NoEmojis(EmojiHandlerError):
    pass

class EmojiHandler():
    # regex module required (import re)
    def __init__(self, bot, content: str):
        # bot can be discord.Client or discord.ext.Bot
        # content is the text to check
        self.bot = bot
        self.content = content
        self.emoji_regex = r'<(?P<animated>a?):(?P<name>[a-zA-Z0-9_]{2,32}):(?P<id>[0-9]{18,22})>'
        self.emojis = re.findall(self.emoji_regex, self.content)
        if not self.emojis:
            raise EmojiHandler_NoEmojis("No emojis in content.")

    def check(self):
        # Returns True if all emojis in the text are available to the bot, False if not.
        for result in self.emojis:
            id = int(result[2])

            emoji = self.bot.get_emoji(id)
            if not emoji:
                return False
            else:
                continue
        return True

    def fix(self, colon=False):
        # Returns original content with the emojis that the bot can't see replaced with their name only.
        # If colon is True, invalid emojis are replaced with :name: (with the :)
        for result in self.emojis:
            id = int(result[2])
            name = result[1]
            animated = result[0]

            emoji = self.bot.get_emoji(id)
            if not emoji:
                self.content = self.content.replace(f'<{animated}:{name}:{id}>', f'{name if not colon else ":" + name + ":"}')
            else:
                continue
        return self.content

    def replace(self, text='🤔', invalid_only=True):
        # Returns the original content with invalid emojis replaced with text (default: 🤔)
        # If you want to replace all emojis, pass False to invalid_only
        for result in self.emojis:
            id = int(result[2])
            name = result[1]
            animated = result[0]

            emoji = self.bot.get_emoji(id)
            if not emoji:
                self.content = self.content.replace(f'<{animated}:{name}:{id}>', text)
            else:
                if not invalid_only:
                    self.content = self.content.replace(f'<{animated}:{name}:{id}>', text)
                else:
                    continue
        return self.content
