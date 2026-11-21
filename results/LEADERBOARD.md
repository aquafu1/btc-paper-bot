# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 10:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 969 windows, 26862 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 496 | 34.7 | 34.8 | $-219.50 | -4.4% | $780.50 | -0.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 2742 | 51.3 | 50.5 | $-735.10 | -2.7% | $264.90 | -1.4 | done | can't tell from luck |
| value_ev10 | 1227 | 37.9 | 39.1 | $-749.05 | -6.1% | $250.95 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2292 | 50.2 | 49.8 | $-883.75 | -3.9% | $116.25 | -1.8 | done | can't tell from luck |
| trend_filter | 1608 | 50.0 | 50.9 | $-1067.85 | -6.6% | $-67.85 | -2.7 | done | losing for real |
| value_ev5 | 1859 | 39.8 | 40.9 | $-1132.06 | -6.1% | $-132.06 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 2292 | 49.8 | 50.9 | $-1647.28 | -7.2% | $-647.28 | -3.5 | done | losing for real |
| coinflip | 3868 | 50.2 | 50.3 | $-1779.03 | -4.6% | $-779.03 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2742 | 48.7 | 50.3 | $-1949.98 | -7.1% | $-949.98 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3868 | 50.9 | 51.6 | $-2010.82 | -5.2% | $-1010.82 | -3.3 | done | losing for real |
| always_up | 3868 | 46.8 | 49.6 | $-3837.42 | -9.9% | $-2837.42 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6118 | 48.2 | 49.1 | $-3459.21 |
| ETH | 6674 | 48.1 | 48.5 | $-4222.79 |
| SOL | 7016 | 48.2 | 48.6 | $-3922.51 |
| XRP | 7054 | 48.1 | 48.4 | $-4407.32 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
