# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 1:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 935 windows, 25851 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 476 | 35.1 | 34.8 | $-155.74 | -3.3% | $844.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1168 | 38.0 | 39.1 | $-683.12 | -5.8% | $316.88 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 2206 | 50.2 | 49.8 | $-912.47 | -4.1% | $87.53 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2642 | 50.9 | 50.6 | $-927.31 | -3.5% | $72.69 | -1.8 | done | can't tell from luck |
| trend_filter | 1538 | 50.1 | 51.0 | $-1040.73 | -6.8% | $-40.73 | -2.7 | done | losing for real |
| value_ev5 | 1777 | 39.7 | 41.0 | $-1129.62 | -6.4% | $-129.62 | -2.3 | done | losing for real |
| coinflip | 3732 | 50.4 | 50.4 | $-1547.93 | -4.1% | $-547.93 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2206 | 49.8 | 50.9 | $-1567.30 | -7.1% | $-567.30 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 2642 | 49.1 | 50.3 | $-1661.55 | -6.3% | $-661.55 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 3732 | 51.0 | 51.6 | $-1879.49 | -5.0% | $-879.49 | -3.2 | done | losing for real |
| always_up | 3732 | 46.7 | 49.7 | $-3872.31 | -10.4% | $-2872.31 | -6.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5894 | 48.1 | 49.1 | $-3486.04 |
| ETH | 6428 | 48.2 | 48.6 | $-4047.54 |
| SOL | 6744 | 48.2 | 48.6 | $-3971.56 |
| XRP | 6785 | 48.3 | 48.5 | $-3872.41 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
