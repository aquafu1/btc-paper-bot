# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 12:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 497 windows, 13670 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1160 | 51.1 | 49.9 | $-216.49 | -1.9% | $783.51 | -0.6 | done | can't tell from luck |
| value_ev20 | 254 | 33.9 | 35.5 | $-219.21 | -8.6% | $780.79 | -1.0 | done | can't tell from luck |
| value_ev10 | 643 | 38.1 | 39.8 | $-510.56 | -7.9% | $489.44 | -1.7 | done | can't tell from luck |
| trend_filter | 803 | 49.8 | 50.8 | $-525.50 | -6.5% | $474.50 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1380 | 49.8 | 49.7 | $-556.34 | -4.0% | $443.66 | -1.5 | done | can't tell from luck |
| value_ev5 | 950 | 40.3 | 41.6 | $-646.78 | -6.8% | $353.22 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1380 | 50.2 | 51.6 | $-947.23 | -6.9% | $52.77 | -2.6 | done | losing for real |
| coinflip | 1980 | 50.1 | 50.7 | $-1034.84 | -5.2% | $-34.84 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1160 | 48.9 | 51.4 | $-1075.31 | -9.3% | $-75.31 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1980 | 49.8 | 51.6 | $-1449.11 | -7.3% | $-449.11 | -3.4 | done | losing for real |
| always_up | 1980 | 46.2 | 50.2 | $-2398.52 | -12.1% | $-1398.52 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3080 | 47.3 | 49.3 | $-2542.64 |
| ETH | 3425 | 48.0 | 48.7 | $-2282.04 |
| SOL | 3565 | 47.7 | 49.1 | $-2698.40 |
| XRP | 3600 | 48.4 | 48.8 | $-2056.80 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
