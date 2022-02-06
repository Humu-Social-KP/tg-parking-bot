import logging
from parking_bot.runner import BotRunner
from parking_bot.settings import BOT_TOKEN

logging.basicConfig(level=logging.DEBUG)

runner = BotRunner(BOT_TOKEN)
runner.setup()


if __name__ == '__main__':
    runner.run_bot()
