# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 4:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 994 windows, 27630 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 505 | 34.3 | 34.9 | $-285.26 | -5.6% | $714.74 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2818 | 51.0 | 50.4 | $-900.75 | -3.2% | $99.25 | -1.7 | done | can't tell from luck |
| value_ev10 | 1260 | 37.5 | 39.1 | $-911.38 | -7.2% | $88.62 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2378 | 49.7 | 49.7 | $-1126.76 | -4.7% | $-126.76 | -2.3 | done | losing for real |
| trend_filter | 1659 | 49.5 | 50.8 | $-1244.66 | -7.5% | $-244.66 | -3.1 | done | losing for real |
| value_ev5 | 1910 | 39.5 | 41.0 | $-1294.56 | -6.8% | $-294.56 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2378 | 50.3 | 50.9 | $-1525.71 | -6.4% | $-525.71 | -3.2 | done | losing for real |
| coinflip | 3968 | 50.3 | 50.3 | $-1775.17 | -4.5% | $-775.17 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2818 | 49.0 | 50.4 | $-1874.40 | -6.7% | $-874.40 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 3968 | 50.8 | 51.5 | $-2143.26 | -5.4% | $-1143.26 | -3.5 | done | losing for real |
| always_up | 3968 | 46.8 | 49.6 | $-3956.07 | -10.0% | $-2956.07 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6299 | 48.2 | 49.1 | $-3549.44 |
| ETH | 6863 | 48.0 | 48.5 | $-4495.65 |
| SOL | 7220 | 48.1 | 48.6 | $-4313.31 |
| XRP | 7248 | 48.0 | 48.4 | $-4679.59 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
