# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 1:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 262 windows, 6870 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 682 | 55.4 | 52.3 | $+141.28 | +2.1% | $1141.28 | +0.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 550 | 53.5 | 52.2 | $-93.41 | -1.7% | $906.59 | -0.4 | done | can't tell from luck |
| value_ev20 | 120 | 33.3 | 36.7 | $-151.51 | -12.6% | $848.49 | -1.1 | Sun 12:00 PM | too few trades (120/200) |
| value_ev10 | 326 | 36.2 | 40.7 | $-469.85 | -14.4% | $530.15 | -2.2 | done | losing for real |
| trend_filter | 359 | 45.7 | 50.3 | $-485.27 | -13.5% | $514.73 | -2.6 | done | losing for real |
| value_ev5 | 481 | 39.1 | 42.4 | $-570.76 | -11.9% | $429.24 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 550 | 46.5 | 49.7 | $-620.06 | -11.3% | $379.94 | -2.7 | done | losing for real |
| coinflip | 1040 | 49.2 | 50.8 | $-793.48 | -7.6% | $206.52 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 1040 | 49.6 | 51.5 | $-830.81 | -8.0% | $169.19 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 682 | 44.6 | 49.8 | $-978.80 | -14.4% | $21.20 | -3.8 | done | losing for real |
| always_up | 1040 | 47.6 | 50.1 | $-993.22 | -9.6% | $6.78 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1535 | 46.5 | 49.6 | $-1602.29 |
| ETH | 1709 | 46.7 | 49.1 | $-1714.32 |
| SOL | 1782 | 48.0 | 49.3 | $-1499.04 |
| XRP | 1844 | 48.7 | 49.2 | $-1030.23 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
