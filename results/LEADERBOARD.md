# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 6:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 427 windows, 11742 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 213 | 34.7 | 36.2 | $-164.42 | -7.7% | $835.58 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1003 | 50.6 | 50.0 | $-293.31 | -2.9% | $706.69 | -0.9 | done | can't tell from luck |
| value_ev10 | 549 | 39.3 | 40.3 | $-326.49 | -5.9% | $673.51 | -1.2 | done | can't tell from luck |
| trend_filter | 672 | 49.7 | 50.7 | $-405.86 | -6.0% | $594.14 | -1.6 | done | can't tell from luck |
| value_ev5 | 824 | 41.4 | 42.0 | $-434.85 | -5.3% | $565.15 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1189 | 49.2 | 50.0 | $-611.61 | -5.1% | $388.39 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1189 | 50.8 | 51.7 | $-706.65 | -5.9% | $293.35 | -2.2 | done | losing for real |
| coinflip | 1700 | 50.6 | 50.9 | $-734.22 | -4.3% | $265.78 | -1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 1003 | 49.4 | 51.8 | $-896.15 | -8.9% | $103.85 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1700 | 49.6 | 51.6 | $-1257.61 | -7.4% | $-257.61 | -3.2 | done | losing for real |
| always_up | 1700 | 46.2 | 50.5 | $-2074.56 | -12.2% | $-1074.56 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2659 | 47.6 | 49.4 | $-2034.64 |
| ETH | 2945 | 48.0 | 48.9 | $-1869.80 |
| SOL | 3045 | 47.8 | 49.4 | $-2381.45 |
| XRP | 3093 | 48.9 | 49.3 | $-1619.83 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
