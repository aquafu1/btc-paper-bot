# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 9:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 532 windows, 14692 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1252 | 51.9 | 49.9 | $-22.51 | -0.2% | $977.49 | -0.1 | done | can't tell from luck |
| value_ev20 | 279 | 34.8 | 35.6 | $-202.64 | -7.3% | $797.36 | -0.9 | done | can't tell from luck |
| trend_filter | 863 | 50.2 | 50.8 | $-472.77 | -5.5% | $527.23 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1488 | 50.0 | 49.7 | $-527.72 | -3.5% | $472.28 | -1.4 | done | can't tell from luck |
| value_ev10 | 686 | 38.2 | 39.8 | $-540.63 | -7.9% | $459.37 | -1.7 | done | can't tell from luck |
| value_ev5 | 1024 | 40.3 | 41.5 | $-696.07 | -6.8% | $303.93 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1488 | 50.0 | 51.4 | $-1065.26 | -7.2% | $-65.26 | -2.8 | done | losing for real |
| coinflip | 2120 | 49.9 | 50.6 | $-1185.08 | -5.6% | $-185.08 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1252 | 48.1 | 51.2 | $-1323.22 | -10.6% | $-323.22 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2120 | 49.6 | 51.6 | $-1641.17 | -7.7% | $-641.17 | -3.7 | done | losing for real |
| always_up | 2120 | 46.7 | 50.2 | $-2329.88 | -11.0% | $-1329.88 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3331 | 47.5 | 49.3 | $-2636.32 |
| ETH | 3663 | 48.1 | 48.7 | $-2368.73 |
| SOL | 3831 | 47.7 | 49.0 | $-2798.87 |
| XRP | 3867 | 48.5 | 48.8 | $-2203.04 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
