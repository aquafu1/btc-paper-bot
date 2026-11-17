# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 11:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 591 windows, 16353 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1387 | 51.2 | 49.6 | $-209.29 | -1.5% | $790.71 | -0.6 | done | can't tell from luck |
| value_ev20 | 321 | 34.0 | 35.2 | $-276.40 | -8.6% | $723.60 | -1.2 | done | can't tell from luck |
| trend_filter | 950 | 50.1 | 51.0 | $-564.37 | -5.9% | $435.63 | -1.9 | done | can't tell from luck |
| value_ev10 | 769 | 37.7 | 39.4 | $-655.17 | -8.5% | $344.83 | -2.0 | done | can't tell from luck |
| value_ev5 | 1149 | 40.3 | 41.2 | $-744.66 | -6.5% | $255.34 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1661 | 50.9 | 51.0 | $-773.95 | -4.7% | $226.05 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1661 | 49.1 | 49.9 | $-969.40 | -5.8% | $30.60 | -2.4 | done | losing for real |
| coinflip | 2356 | 49.9 | 50.5 | $-1218.58 | -5.2% | $-218.58 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1387 | 48.8 | 51.3 | $-1342.41 | -9.7% | $-342.41 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2356 | 50.0 | 51.8 | $-1693.91 | -7.2% | $-693.91 | -3.6 | done | losing for real |
| always_up | 2356 | 47.5 | 49.7 | $-2076.92 | -8.8% | $-1076.92 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3710 | 47.9 | 49.2 | $-2570.74 |
| ETH | 4079 | 48.0 | 48.5 | $-2623.95 |
| SOL | 4253 | 47.8 | 48.7 | $-3022.65 |
| XRP | 4311 | 48.5 | 48.6 | $-2307.73 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
