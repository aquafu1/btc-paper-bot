# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 11:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 255 windows, 6680 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 662 | 55.4 | 52.3 | $+127.72 | +1.9% | $1127.72 | +0.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 532 | 53.4 | 52.0 | $-73.79 | -1.4% | $926.21 | -0.3 | done | can't tell from luck |
| value_ev20 | 119 | 33.6 | 36.7 | $-141.51 | -11.9% | $858.49 | -1.0 | Sun 10:00 AM | too few trades (119/200) |
| value_ev10 | 318 | 36.5 | 40.8 | $-444.49 | -14.0% | $555.51 | -2.1 | done | losing for real |
| trend_filter | 349 | 46.1 | 50.7 | $-450.99 | -12.9% | $549.01 | -2.5 | done | losing for real |
| value_ev5 | 470 | 39.1 | 42.4 | $-556.12 | -11.8% | $443.88 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 532 | 46.6 | 50.1 | $-614.91 | -11.6% | $385.09 | -2.7 | done | losing for real |
| coinflip | 1012 | 49.5 | 50.9 | $-727.94 | -7.2% | $272.06 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1012 | 49.8 | 51.6 | $-780.94 | -7.7% | $219.06 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 662 | 44.6 | 49.8 | $-961.00 | -14.5% | $39.00 | -3.8 | done | losing for real |
| always_up | 1012 | 47.1 | 50.4 | $-1089.46 | -10.8% | $-89.46 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1493 | 46.6 | 49.7 | $-1524.13 |
| ETH | 1664 | 46.7 | 49.1 | $-1722.05 |
| SOL | 1729 | 48.0 | 49.4 | $-1490.56 |
| XRP | 1794 | 48.7 | 49.2 | $-976.70 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
