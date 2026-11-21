# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 8:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 961 windows, 26608 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 488 | 35.2 | 34.9 | $-139.50 | -2.9% | $860.50 | -0.5 | done | can't tell from luck |
| value_ev10 | 1208 | 38.3 | 39.1 | $-602.30 | -5.0% | $397.70 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2719 | 51.4 | 50.6 | $-667.89 | -2.5% | $332.11 | -1.3 | done | can't tell from luck |
| momentum_60m_0.30pct | 2270 | 50.1 | 49.7 | $-901.20 | -4.0% | $98.80 | -1.9 | done | can't tell from luck |
| value_ev5 | 1835 | 40.1 | 41.0 | $-953.13 | -5.2% | $46.87 | -1.9 | done | can't tell from luck |
| trend_filter | 1591 | 49.8 | 50.9 | $-1075.59 | -6.8% | $-75.59 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2270 | 49.9 | 51.0 | $-1578.09 | -7.0% | $-578.09 | -3.4 | done | losing for real |
| coinflip | 3836 | 50.2 | 50.4 | $-1762.76 | -4.6% | $-762.76 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2719 | 48.6 | 50.3 | $-1949.74 | -7.2% | $-949.74 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3836 | 50.8 | 51.5 | $-2019.02 | -5.3% | $-1019.02 | -3.4 | done | losing for real |
| always_up | 3836 | 46.9 | 49.6 | $-3731.74 | -9.7% | $-2731.74 | -6.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6062 | 48.2 | 49.0 | $-3449.96 |
| ETH | 6609 | 48.1 | 48.5 | $-4004.43 |
| SOL | 6949 | 48.3 | 48.6 | $-3754.15 |
| XRP | 6988 | 48.2 | 48.5 | $-4172.43 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
