# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 9:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 772 windows, 21296 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 403 | 33.0 | 34.9 | $-381.45 | -9.5% | $618.55 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2174 | 51.2 | 50.6 | $-632.29 | -2.9% | $367.71 | -1.4 | done | can't tell from luck |
| value_ev10 | 976 | 37.6 | 39.1 | $-714.62 | -7.3% | $285.38 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1799 | 49.8 | 49.6 | $-764.23 | -4.2% | $235.77 | -1.8 | done | can't tell from luck |
| trend_filter | 1249 | 49.7 | 50.8 | $-840.45 | -6.7% | $159.55 | -2.4 | done | losing for real |
| value_ev5 | 1476 | 39.9 | 41.0 | $-934.74 | -6.3% | $65.26 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1799 | 50.2 | 51.2 | $-1176.18 | -6.5% | $-176.18 | -2.8 | done | losing for real |
| coinflip | 3082 | 50.3 | 50.3 | $-1275.06 | -4.1% | $-275.06 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 2174 | 48.8 | 50.2 | $-1461.63 | -6.7% | $-461.63 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 3082 | 51.0 | 51.6 | $-1529.15 | -5.0% | $-529.15 | -2.8 | done | losing for real |
| always_up | 3082 | 47.0 | 49.5 | $-2835.64 | -9.2% | $-1835.64 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4831 | 48.2 | 49.1 | $-2918.08 |
| ETH | 5313 | 47.9 | 48.5 | $-3615.14 |
| SOL | 5547 | 48.0 | 48.5 | $-3279.54 |
| XRP | 5605 | 48.5 | 48.4 | $-2732.68 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
