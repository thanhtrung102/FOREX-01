#from bot.bot import Bot
from infrastructure.instrument_collection import instrumentCollection
from stream_bot.stream_bot import run_bot

if __name__ == "__main__":
    instrumentCollection.LoadInstruments("./data")
    #b = Bot()
    #b.run()
    run_bot()