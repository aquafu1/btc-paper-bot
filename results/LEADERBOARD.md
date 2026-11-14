# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 4:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 323 windows, 8648 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 700 | 53.3 | 51.7 | $-84.58 | -1.2% | $915.42 | -0.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 861 | 53.0 | 51.9 | $-193.41 | -2.2% | $806.59 | -0.7 | done | can't tell from luck |
| value_ev20 | 163 | 33.7 | 36.8 | $-212.09 | -13.0% | $787.91 | -1.3 | Sun 12:00 AM | too few trades (163/200) |
| value_ev10 | 414 | 37.7 | 40.5 | $-459.41 | -11.1% | $540.59 | -1.9 | done | can't tell from luck |
| value_ev5 | 621 | 39.6 | 42.2 | $-645.19 | -10.4% | $354.81 | -2.3 | done | losing for real |
| trend_filter | 476 | 45.0 | 50.4 | $-718.15 | -15.1% | $281.85 | -3.4 | done | losing for real |
| momentum_60m_0.30pct | 700 | 46.7 | 49.9 | $-776.76 | -11.1% | $223.24 | -3.0 | done | losing for real |
| coinflip | 1284 | 50.0 | 51.0 | $-782.60 | -6.1% | $217.40 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 861 | 47.0 | 49.8 | $-835.74 | -9.7% | $164.26 | -2.9 | done | losing for real |
| always_up | 1284 | 47.7 | 50.5 | $-1228.48 | -9.6% | $-228.48 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 1284 | 48.4 | 51.4 | $-1284.74 | -10.0% | $-284.74 | -3.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1938 | 46.3 | 49.3 | $-2014.33 |
| ETH | 2172 | 46.8 | 48.8 | $-2138.02 |
| SOL | 2252 | 48.0 | 49.4 | $-1794.00 |
| XRP | 2286 | 48.7 | 49.2 | $-1274.80 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
