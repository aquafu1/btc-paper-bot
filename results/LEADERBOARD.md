# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 12:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 688 windows, 19043 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 362 | 34.3 | 34.9 | $-233.12 | -6.4% | $766.88 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1607 | 50.4 | 49.5 | $-439.87 | -2.7% | $560.13 | -1.1 | done | can't tell from luck |
| value_ev10 | 880 | 38.4 | 39.2 | $-509.28 | -5.8% | $490.72 | -1.4 | done | can't tell from luck |
| trend_filter | 1111 | 50.4 | 50.9 | $-593.14 | -5.3% | $406.86 | -1.8 | done | can't tell from luck |
| value_ev5 | 1323 | 40.8 | 41.1 | $-609.40 | -4.6% | $390.60 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1959 | 51.4 | 50.8 | $-613.33 | -3.1% | $386.67 | -1.4 | done | can't tell from luck |
| coinflip | 2745 | 50.2 | 50.3 | $-1180.18 | -4.3% | $-180.18 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1607 | 49.6 | 51.3 | $-1254.51 | -7.8% | $-254.51 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1959 | 48.6 | 49.9 | $-1286.90 | -6.6% | $-286.90 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 2745 | 50.8 | 51.8 | $-1524.53 | -5.6% | $-524.53 | -3.0 | done | losing for real |
| always_up | 2745 | 47.5 | 49.6 | $-2279.90 | -8.3% | $-1279.90 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4325 | 48.3 | 49.1 | $-2482.60 |
| ETH | 4740 | 48.3 | 48.6 | $-2804.90 |
| SOL | 4962 | 48.2 | 48.6 | $-2842.56 |
| XRP | 5016 | 48.5 | 48.4 | $-2394.10 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
