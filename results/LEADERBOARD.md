# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 8:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1154 windows, 31877 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 614 | 34.5 | 35.2 | $-397.85 | -6.5% | $602.15 | -1.2 | done | can't tell from luck |
| value_ev10 | 1504 | 38.3 | 39.2 | $-871.63 | -5.8% | $128.37 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3200 | 50.8 | 50.4 | $-1037.24 | -3.2% | $-37.24 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2687 | 49.7 | 49.5 | $-1172.85 | -4.4% | $-172.85 | -2.3 | done | losing for real |
| value_ev5 | 2272 | 40.2 | 41.1 | $-1249.73 | -5.5% | $-249.73 | -2.2 | done | losing for real |
| trend_filter | 1889 | 49.0 | 50.5 | $-1513.44 | -8.0% | $-513.44 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2687 | 50.3 | 51.0 | $-1680.43 | -6.3% | $-680.43 | -3.3 | done | losing for real |
| coinflip | 4608 | 50.2 | 50.2 | $-1921.39 | -4.2% | $-921.39 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 3200 | 49.2 | 50.2 | $-1943.17 | -6.1% | $-943.17 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 4608 | 50.1 | 51.4 | $-2909.33 | -6.3% | $-1909.33 | -4.4 | done | losing for real |
| always_up | 4608 | 47.7 | 49.3 | $-3477.02 | -7.5% | $-2477.02 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7304 | 48.2 | 49.0 | $-3808.09 |
| ETH | 7899 | 48.1 | 48.4 | $-4673.79 |
| SOL | 8296 | 48.0 | 48.4 | $-4648.11 |
| XRP | 8378 | 48.1 | 48.2 | $-5044.10 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
