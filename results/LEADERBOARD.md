# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 1:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1124 windows, 31100 settled trades, 38 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 594 | 34.7 | 35.2 | $-345.99 | -5.8% | $654.01 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3136 | 51.2 | 50.5 | $-794.38 | -2.5% | $205.62 | -1.4 | done | can't tell from luck |
| value_ev10 | 1453 | 38.2 | 39.2 | $-871.58 | -6.0% | $128.42 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2635 | 49.7 | 49.4 | $-1118.41 | -4.2% | $-118.41 | -2.2 | done | losing for real |
| value_ev5 | 2199 | 40.1 | 41.1 | $-1243.65 | -5.7% | $-243.65 | -2.2 | done | losing for real |
| trend_filter | 1848 | 49.1 | 50.4 | $-1428.45 | -7.7% | $-428.45 | -3.4 | done | losing for real |
| reversal_60m_0.30pct | 2635 | 50.3 | 51.1 | $-1667.41 | -6.3% | $-667.41 | -3.3 | done | losing for real |
| coinflip | 4488 | 50.4 | 50.2 | $-1735.31 | -3.9% | $-735.31 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 3136 | 48.8 | 50.2 | $-2123.61 | -6.8% | $-1123.61 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4488 | 50.4 | 51.4 | $-2648.66 | -5.9% | $-1648.66 | -4.1 | done | losing for real |
| always_up | 4488 | 47.7 | 49.3 | $-3419.30 | -7.6% | $-2419.30 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7131 | 48.4 | 49.0 | $-3602.37 |
| ETH | 7705 | 48.1 | 48.4 | $-4640.43 |
| SOL | 8094 | 48.1 | 48.4 | $-4512.71 |
| XRP | 8170 | 48.2 | 48.2 | $-4641.25 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
