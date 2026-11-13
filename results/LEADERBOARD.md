# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 2:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 265 windows, 6964 settled trades, 13 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 687 | 55.3 | 52.3 | $+125.71 | +1.8% | $1125.71 | +0.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 557 | 53.1 | 52.2 | $-134.45 | -2.4% | $865.55 | -0.6 | done | can't tell from luck |
| value_ev20 | 122 | 32.8 | 36.7 | $-171.51 | -14.1% | $828.49 | -1.2 | Sun 11:45 AM | too few trades (122/200) |
| value_ev10 | 333 | 36.6 | 40.7 | $-443.49 | -13.3% | $556.51 | -2.1 | done | losing for real |
| trend_filter | 363 | 45.7 | 50.2 | $-490.09 | -13.5% | $509.91 | -2.6 | done | losing for real |
| value_ev5 | 490 | 39.2 | 42.4 | $-564.40 | -11.5% | $435.60 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 557 | 46.9 | 49.7 | $-593.55 | -10.7% | $406.45 | -2.6 | done | losing for real |
| coinflip | 1056 | 49.4 | 50.8 | $-760.26 | -7.2% | $239.74 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1056 | 49.4 | 51.5 | $-872.12 | -8.3% | $127.88 | -2.8 | done | losing for real |
| always_up | 1056 | 48.0 | 50.1 | $-908.58 | -8.6% | $91.42 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 687 | 44.7 | 49.7 | $-971.06 | -14.1% | $28.94 | -3.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1551 | 46.5 | 49.5 | $-1626.86 |
| ETH | 1740 | 46.7 | 49.0 | $-1745.87 |
| SOL | 1802 | 48.2 | 49.2 | $-1365.31 |
| XRP | 1871 | 48.7 | 49.1 | $-1045.76 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
