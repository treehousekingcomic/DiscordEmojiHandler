import re
from typing import Union
import discord
from discord.ext import commands


class EmojiHandler:
    """The main EmojiHandler class."""

    def __init__(
        self, bot: Union[discord.Client, commands.Bot, commands.AutoShardedBot]
    ):
        """Initialize the emoji handler.

        Parameters
        ----------
        bot : Union[discord.Client, discord.ext.commands.Bot, commands.AutoShardedBot]
            the bot to handle emojis form
        """
        self.bot = bot
        self.emoji_regex = (
            r"<(?P<animated>a?):(?P<name>[a-zA-Z0-9_]{2,32}):(?P<id>[0-9]{18,22})>"
        )

    def check(self, content: str):
        """Return True if all emojis in the text are available to the bot, False if not.

        Parameters
        ----------
        content : str
            the text to get the emojis from

        Returns
        -------
        bool
            True if all emojis in the text are available to the bot, False if not.
        """
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

    def fix(self, content: str, colon=False):
        """Get the original content with the emojis that the bot can't see replaced with their name only.

        Parameters
        ----------
        content : str
            the text to fix the emojis from
        colon : bool, optional
            If this is True, invalid emojis have a colon (eg. :name:), by default False

        Returns
        -------
        str
            text with the emojis fixed
        """
        if not content:
            return None
        emojis = re.findall(self.emoji_regex, content)
        for result in emojis:
            animated_, name_, id_ = result

            emoji = self.bot.get_emoji(int(id_))
            if not emoji or not emoji.is_usable():
                content = content.replace(
                    f"<{animated_}:{name_}:{id_}>",
                    f'{name_ if not colon else ":" + name_ + ":"}',
                )
            else:
                continue
        return content

    def replace(self, content: str, text: str = "🤔", invalid_only=True):
        """Get the original content with invalid emojis replaced with text.

        Parameters
        ----------
        content : str
            the content to replace the original emojis from
        text : str, optional
            the text that the content should be replaced with, by default "🤔"
        invalid_only : bool, optional
            whether to only replace invalid or not, passing False will replace all emojis, by default True

        Returns
        -------
        str
            The original content with invalid emojis replaced with text
        """
        if not content:
            return None
        emojis = re.findall(self.emoji_regex, content)
        for result in emojis:
            animated_, name_, id_ = result

            emoji = self.bot.get_emoji(int(id_))
            if not emoji or not emoji.is_usable():
                content = content.replace(f"<{animated_}:{name_}:{id_}>", text)
            elif not invalid_only:
                content = content.replace(f"<{animated_}:{name_}:{id_}>", text)
            else:
                continue
        return content
