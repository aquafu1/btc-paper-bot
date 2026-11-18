# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 6:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 664 windows, 18373 settled trades, 29 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 343 | 34.1 | 35.4 | $-267.49 | -7.8% | $732.51 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1561 | 50.5 | 49.6 | $-397.13 | -2.5% | $602.87 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1885 | 51.5 | 50.9 | $-562.55 | -3.0% | $437.45 | -1.3 | done | can't tell from luck |
| trend_filter | 1065 | 50.4 | 51.0 | $-575.94 | -5.4% | $424.06 | -1.8 | done | can't tell from luck |
| value_ev10 | 844 | 38.2 | 39.5 | $-631.06 | -7.5% | $368.94 | -1.8 | done | can't tell from luck |
| value_ev5 | 1276 | 40.6 | 41.4 | $-746.42 | -5.8% | $253.58 | -1.8 | done | can't tell from luck |
| coinflip | 2651 | 50.2 | 50.4 | $-1171.36 | -4.4% | $-171.36 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1561 | 49.5 | 51.3 | $-1255.73 | -8.0% | $-255.73 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 1885 | 48.5 | 50.0 | $-1306.96 | -6.9% | $-306.96 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2651 | 50.8 | 51.8 | $-1447.89 | -5.5% | $-447.89 | -2.9 | done | losing for real |
| always_up | 2651 | 47.6 | 49.7 | $-2170.01 | -8.2% | $-1170.01 | -4.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4174 | 48.3 | 49.3 | $-2576.62 |
| ETH | 4585 | 48.2 | 48.7 | $-2870.07 |
| SOL | 4784 | 48.2 | 48.8 | $-2795.01 |
| XRP | 4830 | 48.6 | 48.6 | $-2290.84 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
