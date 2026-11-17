# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 1:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 647 windows, 17880 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 337 | 34.7 | 35.3 | $-207.49 | -6.2% | $792.51 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1507 | 50.7 | 49.6 | $-313.57 | -2.1% | $686.43 | -0.8 | done | can't tell from luck |
| value_ev10 | 825 | 38.5 | 39.5 | $-534.77 | -6.5% | $465.23 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1841 | 51.5 | 51.0 | $-580.08 | -3.2% | $419.92 | -1.4 | done | can't tell from luck |
| value_ev5 | 1249 | 41.1 | 41.4 | $-593.62 | -4.8% | $406.38 | -1.4 | done | can't tell from luck |
| trend_filter | 1033 | 50.0 | 50.8 | $-598.76 | -5.8% | $401.24 | -1.9 | done | can't tell from luck |
| coinflip | 2580 | 50.2 | 50.5 | $-1122.94 | -4.4% | $-122.94 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 1841 | 48.5 | 50.0 | $-1236.14 | -6.7% | $-236.14 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 1507 | 49.3 | 51.4 | $-1275.36 | -8.5% | $-275.36 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2580 | 50.5 | 51.7 | $-1506.63 | -5.8% | $-506.63 | -3.1 | done | losing for real |
| always_up | 2580 | 47.3 | 49.7 | $-2250.33 | -8.7% | $-1250.33 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4054 | 48.3 | 49.3 | $-2435.94 |
| ETH | 4468 | 48.2 | 48.7 | $-2666.31 |
| SOL | 4648 | 48.0 | 48.8 | $-2839.40 |
| XRP | 4710 | 48.5 | 48.5 | $-2278.02 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
