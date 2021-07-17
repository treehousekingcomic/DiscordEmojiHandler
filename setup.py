from distutils.core import setup

setup(
    name="DiscordEmojiHandler",  # How you named your package folder (MyLib)
    packages=["DiscordEmojiHandler"],  # Chose the same as "name"
    version="1.8",  # Start with a small number and increase it with every change you make
    license="MIT",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="Work with messages that contain emojis that your bot can't see? Emoji Handler will take care of the problem.",  # Give a short description about your library
    author="Ali S.",  # Type in your name
    author_email="discordemojihandler@thkc.space",  # Type in your E-Mail
    url="https://github.com/treehousekingcomic/DiscordEmojiHandler",  # Provide either the link to your github or to your website
    download_url="https://github.com/treehousekingcomic/DiscordEmojiHandler/archive/v1.8.tar.gz",  # I explain this later on
    keywords=[
        "discord.py",
        "emojis",
        "handler",
    ],  # Keywords that define your package best
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3",  # Specify which python versions that you want to support
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
