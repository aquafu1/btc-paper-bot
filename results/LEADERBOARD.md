# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 7:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1343 windows, 35275 settled trades, 407 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 694 | 34.3 | 35.4 | $-528.07 | -7.6% | $471.93 | -1.5 | done | can't tell from luck |
| value_ev10 | 1700 | 38.8 | 39.2 | $-784.05 | -4.6% | $215.95 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3530 | 50.9 | 50.1 | $-979.40 | -2.8% | $20.60 | -1.6 | done | can't tell from luck |
| value_ev5 | 2566 | 40.5 | 41.1 | $-1289.90 | -5.0% | $-289.90 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2964 | 49.3 | 49.4 | $-1467.18 | -4.9% | $-467.18 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2964 | 50.7 | 50.9 | $-1533.36 | -5.2% | $-533.36 | -2.9 | done | losing for real |
| trend_filter | 2099 | 48.6 | 50.5 | $-1807.74 | -8.6% | $-807.74 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3530 | 49.1 | 50.3 | $-2246.71 | -6.4% | $-1246.71 | -3.8 | done | losing for real |
| coinflip | 5076 | 50.0 | 50.1 | $-2289.99 | -4.5% | $-1289.99 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5076 | 50.3 | 51.4 | $-3041.03 | -6.0% | $-2041.03 | -4.4 | done | losing for real |
| always_up | 5076 | 47.9 | 49.4 | $-3668.02 | -7.2% | $-2668.02 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8646 | 47.9 | 48.9 | $-5183.88 |
| ETH | 9319 | 48.2 | 48.2 | $-4867.33 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
