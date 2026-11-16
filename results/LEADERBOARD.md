# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 10:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 488 windows, 13418 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 249 | 34.5 | 35.8 | $-169.21 | -6.8% | $830.79 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1141 | 51.1 | 49.8 | $-189.48 | -1.7% | $810.52 | -0.6 | done | can't tell from luck |
| value_ev10 | 633 | 38.7 | 40.0 | $-410.56 | -6.5% | $589.44 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1350 | 50.1 | 49.9 | $-431.95 | -3.2% | $568.05 | -1.2 | done | can't tell from luck |
| trend_filter | 789 | 49.4 | 50.7 | $-540.26 | -6.8% | $459.74 | -2.0 | done | can't tell from luck |
| value_ev5 | 933 | 40.7 | 41.8 | $-546.74 | -5.9% | $453.26 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1350 | 49.9 | 51.5 | $-973.72 | -7.2% | $26.28 | -2.7 | done | losing for real |
| coinflip | 1944 | 49.9 | 50.8 | $-1030.74 | -5.3% | $-30.74 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1141 | 48.9 | 51.5 | $-1050.89 | -9.2% | $-50.89 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1944 | 49.5 | 51.7 | $-1486.11 | -7.6% | $-486.11 | -3.5 | done | losing for real |
| always_up | 1944 | 46.4 | 50.4 | $-2268.52 | -11.7% | $-1268.52 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3025 | 47.3 | 49.3 | $-2477.32 |
| ETH | 3363 | 48.1 | 48.8 | $-2165.73 |
| SOL | 3498 | 47.8 | 49.2 | $-2520.85 |
| XRP | 3532 | 48.4 | 48.9 | $-1934.28 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
