from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
from simulation.ma_cross import run_ma_sim
from dateutil import parser
from infrastructure.collect_data import run_collection

if __name__ == '__main__':
    api = OandaApi()
    print(api.fetch_candles("EUR_USD", granularity = "D", price = "MB"))

    #data = api.get_account_summary()
    #print(data)

    #instrumentCollection.CreateFile(api.get_instruments())
    #instrumentCollection.LoadInstruments("./data")
    #instrumentCollection.PrintInstruments() 
    #run_ma_sim(curr_list=["EUR", "USD", "GBP", "JPY", "AUD", "CAD"])

    #instrumentCollection.LoadInstruments("./data")
    #run_collection(instrumentCollection, api)
    run_ma_sim()


