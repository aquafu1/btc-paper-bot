# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 12:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 496 windows, 13646 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 254 | 33.9 | 35.5 | $-219.21 | -8.6% | $780.79 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1159 | 51.1 | 49.9 | $-223.22 | -1.9% | $776.78 | -0.7 | done | can't tell from luck |
| value_ev10 | 643 | 38.1 | 39.8 | $-510.56 | -7.9% | $489.44 | -1.7 | done | can't tell from luck |
| trend_filter | 802 | 49.8 | 50.8 | $-532.23 | -6.6% | $467.77 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1376 | 49.6 | 49.7 | $-588.77 | -4.3% | $411.23 | -1.6 | done | can't tell from luck |
| value_ev5 | 949 | 40.4 | 41.6 | $-636.78 | -6.7% | $363.22 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1376 | 50.4 | 51.6 | $-907.23 | -6.6% | $92.77 | -2.5 | done | losing for real |
| coinflip | 1976 | 50.1 | 50.7 | $-1035.14 | -5.2% | $-35.14 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1159 | 48.9 | 51.4 | $-1065.31 | -9.2% | $-65.31 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1976 | 49.8 | 51.6 | $-1444.78 | -7.3% | $-444.78 | -3.4 | done | losing for real |
| always_up | 1976 | 46.3 | 50.2 | $-2358.52 | -11.9% | $-1358.52 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3075 | 47.3 | 49.3 | $-2535.38 |
| ETH | 3420 | 48.0 | 48.7 | $-2288.85 |
| SOL | 3559 | 47.7 | 49.1 | $-2653.80 |
| XRP | 3592 | 48.4 | 48.8 | $-2043.74 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
