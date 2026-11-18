# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 8:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 723 windows, 19889 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 381 | 33.3 | 34.9 | $-334.03 | -8.8% | $665.97 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 2035 | 51.6 | 50.8 | $-509.40 | -2.5% | $490.60 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1664 | 50.0 | 49.5 | $-592.73 | -3.6% | $407.27 | -1.4 | done | can't tell from luck |
| value_ev10 | 915 | 37.9 | 39.1 | $-622.90 | -6.8% | $377.10 | -1.7 | done | can't tell from luck |
| value_ev5 | 1378 | 40.6 | 41.1 | $-686.89 | -5.0% | $313.11 | -1.6 | done | can't tell from luck |
| trend_filter | 1165 | 50.1 | 50.9 | $-688.12 | -5.9% | $311.88 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1664 | 50.0 | 51.3 | $-1194.33 | -7.2% | $-194.33 | -3.0 | done | losing for real |
| coinflip | 2884 | 50.2 | 50.3 | $-1253.48 | -4.3% | $-253.48 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 2035 | 48.4 | 50.0 | $-1453.92 | -7.1% | $-453.92 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2884 | 51.0 | 51.8 | $-1462.09 | -5.1% | $-462.09 | -2.8 | done | losing for real |
| always_up | 2884 | 47.2 | 49.5 | $-2537.99 | -8.8% | $-1537.99 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4500 | 48.1 | 49.1 | $-2809.43 |
| ETH | 4955 | 48.2 | 48.5 | $-3015.89 |
| SOL | 5183 | 48.1 | 48.7 | $-3078.73 |
| XRP | 5251 | 48.6 | 48.4 | $-2431.84 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
