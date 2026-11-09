"""Settings for the paper bot. All money here is FAKE."""

WINDOW_SECONDS = 15 * 60          # Polymarket "BTC Up or Down" 15-minute markets

STARTING_BANKROLL = 1000.00       # fake dollars per strategy
STAKE = 10.00                     # fake dollars per trade

# Price assumptions (used in backtests, and live only if Polymarket odds can't be fetched)
SIM_ENTRY_PRICE = 0.51            # pay 51c for a share that pays $1 if right (50c + 1c spread)

# Estimated taker fee as a fraction of the stake. Polymarket's fee rules for these
# markets can change -- check their docs and update this if needed.
FEE_RATE = 0.015

# Live: only enter a window if we're this early into it.
# With a real Polymarket price we can enter later (the price already reflects the move).
MAX_ENTRY_DELAY_REAL_PRICE = 10 * 60
MAX_ENTRY_DELAY_SIM_PRICE = 2 * 60

COINBASE_PRODUCT = "BTC-USD"
POLY_SLUG_TEMPLATE = "btc-updown-15m-{start}"   # window start as unix seconds
