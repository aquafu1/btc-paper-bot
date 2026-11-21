# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 11:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 972 windows, 26956 settled trades, 68 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 496 | 34.7 | 34.8 | $-219.50 | -4.4% | $780.50 | -0.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 2753 | 51.3 | 50.5 | $-703.50 | -2.6% | $296.50 | -1.3 | done | can't tell from luck |
| value_ev10 | 1229 | 37.9 | 39.1 | $-744.80 | -6.1% | $255.20 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2304 | 50.3 | 49.8 | $-840.93 | -3.6% | $159.07 | -1.8 | done | can't tell from luck |
| value_ev5 | 1865 | 39.8 | 41.0 | $-1098.05 | -5.9% | $-98.05 | -2.1 | done | losing for real |
| trend_filter | 1612 | 49.9 | 50.9 | $-1107.85 | -6.9% | $-107.85 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2304 | 49.7 | 50.9 | $-1695.44 | -7.4% | $-695.44 | -3.6 | done | losing for real |
| coinflip | 3880 | 50.2 | 50.3 | $-1804.70 | -4.7% | $-804.70 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2753 | 48.7 | 50.3 | $-1991.16 | -7.2% | $-991.16 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3880 | 50.7 | 51.6 | $-2130.82 | -5.5% | $-1130.82 | -3.5 | done | losing for real |
| always_up | 3880 | 46.8 | 49.6 | $-3885.58 | -10.0% | $-2885.58 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6140 | 48.2 | 49.1 | $-3515.81 |
| ETH | 6699 | 48.0 | 48.5 | $-4305.08 |
| SOL | 7039 | 48.2 | 48.6 | $-3976.65 |
| XRP | 7078 | 48.1 | 48.4 | $-4424.79 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
