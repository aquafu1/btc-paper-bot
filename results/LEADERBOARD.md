# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 12:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 641 windows, 17718 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1496 | 51.1 | 49.6 | $-203.57 | -1.4% | $796.43 | -0.5 | done | can't tell from luck |
| value_ev20 | 334 | 34.1 | 35.3 | $-256.80 | -7.7% | $743.20 | -1.1 | done | can't tell from luck |
| trend_filter | 1023 | 50.5 | 50.8 | $-498.76 | -4.9% | $501.24 | -1.6 | done | can't tell from luck |
| value_ev10 | 817 | 38.4 | 39.5 | $-557.13 | -6.8% | $442.87 | -1.6 | done | can't tell from luck |
| value_ev5 | 1238 | 40.9 | 41.4 | $-652.25 | -5.3% | $347.75 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1823 | 51.1 | 51.0 | $-697.36 | -3.8% | $302.64 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1823 | 48.9 | 50.0 | $-1110.30 | -6.1% | $-110.30 | -2.6 | done | losing for real |
| coinflip | 2556 | 50.2 | 50.5 | $-1139.08 | -4.5% | $-139.08 | -2.3 | done | losing for real |
| momentum_5m_0.00pct | 2556 | 50.7 | 51.7 | $-1369.60 | -5.4% | $-369.60 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1496 | 48.9 | 51.4 | $-1372.04 | -9.2% | $-372.04 | -3.6 | done | losing for real |
| always_up | 2556 | 47.3 | 49.7 | $-2260.04 | -8.8% | $-1260.04 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4026 | 48.4 | 49.3 | $-2375.16 |
| ETH | 4429 | 48.3 | 48.7 | $-2605.66 |
| SOL | 4599 | 48.0 | 48.8 | $-2894.54 |
| XRP | 4664 | 48.5 | 48.5 | $-2241.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
