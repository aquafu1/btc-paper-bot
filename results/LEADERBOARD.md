# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 7:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 284 windows, 7506 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 739 | 54.3 | 51.8 | $+27.54 | +0.4% | $1027.54 | +0.1 | done | can't tell from luck |
| value_ev20 | 139 | 35.3 | 36.4 | $-119.35 | -8.6% | $880.65 | -0.8 | Sun 4:00 AM | too few trades (139/200) |
| reversal_60m_0.30pct | 605 | 52.4 | 51.8 | $-192.68 | -3.2% | $807.32 | -0.8 | done | can't tell from luck |
| value_ev10 | 364 | 38.2 | 40.5 | $-360.86 | -9.9% | $639.14 | -1.6 | done | can't tell from luck |
| trend_filter | 397 | 46.6 | 50.5 | $-489.72 | -12.3% | $510.28 | -2.5 | done | losing for real |
| value_ev5 | 534 | 40.1 | 42.2 | $-500.97 | -9.4% | $499.03 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 605 | 47.6 | 49.8 | $-564.68 | -9.3% | $435.32 | -2.3 | done | losing for real |
| coinflip | 1128 | 49.9 | 50.9 | $-693.46 | -6.1% | $306.54 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1128 | 49.6 | 51.5 | $-887.73 | -7.9% | $112.27 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 739 | 45.7 | 49.9 | $-914.97 | -12.4% | $85.03 | -3.4 | done | losing for real |
| always_up | 1128 | 47.6 | 50.3 | $-1076.00 | -9.5% | $-76.00 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1673 | 46.7 | 49.5 | $-1636.67 |
| ETH | 1875 | 47.1 | 48.8 | $-1720.48 |
| SOL | 1949 | 48.3 | 49.3 | $-1491.37 |
| XRP | 2009 | 49.0 | 49.1 | $-924.36 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
