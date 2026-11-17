# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 9:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 631 windows, 17430 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1472 | 51.1 | 49.5 | $-191.57 | -1.3% | $808.43 | -0.5 | done | can't tell from luck |
| value_ev20 | 330 | 33.9 | 35.3 | $-274.70 | -8.3% | $725.30 | -1.2 | done | can't tell from luck |
| trend_filter | 1006 | 50.1 | 50.8 | $-573.57 | -5.7% | $426.43 | -1.8 | done | can't tell from luck |
| value_ev10 | 804 | 38.3 | 39.5 | $-575.74 | -7.2% | $424.26 | -1.7 | done | can't tell from luck |
| value_ev5 | 1218 | 40.6 | 41.4 | $-714.18 | -5.9% | $285.82 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1790 | 50.9 | 51.1 | $-825.65 | -4.6% | $174.35 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1790 | 49.1 | 49.9 | $-999.14 | -5.6% | $0.86 | -2.4 | done | losing for real |
| coinflip | 2516 | 50.1 | 50.5 | $-1195.22 | -4.8% | $-195.22 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1472 | 48.9 | 51.5 | $-1391.97 | -9.5% | $-391.97 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2516 | 50.4 | 51.7 | $-1552.53 | -6.2% | $-552.53 | -3.2 | done | losing for real |
| always_up | 2516 | 47.4 | 49.7 | $-2187.24 | -8.7% | $-1187.24 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3956 | 48.2 | 49.2 | $-2482.00 |
| ETH | 4360 | 48.2 | 48.6 | $-2645.57 |
| SOL | 4526 | 47.9 | 48.8 | $-3021.39 |
| XRP | 4588 | 48.5 | 48.5 | $-2332.55 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
