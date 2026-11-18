# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 9:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 726 windows, 19995 settled trades, 33 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 381 | 33.3 | 34.9 | $-334.03 | -8.8% | $665.97 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 2048 | 51.9 | 50.7 | $-372.79 | -1.8% | $627.21 | -0.8 | done | can't tell from luck |
| value_ev10 | 917 | 38.1 | 39.1 | $-585.38 | -6.4% | $414.62 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1674 | 49.9 | 49.5 | $-630.14 | -3.8% | $369.86 | -1.5 | done | can't tell from luck |
| value_ev5 | 1385 | 40.6 | 41.1 | $-680.43 | -4.9% | $319.57 | -1.5 | done | can't tell from luck |
| trend_filter | 1171 | 49.9 | 50.9 | $-748.12 | -6.4% | $251.88 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1674 | 50.1 | 51.3 | $-1135.84 | -6.8% | $-135.84 | -2.8 | done | losing for real |
| coinflip | 2899 | 50.3 | 50.3 | $-1191.75 | -4.1% | $-191.75 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2048 | 48.1 | 50.1 | $-1552.37 | -7.6% | $-552.37 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2899 | 50.8 | 51.8 | $-1597.08 | -5.5% | $-597.08 | -3.1 | done | losing for real |
| always_up | 2899 | 47.2 | 49.6 | $-2590.28 | -8.9% | $-1590.28 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4527 | 48.1 | 49.1 | $-2865.71 |
| ETH | 4984 | 48.2 | 48.5 | $-3022.63 |
| SOL | 5212 | 48.1 | 48.7 | $-3053.38 |
| XRP | 5272 | 48.5 | 48.4 | $-2476.49 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
