# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 5:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1431 windows, 36544 settled trades, 438 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 737 | 34.6 | 35.3 | $-503.47 | -6.8% | $496.53 | -1.4 | done | can't tell from luck |
| value_ev10 | 1776 | 38.8 | 39.1 | $-801.46 | -4.5% | $198.54 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3648 | 50.9 | 50.0 | $-971.29 | -2.7% | $28.71 | -1.6 | done | can't tell from luck |
| value_ev5 | 2678 | 40.6 | 41.1 | $-1285.90 | -4.8% | $-285.90 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3064 | 49.2 | 49.3 | $-1512.27 | -4.9% | $-512.27 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3064 | 50.8 | 51.0 | $-1568.70 | -5.1% | $-568.70 | -2.9 | done | losing for real |
| trend_filter | 2170 | 48.6 | 50.4 | $-1882.71 | -8.7% | $-882.71 | -4.1 | done | losing for real |
| coinflip | 5253 | 50.1 | 50.0 | $-2186.39 | -4.2% | $-1186.39 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 3648 | 49.1 | 50.2 | $-2269.92 | -6.2% | $-1269.92 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5253 | 50.2 | 51.4 | $-3236.31 | -6.2% | $-2236.31 | -4.6 | done | losing for real |
| always_up | 5253 | 48.0 | 49.2 | $-3609.76 | -6.9% | $-2609.76 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9268 | 48.1 | 48.7 | $-4850.44 |
| ETH | 9966 | 48.0 | 48.0 | $-5393.50 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
