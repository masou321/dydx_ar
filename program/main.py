from func_private import abort_all_positions
from constants import ABORT_ALL_POSITIONS, FIND_COINTEGRATED
from func_connections import connect_dydx
from func_public import construct_market_prices

if __name__ == "__main__":
  # Connect to client
  try:
    print("Connect to client...")
    client = connect_dydx()
  except Exception as exp:
    print("Error connecting to client: ", exp)
    exit(1)

  # Abort all open positions
  if ABORT_ALL_POSITIONS:
    try:
      print("Closing all positions...")
      close_orders = abort_all_positions(client)
    except Exception as exp:
      print("Error closing all positions: ", exp)
      exit(1)

  # Find Cointegrated Paires
  if FIND_COINTEGRATED:
    try:
      print("Fetching market prices ,please allow 3 mins... ")
      df_market_prices = construct_market_prices(client)
    except Exception as exp:
      print("Error cunstructing market prices: ", exp)
      exit(1)