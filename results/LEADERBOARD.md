# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 9:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 870 windows, 23996 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 452 | 35.6 | 34.9 | $-106.41 | -2.4% | $893.59 | -0.4 | done | can't tell from luck |
| value_ev10 | 1100 | 38.5 | 39.1 | $-555.43 | -5.0% | $444.57 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 2028 | 50.0 | 49.7 | $-855.96 | -4.2% | $144.04 | -1.9 | done | can't tell from luck |
| value_ev5 | 1662 | 40.1 | 41.0 | $-917.83 | -5.5% | $82.17 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2450 | 50.6 | 50.5 | $-936.95 | -3.8% | $63.05 | -1.9 | done | can't tell from luck |
| trend_filter | 1410 | 49.9 | 50.9 | $-982.42 | -7.0% | $17.58 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2028 | 50.0 | 51.0 | $-1355.60 | -6.7% | $-355.60 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2450 | 49.4 | 50.4 | $-1389.65 | -5.7% | $-389.65 | -2.8 | done | losing for real |
| coinflip | 3472 | 50.1 | 50.3 | $-1534.93 | -4.4% | $-534.93 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3472 | 51.1 | 51.7 | $-1666.97 | -4.8% | $-666.97 | -2.9 | done | losing for real |
| always_up | 3472 | 46.9 | 49.6 | $-3367.85 | -9.7% | $-2367.85 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5474 | 48.3 | 49.0 | $-2919.52 |
| ETH | 5969 | 48.1 | 48.5 | $-3844.01 |
| SOL | 6261 | 48.3 | 48.6 | $-3458.27 |
| XRP | 6292 | 48.3 | 48.5 | $-3448.18 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
