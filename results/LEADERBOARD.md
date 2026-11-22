# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 2:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1082 windows, 29909 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 561 | 34.6 | 35.2 | $-318.28 | -5.7% | $681.72 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 3024 | 51.3 | 50.5 | $-780.27 | -2.6% | $219.73 | -1.4 | done | can't tell from luck |
| value_ev10 | 1383 | 37.8 | 39.2 | $-920.65 | -6.7% | $79.35 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2537 | 49.7 | 49.6 | $-1127.93 | -4.4% | $-127.93 | -2.2 | done | losing for real |
| trend_filter | 1778 | 49.6 | 50.6 | $-1244.89 | -7.0% | $-244.89 | -3.0 | done | losing for real |
| value_ev5 | 2102 | 39.8 | 41.1 | $-1304.13 | -6.2% | $-304.13 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2537 | 50.3 | 51.1 | $-1625.87 | -6.4% | $-625.87 | -3.3 | done | losing for real |
| coinflip | 4321 | 50.5 | 50.3 | $-1668.80 | -3.9% | $-668.80 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 4321 | 51.0 | 51.5 | $-2030.72 | -4.7% | $-1030.72 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3024 | 48.7 | 50.3 | $-2126.19 | -7.0% | $-1126.19 | -3.9 | done | losing for real |
| always_up | 4321 | 47.4 | 49.4 | $-3642.44 | -8.4% | $-2642.44 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6834 | 48.5 | 49.0 | $-3334.27 |
| ETH | 7403 | 48.2 | 48.5 | $-4452.80 |
| SOL | 7800 | 48.1 | 48.5 | $-4380.48 |
| XRP | 7872 | 48.2 | 48.3 | $-4622.62 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
