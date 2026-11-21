# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 1:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 981 windows, 27249 settled trades, 66 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 502 | 34.5 | 34.9 | $-255.26 | -5.1% | $744.74 | -0.9 | done | can't tell from luck |
| value_ev10 | 1245 | 37.8 | 39.1 | $-787.53 | -6.3% | $212.47 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 2784 | 51.1 | 50.4 | $-804.99 | -2.9% | $195.01 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2332 | 50.1 | 49.7 | $-922.91 | -4.0% | $77.09 | -1.9 | done | can't tell from luck |
| value_ev5 | 1885 | 39.8 | 41.0 | $-1134.87 | -6.0% | $-134.87 | -2.2 | done | losing for real |
| trend_filter | 1637 | 49.7 | 50.9 | $-1159.82 | -7.1% | $-159.82 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2332 | 49.9 | 50.9 | $-1651.08 | -7.1% | $-651.08 | -3.5 | done | losing for real |
| coinflip | 3916 | 50.2 | 50.3 | $-1767.56 | -4.5% | $-767.56 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2784 | 48.9 | 50.3 | $-1935.94 | -7.0% | $-935.94 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 3916 | 50.8 | 51.5 | $-2075.23 | -5.3% | $-1075.23 | -3.4 | done | losing for real |
| always_up | 3916 | 46.9 | 49.6 | $-3876.40 | -9.9% | $-2876.40 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6212 | 48.2 | 49.1 | $-3528.38 |
| ETH | 6773 | 48.0 | 48.5 | $-4370.05 |
| SOL | 7116 | 48.1 | 48.6 | $-4089.93 |
| XRP | 7148 | 48.2 | 48.5 | $-4383.24 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
