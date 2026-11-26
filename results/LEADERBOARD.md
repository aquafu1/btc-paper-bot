# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 2:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1513 windows, 37600 settled trades, 387 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 764 | 34.6 | 35.4 | $-548.45 | -7.2% | $451.55 | -1.5 | done | can't tell from luck |
| value_ev10 | 1838 | 38.6 | 39.2 | $-927.33 | -5.0% | $72.67 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3741 | 50.9 | 50.1 | $-970.43 | -2.6% | $29.57 | -1.6 | done | can't tell from luck |
| value_ev5 | 2770 | 40.6 | 41.1 | $-1335.21 | -4.8% | $-335.21 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3136 | 51.1 | 51.0 | $-1424.29 | -4.5% | $-424.29 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3136 | 48.9 | 49.2 | $-1720.56 | -5.5% | $-720.56 | -3.1 | done | losing for real |
| trend_filter | 2226 | 48.6 | 50.3 | $-1912.55 | -8.6% | $-912.55 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3741 | 49.1 | 50.2 | $-2303.97 | -6.2% | $-1303.97 | -3.8 | done | losing for real |
| coinflip | 5416 | 50.0 | 50.0 | $-2384.05 | -4.4% | $-1384.05 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5416 | 50.2 | 51.3 | $-3327.38 | -6.1% | $-2327.38 | -4.7 | done | losing for real |
| always_up | 5416 | 48.1 | 49.2 | $-3544.91 | -6.5% | $-2544.91 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9768 | 48.0 | 48.7 | $-5352.52 |
| ETH | 10522 | 48.1 | 47.9 | $-5462.39 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
