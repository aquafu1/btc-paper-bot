# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 10:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 344 windows, 9234 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 184 | 37.5 | 36.6 | $-38.35 | -2.1% | $961.65 | -0.2 | Sat 6:00 PM | too few trades (184/200) |
| value_ev10 | 451 | 39.7 | 40.2 | $-226.45 | -5.0% | $773.55 | -0.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 746 | 51.9 | 52.1 | $-305.87 | -4.1% | $694.13 | -1.2 | done | can't tell from luck |
| value_ev5 | 668 | 41.3 | 41.9 | $-358.80 | -5.4% | $641.20 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 914 | 52.0 | 52.0 | $-381.70 | -4.2% | $618.30 | -1.3 | done | can't tell from luck |
| momentum_60m_0.30pct | 746 | 48.1 | 49.6 | $-539.44 | -7.2% | $460.56 | -2.0 | done | can't tell from luck |
| trend_filter | 504 | 46.8 | 50.2 | $-540.93 | -10.7% | $459.07 | -2.4 | done | losing for real |
| coinflip | 1369 | 50.3 | 50.8 | $-652.15 | -4.8% | $347.85 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 914 | 48.0 | 49.7 | $-678.06 | -7.4% | $321.94 | -2.3 | done | losing for real |
| momentum_5m_0.00pct | 1369 | 49.0 | 51.3 | $-1113.28 | -8.1% | $-113.28 | -3.1 | done | losing for real |
| always_up | 1369 | 46.8 | 50.6 | $-1521.01 | -11.1% | $-521.01 | -4.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2077 | 47.0 | 49.2 | $-1730.33 |
| ETH | 2321 | 47.5 | 48.7 | $-1691.87 |
| SOL | 2395 | 48.1 | 49.3 | $-1747.20 |
| XRP | 2441 | 48.8 | 49.1 | $-1186.64 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
