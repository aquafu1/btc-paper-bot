# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 8:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1297 windows, 34609 settled trades, 429 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 682 | 34.2 | 35.3 | $-534.70 | -7.8% | $465.30 | -1.6 | done | can't tell from luck |
| value_ev10 | 1667 | 38.8 | 39.2 | $-765.98 | -4.6% | $234.02 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3472 | 50.8 | 50.2 | $-1044.14 | -3.0% | $-44.14 | -1.8 | done | can't tell from luck |
| value_ev5 | 2515 | 40.5 | 41.1 | $-1243.67 | -4.9% | $-243.67 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2901 | 49.5 | 49.4 | $-1340.39 | -4.6% | $-340.39 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2901 | 50.5 | 51.0 | $-1612.36 | -5.6% | $-612.36 | -3.1 | done | losing for real |
| trend_filter | 2047 | 48.9 | 50.5 | $-1671.96 | -8.2% | $-671.96 | -3.8 | done | losing for real |
| momentum_15m_0.10pct | 3472 | 49.2 | 50.3 | $-2170.99 | -6.3% | $-1170.99 | -3.7 | done | losing for real |
| coinflip | 4984 | 50.0 | 50.1 | $-2205.13 | -4.4% | $-1205.13 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4984 | 50.4 | 51.4 | $-2844.06 | -5.7% | $-1844.06 | -4.1 | done | losing for real |
| always_up | 4984 | 47.9 | 49.3 | $-3580.61 | -7.2% | $-2580.61 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8322 | 48.0 | 48.8 | $-4767.71 |
| ETH | 8977 | 48.3 | 48.2 | $-4662.04 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
