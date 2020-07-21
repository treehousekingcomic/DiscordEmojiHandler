import re

class EmojiHandler():
    # regex module required (import re)
    def __init__(self, bot):
        # bot can be discord.Client or discord.ext.Bot
        self.bot = bot
        self.emoji_regex = r'<(?P<animated>a?):(?P<name>[a-zA-Z0-9_]{2,32}):(?P<id>[0-9]{18,22})>'

    def check(self, content):
        # Returns True if all emojis in the text are available to the bot, False if not.
        emojis = re.findall(self.emoji_regex, content)
        for result in emojis:
            id_ = int(result[2])

            emoji = self.bot.get_emoji(id_)
            if not emoji:
                return False
            elif not emoji.is_usable():
                return False
            else:
                continue
        return True

    def fix(self, content, colon=False):
        # Returns original content with the emojis that the bot can't see replaced with their name only.
        # If colon is True, invalid emojis are replaced with :name: (with the :)
        if not content:
            return None
        emojis = re.findall(self.emoji_regex, content)
        for result in emojis:
            id_, name_, animated_ = result

            emoji = self.bot.get_emoji(id_)
            if not emoji or not emoji.is_usable():
                content = content.replace(f'<{animated_}:{name_}:{id_}>', f'{name if not colon else ":" + name_ + ":"}')
            else:
                continue
        return content

    def replace(self, content, text='🤔', invalid_only=True):
        # Returns the original content with invalid emojis replaced with text (default: 🤔)
        # If you want to replace all emojis, pass False to invalid_only
        if not content:
            return None
        for result in self.emojis:
            id_, name_, animated_ = result

            emoji = self.bot.get_emoji(id_)
            if not emoji or not emoji.is_usable():
                content = content.replace(f'<{animated_}:{name_}:{id_}>', text)
            elif not invalid_only:
                    content = content.replace(f'<{animated_}:{name_}:{id_}>', text)
            else:
                continue
        return content
