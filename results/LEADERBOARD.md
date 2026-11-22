# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 5:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1141 windows, 31550 settled trades, 24 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 607 | 34.6 | 35.2 | $-382.50 | -6.3% | $617.50 | -1.2 | done | can't tell from luck |
| value_ev10 | 1478 | 38.2 | 39.2 | $-916.39 | -6.2% | $83.61 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3173 | 50.9 | 50.4 | $-962.38 | -3.0% | $37.62 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2664 | 49.6 | 49.4 | $-1193.41 | -4.5% | $-193.41 | -2.3 | done | losing for real |
| value_ev5 | 2236 | 40.1 | 41.1 | $-1289.10 | -5.8% | $-289.10 | -2.3 | done | losing for real |
| trend_filter | 1875 | 48.9 | 50.5 | $-1520.56 | -8.1% | $-520.56 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2664 | 50.4 | 51.1 | $-1620.98 | -6.1% | $-620.98 | -3.2 | done | losing for real |
| coinflip | 4560 | 50.3 | 50.2 | $-1869.99 | -4.1% | $-869.99 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 3173 | 49.1 | 50.2 | $-1988.86 | -6.3% | $-988.86 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4560 | 50.2 | 51.4 | $-2865.99 | -6.3% | $-1865.99 | -4.4 | done | losing for real |
| always_up | 4560 | 47.8 | 49.3 | $-3408.32 | -7.5% | $-2408.32 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7229 | 48.3 | 49.0 | $-3795.15 |
| ETH | 7818 | 48.2 | 48.4 | $-4622.42 |
| SOL | 8215 | 48.1 | 48.4 | $-4575.55 |
| XRP | 8288 | 48.1 | 48.3 | $-5025.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
