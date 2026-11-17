# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 10:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 584 windows, 16159 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1372 | 51.2 | 49.6 | $-217.08 | -1.6% | $782.92 | -0.6 | done | can't tell from luck |
| value_ev20 | 316 | 32.9 | 35.2 | $-374.56 | -11.9% | $625.44 | -1.6 | done | can't tell from luck |
| trend_filter | 937 | 50.6 | 50.9 | $-472.40 | -5.0% | $527.60 | -1.6 | done | can't tell from luck |
| value_ev10 | 758 | 37.3 | 39.4 | $-747.02 | -9.9% | $252.98 | -2.3 | done | losing for real |
| reversal_15m_0.10pct | 1643 | 50.8 | 51.0 | $-829.56 | -5.0% | $170.44 | -2.1 | done | losing for real |
| value_ev5 | 1134 | 40.0 | 41.3 | $-845.61 | -7.5% | $154.39 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 1643 | 49.2 | 49.9 | $-942.32 | -5.7% | $57.68 | -2.3 | done | losing for real |
| coinflip | 2328 | 49.9 | 50.5 | $-1233.97 | -5.3% | $-233.97 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1372 | 48.8 | 51.3 | $-1347.70 | -9.8% | $-347.70 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2328 | 50.3 | 51.8 | $-1588.19 | -6.8% | $-588.19 | -3.4 | done | losing for real |
| always_up | 2328 | 47.3 | 49.9 | $-2217.09 | -9.5% | $-1217.09 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3668 | 47.8 | 49.2 | $-2652.78 |
| ETH | 4032 | 48.0 | 48.6 | $-2715.86 |
| SOL | 4200 | 47.8 | 48.8 | $-3129.34 |
| XRP | 4259 | 48.5 | 48.6 | $-2317.51 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
