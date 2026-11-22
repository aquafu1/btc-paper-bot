# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 3:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1133 windows, 31295 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 601 | 34.6 | 35.2 | $-363.62 | -6.1% | $636.38 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3150 | 51.1 | 50.5 | $-865.65 | -2.7% | $134.35 | -1.5 | done | can't tell from luck |
| value_ev10 | 1467 | 38.1 | 39.2 | $-913.03 | -6.2% | $86.97 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2642 | 49.6 | 49.4 | $-1156.63 | -4.4% | $-156.63 | -2.2 | done | losing for real |
| value_ev5 | 2218 | 40.0 | 41.1 | $-1314.80 | -5.9% | $-314.80 | -2.4 | done | losing for real |
| trend_filter | 1853 | 49.1 | 50.4 | $-1446.67 | -7.8% | $-446.67 | -3.4 | done | losing for real |
| reversal_60m_0.30pct | 2642 | 50.4 | 51.1 | $-1637.08 | -6.2% | $-637.08 | -3.3 | done | losing for real |
| coinflip | 4524 | 50.4 | 50.2 | $-1800.44 | -4.0% | $-800.44 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 3150 | 48.9 | 50.2 | $-2063.54 | -6.6% | $-1063.54 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4524 | 50.3 | 51.4 | $-2766.70 | -6.1% | $-1766.70 | -4.2 | done | losing for real |
| always_up | 4524 | 47.7 | 49.3 | $-3440.89 | -7.6% | $-2440.89 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7171 | 48.3 | 49.0 | $-3648.28 |
| ETH | 7752 | 48.1 | 48.4 | $-4648.13 |
| SOL | 8145 | 48.0 | 48.4 | $-4654.91 |
| XRP | 8227 | 48.1 | 48.2 | $-4817.73 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
