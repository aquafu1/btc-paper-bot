# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 8:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 722 windows, 19878 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 380 | 33.4 | 34.9 | $-324.03 | -8.5% | $675.97 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 2035 | 51.6 | 50.8 | $-509.40 | -2.5% | $490.60 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1664 | 50.0 | 49.5 | $-592.73 | -3.6% | $407.27 | -1.4 | done | can't tell from luck |
| value_ev10 | 914 | 38.0 | 39.1 | $-612.90 | -6.7% | $387.10 | -1.7 | done | can't tell from luck |
| trend_filter | 1163 | 50.2 | 50.9 | $-668.12 | -5.7% | $331.88 | -2.0 | done | losing for real |
| value_ev5 | 1377 | 40.7 | 41.1 | $-676.89 | -4.9% | $323.11 | -1.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 1664 | 50.0 | 51.3 | $-1194.33 | -7.2% | $-194.33 | -3.0 | done | losing for real |
| coinflip | 2882 | 50.2 | 50.3 | $-1248.49 | -4.3% | $-248.49 | -2.3 | done | losing for real |
| momentum_5m_0.00pct | 2882 | 51.1 | 51.8 | $-1442.09 | -5.0% | $-442.09 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2035 | 48.4 | 50.0 | $-1453.92 | -7.1% | $-453.92 | -3.2 | done | losing for real |
| always_up | 2882 | 47.2 | 49.5 | $-2547.58 | -8.8% | $-1547.58 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4496 | 48.1 | 49.1 | $-2799.44 |
| ETH | 4955 | 48.2 | 48.5 | $-3015.89 |
| SOL | 5176 | 48.2 | 48.7 | $-3023.31 |
| XRP | 5251 | 48.6 | 48.4 | $-2431.84 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
