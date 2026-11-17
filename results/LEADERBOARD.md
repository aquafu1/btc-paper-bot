# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 7:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 573 windows, 15869 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1352 | 51.4 | 49.7 | $-188.07 | -1.4% | $811.93 | -0.5 | done | can't tell from luck |
| value_ev20 | 309 | 33.3 | 35.2 | $-327.95 | -10.6% | $672.05 | -1.4 | done | can't tell from luck |
| trend_filter | 921 | 50.8 | 51.1 | $-444.64 | -4.8% | $555.36 | -1.5 | done | can't tell from luck |
| value_ev10 | 748 | 37.6 | 39.4 | $-691.32 | -9.2% | $308.68 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1610 | 50.9 | 51.1 | $-802.75 | -5.0% | $197.25 | -2.0 | done | losing for real |
| value_ev5 | 1115 | 39.7 | 41.3 | $-879.74 | -7.9% | $120.26 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1610 | 49.1 | 49.9 | $-914.55 | -5.7% | $85.45 | -2.3 | done | losing for real |
| coinflip | 2284 | 49.8 | 50.4 | $-1240.72 | -5.4% | $-240.72 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1352 | 48.6 | 51.2 | $-1364.93 | -10.1% | $-364.93 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2284 | 50.4 | 51.9 | $-1551.19 | -6.8% | $-551.19 | -3.4 | done | losing for real |
| always_up | 2284 | 47.1 | 49.9 | $-2283.87 | -10.0% | $-1283.87 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3590 | 47.7 | 49.3 | $-2696.80 |
| ETH | 3960 | 47.9 | 48.6 | $-2719.52 |
| SOL | 4136 | 47.8 | 48.7 | $-3081.01 |
| XRP | 4183 | 48.6 | 48.6 | $-2192.40 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
