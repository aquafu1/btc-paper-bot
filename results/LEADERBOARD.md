# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 8:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 241 windows, 6283 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 619 | 56.5 | 52.3 | $+270.09 | +4.4% | $1270.09 | +1.2 | done | can't tell from luck |
| reversal_60m_0.30pct | 492 | 54.7 | 52.4 | $+36.01 | +0.7% | $1036.01 | +0.2 | done | can't tell from luck |
| value_ev20 | 114 | 34.2 | 36.7 | $-120.27 | -10.6% | $879.73 | -0.9 | Sun 9:00 AM | too few trades (114/200) |
| value_ev10 | 306 | 37.6 | 40.8 | $-353.26 | -11.5% | $646.74 | -1.7 | done | can't tell from luck |
| trend_filter | 328 | 45.1 | 50.3 | $-460.59 | -14.0% | $539.41 | -2.6 | done | losing for real |
| value_ev5 | 445 | 39.3 | 42.4 | $-500.33 | -11.2% | $499.67 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 492 | 45.3 | 49.7 | $-637.93 | -13.0% | $362.07 | -2.9 | done | losing for real |
| coinflip | 956 | 49.6 | 50.9 | $-661.73 | -6.9% | $338.27 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 956 | 50.0 | 51.6 | $-676.27 | -7.1% | $323.73 | -2.3 | done | losing for real |
| always_up | 956 | 47.6 | 50.5 | $-957.85 | -10.0% | $42.15 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 619 | 43.5 | 49.8 | $-1012.17 | -16.4% | $-12.17 | -4.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1405 | 46.5 | 49.7 | $-1448.78 |
| ETH | 1568 | 46.6 | 49.0 | $-1603.26 |
| SOL | 1620 | 48.3 | 49.4 | $-1237.67 |
| XRP | 1690 | 49.1 | 49.2 | $-784.59 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
