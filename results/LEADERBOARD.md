# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 11:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 733 windows, 20183 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 381 | 33.3 | 34.9 | $-334.03 | -8.8% | $665.97 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 2070 | 51.6 | 50.7 | $-446.68 | -2.2% | $553.32 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1696 | 50.2 | 49.6 | $-538.27 | -3.2% | $461.73 | -1.3 | done | can't tell from luck |
| value_ev10 | 921 | 38.1 | 39.1 | $-578.03 | -6.3% | $421.97 | -1.6 | done | can't tell from luck |
| trend_filter | 1185 | 50.2 | 51.0 | $-690.04 | -5.8% | $309.96 | -2.0 | done | losing for real |
| value_ev5 | 1392 | 40.6 | 41.1 | $-703.09 | -5.1% | $296.91 | -1.6 | done | can't tell from luck |
| coinflip | 2924 | 50.3 | 50.3 | $-1171.15 | -4.0% | $-171.15 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1696 | 49.8 | 51.2 | $-1247.67 | -7.4% | $-247.67 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2070 | 48.4 | 50.1 | $-1493.11 | -7.2% | $-493.11 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 2924 | 50.9 | 51.8 | $-1560.38 | -5.3% | $-560.38 | -3.0 | done | losing for real |
| always_up | 2924 | 47.0 | 49.6 | $-2694.18 | -9.2% | $-1694.18 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4571 | 48.1 | 49.1 | $-2852.78 |
| ETH | 5029 | 48.2 | 48.5 | $-3061.10 |
| SOL | 5256 | 48.2 | 48.7 | $-2988.84 |
| XRP | 5327 | 48.5 | 48.5 | $-2553.91 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
