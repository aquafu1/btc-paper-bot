# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 1:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 838 windows, 23031 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 423 | 33.1 | 34.9 | $-400.80 | -9.5% | $599.20 | -1.5 | done | can't tell from luck |
| value_ev10 | 1048 | 37.2 | 39.1 | $-883.78 | -8.4% | $116.22 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 2353 | 50.9 | 50.6 | $-893.98 | -3.8% | $106.02 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1939 | 49.8 | 49.6 | $-933.55 | -4.8% | $66.45 | -2.1 | done | losing for real |
| trend_filter | 1356 | 49.7 | 50.8 | $-991.58 | -7.3% | $8.42 | -2.8 | done | losing for real |
| value_ev5 | 1588 | 39.5 | 41.1 | $-1167.89 | -7.4% | $-167.89 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1939 | 50.2 | 51.2 | $-1323.75 | -6.8% | $-323.75 | -3.1 | done | losing for real |
| coinflip | 3344 | 50.3 | 50.3 | $-1435.65 | -4.3% | $-435.65 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 2353 | 49.1 | 50.3 | $-1469.24 | -6.2% | $-469.24 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 3344 | 51.3 | 51.7 | $-1561.66 | -4.7% | $-561.66 | -2.8 | done | losing for real |
| always_up | 3344 | 47.2 | 49.6 | $-3125.12 | -9.3% | $-2125.12 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5233 | 48.1 | 49.1 | $-3342.40 |
| ETH | 5734 | 48.0 | 48.5 | $-3939.44 |
| SOL | 6007 | 48.2 | 48.6 | $-3542.51 |
| XRP | 6057 | 48.4 | 48.5 | $-3362.66 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
