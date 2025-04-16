from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
from simulation.ma_cross import run_ma_sim
from simulation.ema_macd_mp import run_ema_macd
from simulation.ema_macd_mp import run_process
from dateutil import parser
from infrastructure.collect_data import run_collection
#from api.stream_prices import stream_prices
from stream_example.streamer import run_streamer
from db.db import DataDB

def db_tests():
    d = DataDB()

    #d.add_one(DataDB.SAMPLE_COLL, dict(age=12, name='paddy', street='elm'))
    #print(d.query_single(DataDB.SAMPLE_COLL, age=34))
    print(d.query_distinct(DataDB.SAMPLE_COLL, 'age'))

if __name__ == '__main__':
    api = OandaApi()
    #print(api.fetch_candles("EUR_USD", granularity = "D", price = "MB"))

    #dfr = parser.parse("2024-04-21T01:00:00Z")
    #dto = parser.parse("2024-04-29T16:00:00Z")

    #df_candles = api.get_candles_df("EUR_USD", granularity = "H1", 
                                    #date_f = dfr, date_t = dto)

    #print(df_candles.head())
    #print()
    #print(df_candles.tail())
    #data = api.get_account_summary()
    #print(data)

    #instrumentCollection.CreateFile(api.get_instruments())
    #instrumentCollection.LoadInstruments("./data")
    #instrumentCollection.PrintInstruments() 
    #run_ma_sim(curr_list=["EUR", "USD", "GBP", "JPY", "AUD", "CAD"])

    #instrumentCollection.LoadInstruments("./data")
    #run_collection(instrumentCollection, api)
    #run_ma_sim()
    #run_process(instrumentCollection)
    #run_ema_macd(instrumentCollection)    
    
    #stream_prices(['GBP_JPY', 'AUD_NZD'])
    #run_streamer()
    #d = DataDB()
    #d.test_connection()
    #instrumentCollection.CreateDB(api.get_account_instruments())
    instrumentCollection.LoadInstrumentsDB()
    print(instrumentCollection.instruments_dict)
    #d.test_connection()
    #db_tests()
