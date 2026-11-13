# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 1:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 261 windows, 6857 settled trades, 31 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 680 | 55.6 | 52.2 | $+161.28 | +2.4% | $1161.28 | +0.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 549 | 53.6 | 52.2 | $-83.41 | -1.5% | $916.59 | -0.4 | done | can't tell from luck |
| value_ev20 | 120 | 33.3 | 36.7 | $-151.51 | -12.6% | $848.49 | -1.1 | Sun 12:00 PM | too few trades (120/200) |
| value_ev10 | 326 | 36.2 | 40.7 | $-469.85 | -14.4% | $530.15 | -2.2 | done | losing for real |
| trend_filter | 358 | 45.5 | 50.4 | $-505.04 | -14.1% | $494.96 | -2.7 | done | losing for real |
| value_ev5 | 481 | 39.1 | 42.4 | $-570.76 | -11.9% | $429.24 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 549 | 46.4 | 49.8 | $-639.82 | -11.7% | $360.18 | -2.8 | done | losing for real |
| coinflip | 1038 | 49.2 | 50.8 | $-799.31 | -7.7% | $200.69 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 1038 | 49.5 | 51.6 | $-866.41 | -8.3% | $133.59 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 680 | 44.4 | 49.8 | $-1014.40 | -14.9% | $-14.40 | -4.0 | done | losing for real |
| always_up | 1038 | 47.5 | 50.2 | $-1028.82 | -9.9% | $-28.82 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1530 | 46.4 | 49.6 | $-1655.63 |
| ETH | 1701 | 46.6 | 49.1 | $-1783.14 |
| SOL | 1782 | 48.0 | 49.3 | $-1499.04 |
| XRP | 1844 | 48.7 | 49.2 | $-1030.23 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
