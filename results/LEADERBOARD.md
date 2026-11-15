# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 9:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 438 windows, 12065 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 220 | 34.5 | 36.1 | $-178.23 | -8.1% | $821.77 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1030 | 51.2 | 49.9 | $-188.53 | -1.8% | $811.47 | -0.6 | done | can't tell from luck |
| trend_filter | 697 | 50.2 | 50.6 | $-341.34 | -4.9% | $658.66 | -1.3 | done | can't tell from luck |
| value_ev10 | 569 | 38.7 | 40.2 | $-423.63 | -7.4% | $576.37 | -1.5 | done | can't tell from luck |
| value_ev5 | 847 | 41.0 | 41.9 | $-519.11 | -6.1% | $480.89 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1220 | 49.5 | 50.0 | $-559.56 | -4.6% | $440.44 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1220 | 50.5 | 51.7 | $-817.47 | -6.7% | $182.53 | -2.5 | done | losing for real |
| coinflip | 1744 | 50.4 | 50.9 | $-819.64 | -4.7% | $180.36 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 1030 | 48.8 | 51.8 | $-1036.12 | -10.1% | $-36.12 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 1744 | 49.8 | 51.6 | $-1228.12 | -7.0% | $-228.12 | -3.0 | done | losing for real |
| always_up | 1744 | 45.9 | 50.5 | $-2246.46 | -12.9% | $-1246.46 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2725 | 47.5 | 49.3 | $-2145.35 |
| ETH | 3031 | 48.0 | 48.8 | $-1924.88 |
| SOL | 3131 | 47.8 | 49.3 | $-2480.52 |
| XRP | 3178 | 48.6 | 49.2 | $-1807.45 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
