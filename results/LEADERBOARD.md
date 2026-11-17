# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 9:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 583 windows, 16131 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1369 | 51.1 | 49.6 | $-249.10 | -1.8% | $750.90 | -0.7 | done | can't tell from luck |
| value_ev20 | 316 | 32.9 | 35.2 | $-374.56 | -11.9% | $625.44 | -1.6 | done | can't tell from luck |
| trend_filter | 934 | 50.4 | 50.9 | $-504.41 | -5.4% | $495.59 | -1.7 | done | can't tell from luck |
| value_ev10 | 757 | 37.3 | 39.4 | $-757.94 | -10.0% | $242.06 | -2.3 | done | losing for real |
| reversal_15m_0.10pct | 1640 | 50.9 | 51.0 | $-799.56 | -4.9% | $200.44 | -2.0 | done | losing for real |
| value_ev5 | 1131 | 39.9 | 41.3 | $-877.62 | -7.8% | $122.38 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 1640 | 49.1 | 49.9 | $-974.33 | -5.9% | $25.67 | -2.4 | done | losing for real |
| coinflip | 2325 | 49.9 | 50.5 | $-1245.91 | -5.4% | $-245.91 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1369 | 48.9 | 51.3 | $-1317.70 | -9.6% | $-317.70 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2325 | 50.2 | 51.8 | $-1620.20 | -7.0% | $-620.20 | -3.5 | done | losing for real |
| always_up | 2325 | 47.2 | 49.9 | $-2249.10 | -9.7% | $-1249.10 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3668 | 47.8 | 49.2 | $-2652.78 |
| ETH | 4022 | 47.9 | 48.6 | $-2783.20 |
| SOL | 4191 | 47.7 | 48.8 | $-3186.47 |
| XRP | 4250 | 48.5 | 48.6 | $-2347.96 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
