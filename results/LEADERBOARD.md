# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 10:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 971 windows, 26940 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 496 | 34.7 | 34.8 | $-219.50 | -4.4% | $780.50 | -0.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 2751 | 51.3 | 50.5 | $-719.10 | -2.6% | $280.90 | -1.4 | done | can't tell from luck |
| value_ev10 | 1229 | 37.9 | 39.1 | $-744.80 | -6.1% | $255.20 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2302 | 50.3 | 49.8 | $-820.93 | -3.6% | $179.07 | -1.7 | done | can't tell from luck |
| trend_filter | 1610 | 49.9 | 50.9 | $-1087.85 | -6.8% | $-87.85 | -2.8 | done | losing for real |
| value_ev5 | 1865 | 39.8 | 41.0 | $-1098.05 | -5.9% | $-98.05 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2302 | 49.7 | 50.9 | $-1711.04 | -7.4% | $-711.04 | -3.6 | done | losing for real |
| coinflip | 3878 | 50.2 | 50.3 | $-1803.13 | -4.6% | $-803.13 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2751 | 48.7 | 50.3 | $-1971.16 | -7.2% | $-971.16 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3878 | 50.7 | 51.6 | $-2110.82 | -5.4% | $-1110.82 | -3.5 | done | losing for real |
| always_up | 3878 | 46.8 | 49.6 | $-3901.18 | -10.1% | $-2901.18 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6140 | 48.2 | 49.1 | $-3515.81 |
| ETH | 6699 | 48.0 | 48.5 | $-4305.08 |
| SOL | 7031 | 48.2 | 48.6 | $-3948.16 |
| XRP | 7070 | 48.1 | 48.4 | $-4418.52 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
