# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 3:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 797 windows, 21956 settled trades, 24 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 407 | 33.4 | 34.9 | $-339.14 | -8.3% | $660.86 | -1.3 | done | can't tell from luck |
| value_ev10 | 1004 | 37.8 | 39.2 | $-675.25 | -6.7% | $324.75 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1851 | 50.2 | 49.6 | $-678.05 | -3.7% | $321.95 | -1.6 | done | can't tell from luck |
| trend_filter | 1287 | 50.3 | 50.8 | $-727.79 | -5.7% | $272.21 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2245 | 50.8 | 50.6 | $-866.93 | -3.9% | $133.07 | -1.8 | done | can't tell from luck |
| value_ev5 | 1514 | 40.1 | 41.1 | $-880.98 | -5.8% | $119.02 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 2245 | 49.2 | 50.2 | $-1290.55 | -5.7% | $-290.55 | -2.7 | done | losing for real |
| coinflip | 3184 | 50.2 | 50.3 | $-1359.32 | -4.3% | $-359.32 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 3184 | 51.3 | 51.6 | $-1363.01 | -4.3% | $-363.01 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1851 | 49.8 | 51.2 | $-1364.97 | -7.4% | $-364.97 | -3.2 | done | losing for real |
| always_up | 3184 | 47.5 | 49.6 | $-2672.85 | -8.4% | $-1672.85 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4986 | 48.3 | 49.1 | $-2821.70 |
| ETH | 5473 | 48.2 | 48.5 | $-3423.23 |
| SOL | 5722 | 48.3 | 48.6 | $-3178.37 |
| XRP | 5775 | 48.5 | 48.5 | $-2795.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
