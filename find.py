import openbbterminal
import pandas as pd

# Connect to the OpenBB Terminal API
ot = openbbterminal.OpenBBTerminal(api_key='YOUR_API_KEY', api_secret='YOUR_API_SECRET')

# Define your trading strategy
def simple_strategy(df):
    # Extract the bid and ask data from the orderbook
    bid_data = pd.DataFrame(df['bids'])
    ask_data = pd.DataFrame(df['asks'])
    
    # Calculate the bid-ask spread
    spread = ask_data.iloc[0]['price'] - bid_data.iloc[0]['price']
    
    # Place a buy order if the spread is less than 1 pip
    if spread < 0.0001:
        ot.place_order(pair='EURUSD', side='buy', quantity=1000, price=bid_data.iloc[0]['price'])
    
    # Place a sell order if the spread is greater than 2 pips
    elif spread > 0.0002:
        ot.place_order(pair='EURUSD', side='sell', quantity=1000, price=ask_data.iloc[0]['price'])

# Run the strategy on a loop
while True:
    # Get the latest orderbook data
    orderbook = ot.get_orderbook(pair='EURUSD')
    
    # Run the strategy on the orderbook data
    simple_strategy(orderbook)