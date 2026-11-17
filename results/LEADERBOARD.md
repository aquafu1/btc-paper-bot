# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 10:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 634 windows, 17519 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1481 | 50.9 | 49.5 | $-242.96 | -1.6% | $757.04 | -0.6 | done | can't tell from luck |
| value_ev20 | 330 | 33.9 | 35.3 | $-274.70 | -8.3% | $725.30 | -1.2 | done | can't tell from luck |
| value_ev10 | 805 | 38.4 | 39.5 | $-565.25 | -7.0% | $434.75 | -1.6 | done | can't tell from luck |
| trend_filter | 1012 | 50.1 | 50.8 | $-577.37 | -5.7% | $422.63 | -1.9 | done | can't tell from luck |
| value_ev5 | 1222 | 40.7 | 41.4 | $-714.39 | -5.8% | $285.61 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1802 | 51.0 | 51.1 | $-790.54 | -4.4% | $209.46 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1802 | 49.0 | 49.9 | $-1043.34 | -5.8% | $-43.34 | -2.5 | done | losing for real |
| coinflip | 2528 | 50.1 | 50.5 | $-1179.68 | -4.7% | $-179.68 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1481 | 49.1 | 51.5 | $-1347.85 | -9.1% | $-347.85 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2528 | 50.5 | 51.7 | $-1497.94 | -5.9% | $-497.94 | -3.1 | done | losing for real |
| always_up | 2528 | 47.4 | 49.7 | $-2173.12 | -8.6% | $-1173.12 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3977 | 48.3 | 49.2 | $-2450.91 |
| ETH | 4386 | 48.2 | 48.6 | $-2609.99 |
| SOL | 4547 | 48.0 | 48.8 | $-2997.13 |
| XRP | 4609 | 48.5 | 48.6 | $-2349.12 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
