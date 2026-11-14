# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 1:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 308 windows, 8226 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 669 | 53.1 | 51.7 | $-121.46 | -1.8% | $878.54 | -0.5 | done | can't tell from luck |
| value_ev20 | 152 | 34.9 | 36.5 | $-150.14 | -9.9% | $849.86 | -1.0 | Sun 2:30 AM | too few trades (152/200) |
| reversal_15m_0.10pct | 814 | 53.1 | 51.8 | $-163.02 | -2.0% | $836.98 | -0.6 | done | can't tell from luck |
| value_ev10 | 395 | 38.2 | 40.5 | $-386.52 | -9.8% | $613.48 | -1.7 | done | can't tell from luck |
| value_ev5 | 588 | 39.5 | 42.2 | $-632.64 | -10.8% | $367.36 | -2.3 | done | losing for real |
| trend_filter | 453 | 45.5 | 50.4 | $-642.16 | -14.2% | $357.84 | -3.1 | done | losing for real |
| momentum_60m_0.30pct | 669 | 46.9 | 50.0 | $-725.35 | -10.8% | $274.65 | -2.9 | done | losing for real |
| coinflip | 1224 | 50.0 | 50.9 | $-742.44 | -6.1% | $257.56 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 814 | 46.9 | 49.9 | $-832.60 | -10.2% | $167.40 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1224 | 48.9 | 51.3 | $-1099.90 | -9.0% | $-99.90 | -3.3 | done | losing for real |
| always_up | 1224 | 47.4 | 50.4 | $-1257.79 | -10.3% | $-257.79 | -3.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1850 | 46.5 | 49.3 | $-1837.84 |
| ETH | 2058 | 47.1 | 48.8 | $-1915.92 |
| SOL | 2137 | 48.1 | 49.4 | $-1722.58 |
| XRP | 2181 | 48.6 | 49.1 | $-1277.68 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
