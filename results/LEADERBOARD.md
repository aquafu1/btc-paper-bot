# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 2:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1032 windows, 28684 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 531 | 34.7 | 35.1 | $-288.51 | -5.4% | $711.49 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2919 | 51.1 | 50.5 | $-852.51 | -2.9% | $147.49 | -1.6 | done | can't tell from luck |
| value_ev10 | 1319 | 37.5 | 39.2 | $-970.06 | -7.4% | $29.94 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2461 | 49.8 | 49.6 | $-1082.65 | -4.4% | $-82.65 | -2.2 | done | losing for real |
| trend_filter | 1716 | 49.4 | 50.7 | $-1291.06 | -7.5% | $-291.06 | -3.2 | done | losing for real |
| value_ev5 | 1998 | 39.5 | 41.0 | $-1389.38 | -7.0% | $-389.38 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2461 | 50.2 | 51.0 | $-1637.41 | -6.7% | $-637.41 | -3.4 | done | losing for real |
| coinflip | 4120 | 50.5 | 50.3 | $-1680.97 | -4.1% | $-680.97 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2919 | 48.9 | 50.3 | $-1983.27 | -6.8% | $-983.27 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4120 | 50.8 | 51.5 | $-2225.25 | -5.4% | $-1225.25 | -3.6 | done | losing for real |
| always_up | 4120 | 47.5 | 49.5 | $-3555.06 | -8.6% | $-2555.06 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6538 | 48.3 | 49.1 | $-3527.76 |
| ETH | 7118 | 48.2 | 48.5 | $-4354.30 |
| SOL | 7487 | 48.2 | 48.6 | $-4268.59 |
| XRP | 7541 | 48.1 | 48.4 | $-4805.48 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
