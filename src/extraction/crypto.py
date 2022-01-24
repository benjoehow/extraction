


def get_crypto_candlestick_data(date, coin = "btc", interval = '60'):
    
    r = requests.get('https://api.cryptowat.ch/markets/kraken/btceur/ohlc', 
                 params = {'after': mt.get_nyse_open_timestamp(date = datetime(2021,12,7))})
    header = ["CloseTime", "OpenPrice", "HighPrice", "LowPrice", "ClosePrice", "Volume", "QuoteVolume"]
    
    ret = pd.DataFrame(r.json()['result']['60'], columns = header)
    
    return ret


