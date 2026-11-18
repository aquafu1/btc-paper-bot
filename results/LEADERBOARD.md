# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 9:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 679 windows, 18788 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 351 | 34.8 | 35.1 | $-184.96 | -5.3% | $815.04 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1594 | 50.5 | 49.6 | $-388.83 | -2.4% | $611.17 | -1.0 | done | can't tell from luck |
| value_ev10 | 865 | 38.6 | 39.3 | $-475.56 | -5.5% | $524.44 | -1.3 | done | can't tell from luck |
| trend_filter | 1097 | 50.4 | 50.9 | $-561.27 | -5.1% | $438.73 | -1.7 | done | can't tell from luck |
| value_ev5 | 1303 | 40.8 | 41.3 | $-632.88 | -4.9% | $367.12 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1930 | 51.4 | 50.9 | $-633.74 | -3.3% | $366.26 | -1.5 | done | can't tell from luck |
| coinflip | 2708 | 50.2 | 50.4 | $-1180.94 | -4.4% | $-180.94 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1930 | 48.6 | 49.9 | $-1243.89 | -6.4% | $-243.89 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1594 | 49.5 | 51.3 | $-1267.75 | -8.0% | $-267.75 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2708 | 50.7 | 51.7 | $-1481.03 | -5.5% | $-481.03 | -2.9 | done | losing for real |
| always_up | 2708 | 47.3 | 49.7 | $-2376.50 | -8.8% | $-1376.50 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4271 | 48.3 | 49.2 | $-2454.63 |
| ETH | 4683 | 48.3 | 48.6 | $-2765.62 |
| SOL | 4896 | 48.2 | 48.7 | $-2830.15 |
| XRP | 4938 | 48.5 | 48.5 | $-2376.95 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
