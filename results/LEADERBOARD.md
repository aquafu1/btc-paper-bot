# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 10:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 491 windows, 13495 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 249 | 34.5 | 35.8 | $-169.21 | -6.8% | $830.79 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1147 | 50.9 | 49.8 | $-227.40 | -2.0% | $772.60 | -0.7 | done | can't tell from luck |
| value_ev10 | 634 | 38.6 | 40.0 | $-420.56 | -6.6% | $579.44 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1360 | 49.9 | 49.9 | $-508.56 | -3.7% | $491.44 | -1.4 | done | can't tell from luck |
| value_ev5 | 938 | 40.8 | 41.8 | $-526.78 | -5.6% | $473.22 | -1.5 | done | can't tell from luck |
| trend_filter | 789 | 49.4 | 50.7 | $-540.26 | -6.8% | $459.74 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1360 | 50.1 | 51.5 | $-902.92 | -6.6% | $97.08 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1147 | 49.1 | 51.5 | $-1009.80 | -8.8% | $-9.80 | -3.1 | done | losing for real |
| coinflip | 1957 | 49.9 | 50.7 | $-1023.31 | -5.2% | $-23.31 | -2.3 | done | losing for real |
| momentum_5m_0.00pct | 1957 | 49.7 | 51.7 | $-1436.62 | -7.3% | $-436.62 | -3.4 | done | losing for real |
| always_up | 1957 | 46.5 | 50.4 | $-2233.00 | -11.4% | $-1233.00 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3041 | 47.4 | 49.3 | $-2430.70 |
| ETH | 3386 | 48.1 | 48.8 | $-2177.60 |
| SOL | 3519 | 47.8 | 49.3 | $-2502.40 |
| XRP | 3549 | 48.5 | 48.9 | $-1887.70 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
