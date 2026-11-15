# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 8:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 433 windows, 11887 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 214 | 34.6 | 36.2 | $-174.42 | -8.2% | $825.58 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1013 | 50.7 | 50.0 | $-273.64 | -2.7% | $726.36 | -0.9 | done | can't tell from luck |
| value_ev10 | 556 | 39.0 | 40.3 | $-375.64 | -6.8% | $624.36 | -1.3 | done | can't tell from luck |
| trend_filter | 682 | 49.7 | 50.7 | $-407.02 | -6.0% | $592.98 | -1.6 | done | can't tell from luck |
| value_ev5 | 833 | 41.3 | 42.1 | $-461.13 | -5.5% | $538.87 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1202 | 49.3 | 50.0 | $-615.02 | -5.1% | $384.98 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1202 | 50.7 | 51.7 | $-728.85 | -6.1% | $271.15 | -2.2 | done | losing for real |
| coinflip | 1724 | 50.5 | 50.9 | $-768.47 | -4.5% | $231.53 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 1013 | 49.3 | 51.9 | $-927.25 | -9.2% | $72.75 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 1724 | 49.6 | 51.6 | $-1270.34 | -7.4% | $-270.34 | -3.2 | done | losing for real |
| always_up | 1724 | 46.2 | 50.5 | $-2107.59 | -12.2% | $-1107.59 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2684 | 47.6 | 49.4 | $-2034.74 |
| ETH | 2983 | 48.0 | 48.9 | $-1908.30 |
| SOL | 3085 | 47.8 | 49.4 | $-2409.94 |
| XRP | 3135 | 48.7 | 49.3 | $-1756.39 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
