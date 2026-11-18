# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 9:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 724 windows, 19917 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 381 | 33.3 | 34.9 | $-334.03 | -8.8% | $665.97 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 2039 | 51.7 | 50.8 | $-448.85 | -2.2% | $551.15 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1666 | 49.9 | 49.5 | $-612.73 | -3.7% | $387.27 | -1.5 | done | can't tell from luck |
| value_ev10 | 915 | 37.9 | 39.1 | $-622.90 | -6.8% | $377.10 | -1.7 | done | can't tell from luck |
| value_ev5 | 1380 | 40.7 | 41.1 | $-687.96 | -5.0% | $312.04 | -1.6 | done | can't tell from luck |
| trend_filter | 1167 | 50.0 | 50.9 | $-708.12 | -6.1% | $291.88 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1666 | 50.1 | 51.3 | $-1153.55 | -6.9% | $-153.55 | -2.9 | done | losing for real |
| coinflip | 2888 | 50.2 | 50.3 | $-1211.87 | -4.2% | $-211.87 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 2039 | 48.3 | 50.0 | $-1493.92 | -7.3% | $-493.92 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 2888 | 51.0 | 51.8 | $-1502.09 | -5.2% | $-502.09 | -2.9 | done | losing for real |
| always_up | 2888 | 47.2 | 49.6 | $-2577.99 | -8.9% | $-1577.99 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4505 | 48.1 | 49.1 | $-2817.74 |
| ETH | 4961 | 48.2 | 48.5 | $-3038.02 |
| SOL | 5192 | 48.1 | 48.7 | $-3066.48 |
| XRP | 5259 | 48.6 | 48.4 | $-2431.76 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
