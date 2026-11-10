"""Settings for the paper bot. All money here is FAKE."""

WINDOW_SECONDS = 15 * 60          # Polymarket "<coin> Up or Down" 15-minute markets

STARTING_BANKROLL = 1000.00       # fake dollars per strategy
STAKE = 10.00                     # fake dollars per trade

# Coins traded. Each has its own 15-min Polymarket market and Coinbase price feed.
COINS = ["btc", "eth", "sol", "xrp"]
COINBASE_PRODUCT = {"btc": "BTC-USD", "eth": "ETH-USD", "sol": "SOL-USD", "xrp": "XRP-USD"}
POLY_SLUG_TEMPLATE = "{coin}-updown-15m-{start}"   # window start as unix seconds

# Polymarket taker fee (docs.polymarket.com/trading/fees, confirmed from each market's
# feeSchedule on Nov 10 2026): fee in $ = shares * rate * (p * (1 - p)) ** exponent,
# collected in shares on buys. The live bot reads the real numbers from each market;
# these are only the fallback and the backtest assumption.
FEE_RATE = 0.07
FEE_EXPONENT = 1

# Backtest only: assumed price paid per share (50c + 1c spread).
SIM_ENTRY_PRICE = 0.51

# Live timing. The strategies only look at candles that closed BEFORE the window,
# so the bot buys right after the window opens, while the price is still near 50c.
ENTRY_DELAY = 20                  # seconds after window start to place the paper trades
MAX_ENTRY_DELAY = 120             # later than this, skip the window (price already moved)
SETTLE_DELAY = 150                # seconds after window start: second check, to settle the
                                  # window that just ended (Polymarket resolves ~80s after the end)
MIN_SHARES = 5                    # Polymarket's minimum order size

# The GitHub job runs a loop for this long, then starts a fresh job (6h max per job).
LOOP_SECONDS = int(5.5 * 3600)

# A strategy needs this many settled trades before its result means anything.
MIN_TRADES = 200
