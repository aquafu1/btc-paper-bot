# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 1:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 453 windows, 12425 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 227 | 34.8 | 36.0 | $-152.39 | -6.7% | $847.61 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1053 | 51.2 | 50.0 | $-209.67 | -2.0% | $790.33 | -0.7 | done | can't tell from luck |
| value_ev10 | 585 | 38.8 | 40.1 | $-391.01 | -6.7% | $608.99 | -1.3 | done | can't tell from luck |
| trend_filter | 716 | 49.9 | 50.7 | $-407.75 | -5.7% | $592.25 | -1.6 | done | can't tell from luck |
| value_ev5 | 867 | 40.9 | 41.9 | $-505.69 | -5.8% | $494.31 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1256 | 49.8 | 50.0 | $-517.80 | -4.1% | $482.20 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1256 | 50.2 | 51.6 | $-872.72 | -6.9% | $127.28 | -2.6 | done | losing for real |
| coinflip | 1804 | 49.8 | 50.8 | $-1024.38 | -5.7% | $-24.38 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1053 | 48.8 | 51.7 | $-1041.76 | -9.9% | $-41.76 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 1804 | 49.4 | 51.5 | $-1362.97 | -7.6% | $-362.97 | -3.3 | done | losing for real |
| always_up | 1804 | 46.0 | 50.6 | $-2329.09 | -12.9% | $-1329.09 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2805 | 47.5 | 49.3 | $-2266.44 |
| ETH | 3122 | 47.9 | 48.8 | $-2108.21 |
| SOL | 3234 | 47.6 | 49.3 | $-2549.45 |
| XRP | 3264 | 48.4 | 49.2 | $-1891.14 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
