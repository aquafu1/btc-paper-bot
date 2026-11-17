# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 1:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 646 windows, 17856 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 336 | 34.5 | 35.3 | $-222.63 | -6.6% | $777.37 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1505 | 50.8 | 49.6 | $-293.57 | -2.0% | $706.43 | -0.8 | done | can't tell from luck |
| value_ev10 | 824 | 38.5 | 39.5 | $-549.91 | -6.7% | $450.09 | -1.6 | done | can't tell from luck |
| trend_filter | 1030 | 50.2 | 50.8 | $-568.76 | -5.5% | $431.24 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1839 | 51.4 | 51.0 | $-606.26 | -3.3% | $393.74 | -1.4 | done | can't tell from luck |
| value_ev5 | 1247 | 41.0 | 41.4 | $-619.80 | -5.0% | $380.20 | -1.5 | done | can't tell from luck |
| coinflip | 2577 | 50.2 | 50.5 | $-1159.61 | -4.5% | $-159.61 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1839 | 48.6 | 50.0 | $-1216.14 | -6.6% | $-216.14 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1505 | 49.2 | 51.4 | $-1301.54 | -8.6% | $-301.54 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2577 | 50.5 | 51.7 | $-1476.63 | -5.7% | $-476.63 | -3.0 | done | losing for real |
| always_up | 2577 | 47.3 | 49.7 | $-2220.33 | -8.6% | $-1220.33 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4050 | 48.3 | 49.3 | $-2416.43 |
| ETH | 4468 | 48.2 | 48.7 | $-2666.31 |
| SOL | 4637 | 48.0 | 48.8 | $-2880.26 |
| XRP | 4701 | 48.5 | 48.5 | $-2272.17 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
