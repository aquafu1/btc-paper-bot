# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 10:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 632 windows, 17454 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1473 | 51.1 | 49.5 | $-181.89 | -1.2% | $818.11 | -0.5 | done | can't tell from luck |
| value_ev20 | 330 | 33.9 | 35.3 | $-274.70 | -8.3% | $725.30 | -1.2 | done | can't tell from luck |
| trend_filter | 1008 | 50.2 | 50.8 | $-556.30 | -5.5% | $443.70 | -1.8 | done | can't tell from luck |
| value_ev10 | 804 | 38.3 | 39.5 | $-575.74 | -7.2% | $424.26 | -1.7 | done | can't tell from luck |
| value_ev5 | 1218 | 40.6 | 41.4 | $-714.18 | -5.9% | $285.82 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1794 | 51.0 | 51.1 | $-787.78 | -4.4% | $212.22 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1794 | 49.0 | 49.9 | $-1039.14 | -5.8% | $-39.14 | -2.5 | done | losing for real |
| coinflip | 2520 | 50.1 | 50.5 | $-1174.95 | -4.7% | $-174.95 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1473 | 48.9 | 51.5 | $-1401.97 | -9.5% | $-401.97 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2520 | 50.4 | 51.7 | $-1514.66 | -6.0% | $-514.66 | -3.1 | done | losing for real |
| always_up | 2520 | 47.3 | 49.7 | $-2227.24 | -8.8% | $-1227.24 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3961 | 48.2 | 49.2 | $-2469.25 |
| ETH | 4368 | 48.2 | 48.6 | $-2627.17 |
| SOL | 4531 | 47.9 | 48.8 | $-3012.35 |
| XRP | 4594 | 48.5 | 48.5 | $-2339.79 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
