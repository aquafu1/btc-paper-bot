# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 8:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 289 windows, 7637 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 752 | 54.4 | 51.8 | $+37.38 | +0.5% | $1037.38 | +0.1 | done | can't tell from luck |
| value_ev20 | 142 | 35.9 | 36.4 | $-101.22 | -7.1% | $898.78 | -0.7 | Sun 3:30 AM | too few trades (142/200) |
| reversal_60m_0.30pct | 613 | 52.4 | 51.7 | $-200.58 | -3.3% | $799.42 | -0.8 | done | can't tell from luck |
| value_ev10 | 370 | 38.4 | 40.5 | $-346.90 | -9.4% | $653.10 | -1.5 | done | can't tell from luck |
| trend_filter | 406 | 46.6 | 50.4 | $-496.66 | -12.2% | $503.34 | -2.5 | done | losing for real |
| value_ev5 | 545 | 40.0 | 42.1 | $-515.43 | -9.5% | $484.57 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 613 | 47.6 | 49.9 | $-571.99 | -9.3% | $428.01 | -2.4 | done | losing for real |
| coinflip | 1148 | 50.1 | 50.9 | $-672.91 | -5.9% | $327.09 | -2.0 | done | losing for real |
| momentum_5m_0.00pct | 1148 | 49.3 | 51.4 | $-951.97 | -8.3% | $48.03 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 752 | 45.6 | 49.9 | $-956.62 | -12.7% | $43.38 | -3.6 | done | losing for real |
| always_up | 1148 | 47.6 | 50.2 | $-1086.10 | -9.5% | $-86.10 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1701 | 46.9 | 49.4 | $-1526.83 |
| ETH | 1906 | 47.2 | 48.7 | $-1695.85 |
| SOL | 1986 | 48.2 | 49.3 | $-1582.39 |
| XRP | 2044 | 48.8 | 49.1 | $-1057.92 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
