# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 5:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 854 windows, 23560 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 443 | 34.3 | 34.8 | $-255.60 | -5.8% | $744.40 | -0.9 | done | can't tell from luck |
| value_ev10 | 1078 | 37.8 | 39.0 | $-731.99 | -6.8% | $268.01 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1996 | 50.2 | 49.7 | $-784.87 | -3.9% | $215.13 | -1.8 | done | can't tell from luck |
| trend_filter | 1386 | 50.1 | 50.9 | $-892.50 | -6.4% | $107.50 | -2.5 | done | losing for real |
| reversal_15m_0.10pct | 2405 | 50.6 | 50.5 | $-980.60 | -4.1% | $19.40 | -2.0 | done | losing for real |
| value_ev5 | 1627 | 39.8 | 41.0 | $-1064.54 | -6.5% | $-64.54 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2405 | 49.4 | 50.4 | $-1390.59 | -5.8% | $-390.59 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 1996 | 49.8 | 51.1 | $-1480.37 | -7.4% | $-480.37 | -3.4 | done | losing for real |
| coinflip | 3408 | 50.2 | 50.3 | $-1519.21 | -4.5% | $-519.21 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3408 | 51.3 | 51.7 | $-1549.78 | -4.5% | $-549.78 | -2.7 | done | losing for real |
| always_up | 3408 | 46.9 | 49.5 | $-3311.80 | -9.7% | $-2311.80 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5367 | 48.3 | 49.0 | $-3002.91 |
| ETH | 5868 | 48.0 | 48.5 | $-3891.88 |
| SOL | 6144 | 48.2 | 48.5 | $-3655.94 |
| XRP | 6181 | 48.4 | 48.5 | $-3411.12 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
