from pybit import WebSocket
import pandas as pd
import os
import time

subs = [
    "instrument_info.100ms.BTCUSD"
]
ws = WebSocket(
    "wss://stream-testnet.bybit.com/realtime",
    subscriptions=subs
)
while True:
    data = ws.fetch(subs[0])
    if data:
        timestamp = data['updated_at']
        oi = data['open_interest']
        #create dataframe with timestamp and open interest
        df = pd.DataFrame({'timestamp': [timestamp], 'oi': [oi]})
        #use timestamp as index
        df.set_index('timestamp', inplace=True)
        #if csv exists already then append to it
        if os.path.isfile('wsoi.csv'):
            df.to_csv('wsoi.csv', mode='a', header=False)
        #if csv doesn't exist then create it
        else:
            df.to_csv('wsoi.csv')
        #print dataframe
        print(df)
    #wait 10 seconds
    time.sleep(10)

