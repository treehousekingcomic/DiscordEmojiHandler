import re
import discord

class EmojiHandler():
    """The emoji handler class
    
    Parameters:
        bot (typing.Union[discord.Bot, discord.AutoShardedBot, discord.Client])
    """
    def __init__(self, bot: typing.Union[discord.commands.Bot, discord.commands.AutoShardedBot, discord.Client]):
        self.bot = bot
        self.emoji_regex = r'<(?P<animated>a?):(?P<name>[a-zA-Z0-9_]{2,32}):(?P<id>[0-9]{18,22})>'

    def check(self, content: str):
        """Returns True if all emojis in the text are available to the bot, False if not
        
        Parameters:
            content (str): The message content
        """
        emojis = re.findall(self.emoji_regex, content: str)
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

    def fix(self, content: str, colon: bool=False):
        """
        Returns original content with the emojis that the bot can't see replaced with their name only.
        If colon is True, invalid emojis are replaced with :name: (with the :)
        
        Parameters:
            content (str): The message content
            colon (bool): Whether to replace with :name: or not
        """
        if not content:
            return None
        emojis = re.findall(self.emoji_regex, content: str)
        for result in emojis:
            animated_, name_, id_ = result

            emoji = self.bot.get_emoji(int(id_))
            if not emoji or not emoji.is_usable():
                content = content.replace(f'<{animated_}:{name_}:{id_}>', f'{name_ if not colon else ":" + name_ + ":"}')
            else:
                continue
        return content

    def replace(self, content: str, text: str ='🤔', invalid_only: bool=True):
        """Returns the original content with invalid emojis replaced with text (default: 🤔)
        If you want to replace all emojis pass False to invalid_only
        
        Parameters:
            content (str): The message content
            text (str): What to replace with
            invalid_only (bool): Whether to replace all emojis or not
        
        Returns: 
            content (str): The replaced content/message string
        """
        if not content:
            return None
        emojis = re.findall(self.emoji_regex, content)
        for result in emojis:
            animated_, name_, id_ = result

            emoji = self.bot.get_emoji(int(id_))
            if not emoji or not emoji.is_usable():
                content = content.replace(f'<{animated_}:{name_}:{id_}>', text)
            elif not invalid_only:
                    content = content.replace(f'<{animated_}:{name_}:{id_}>', text)
            else:
                continue
        return content
