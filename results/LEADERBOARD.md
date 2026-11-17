# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 5:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 660 windows, 18264 settled trades, 26 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 343 | 34.1 | 35.4 | $-267.49 | -7.8% | $732.51 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1546 | 50.6 | 49.7 | $-368.45 | -2.4% | $631.55 | -0.9 | done | can't tell from luck |
| trend_filter | 1062 | 50.6 | 51.0 | $-545.94 | -5.1% | $454.06 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1873 | 51.5 | 50.9 | $-560.44 | -3.0% | $439.56 | -1.3 | done | can't tell from luck |
| value_ev10 | 842 | 38.2 | 39.5 | $-611.06 | -7.3% | $388.94 | -1.7 | done | can't tell from luck |
| value_ev5 | 1271 | 40.8 | 41.4 | $-696.42 | -5.5% | $303.58 | -1.7 | done | can't tell from luck |
| coinflip | 2636 | 50.2 | 50.4 | $-1165.26 | -4.4% | $-165.26 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1546 | 49.4 | 51.3 | $-1247.56 | -8.1% | $-247.56 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1873 | 48.5 | 50.1 | $-1276.58 | -6.8% | $-276.58 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2636 | 50.9 | 51.8 | $-1393.03 | -5.3% | $-393.03 | -2.8 | done | losing for real |
| always_up | 2636 | 47.7 | 49.8 | $-2141.33 | -8.1% | $-1141.33 | -4.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4150 | 48.3 | 49.3 | $-2506.66 |
| ETH | 4555 | 48.3 | 48.7 | $-2789.55 |
| SOL | 4756 | 48.2 | 48.8 | $-2760.68 |
| XRP | 4803 | 48.6 | 48.6 | $-2216.66 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
