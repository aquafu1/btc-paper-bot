# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 5:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1381 windows, 35819 settled trades, 402 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 718 | 34.4 | 35.3 | $-534.88 | -7.4% | $465.12 | -1.5 | done | can't tell from luck |
| value_ev10 | 1740 | 38.7 | 39.2 | $-813.93 | -4.7% | $186.07 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3578 | 50.8 | 50.1 | $-1046.85 | -2.9% | $-46.85 | -1.7 | done | can't tell from luck |
| value_ev5 | 2618 | 40.4 | 41.1 | $-1326.02 | -5.1% | $-326.02 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 3002 | 49.2 | 49.3 | $-1496.56 | -5.0% | $-496.56 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3002 | 50.8 | 50.9 | $-1528.09 | -5.1% | $-528.09 | -2.9 | done | losing for real |
| trend_filter | 2127 | 48.5 | 50.4 | $-1900.19 | -8.9% | $-900.19 | -4.2 | done | losing for real |
| coinflip | 5152 | 50.1 | 50.0 | $-2189.16 | -4.2% | $-1189.16 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3578 | 49.2 | 50.2 | $-2190.42 | -6.1% | $-1190.42 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 5152 | 50.1 | 51.3 | $-3211.72 | -6.2% | $-2211.72 | -4.6 | done | losing for real |
| always_up | 5152 | 47.9 | 49.3 | $-3674.92 | -7.1% | $-2674.92 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8910 | 47.9 | 48.8 | $-5099.29 |
| ETH | 9599 | 48.1 | 48.1 | $-5229.22 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
