# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 10:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 680 windows, 18840 settled trades, 30 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 355 | 34.4 | 35.0 | $-224.96 | -6.3% | $775.04 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1598 | 50.4 | 49.5 | $-428.83 | -2.7% | $571.17 | -1.1 | done | can't tell from luck |
| value_ev10 | 870 | 38.4 | 39.2 | $-525.56 | -6.0% | $474.44 | -1.5 | done | can't tell from luck |
| trend_filter | 1098 | 50.4 | 50.9 | $-571.27 | -5.2% | $428.73 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1934 | 51.5 | 51.0 | $-613.24 | -3.2% | $386.76 | -1.4 | done | can't tell from luck |
| value_ev5 | 1308 | 40.6 | 41.2 | $-682.88 | -5.2% | $317.12 | -1.6 | done | can't tell from luck |
| coinflip | 2715 | 50.1 | 50.4 | $-1238.16 | -4.6% | $-238.16 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1598 | 49.6 | 51.3 | $-1241.26 | -7.8% | $-241.26 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1934 | 48.5 | 49.9 | $-1283.89 | -6.6% | $-283.89 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 2715 | 50.8 | 51.8 | $-1464.48 | -5.4% | $-464.48 | -2.9 | done | losing for real |
| always_up | 2715 | 47.3 | 49.7 | $-2395.50 | -8.8% | $-1395.50 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4282 | 48.3 | 49.2 | $-2520.06 |
| ETH | 4693 | 48.2 | 48.6 | $-2813.94 |
| SOL | 4912 | 48.1 | 48.7 | $-2905.43 |
| XRP | 4953 | 48.5 | 48.4 | $-2430.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
