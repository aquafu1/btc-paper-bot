# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 8:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 816 windows, 22376 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 413 | 33.4 | 35.0 | $-341.28 | -8.3% | $658.72 | -1.3 | done | can't tell from luck |
| value_ev10 | 1021 | 37.7 | 39.2 | $-721.12 | -7.1% | $278.88 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1871 | 50.0 | 49.7 | $-782.17 | -4.2% | $217.83 | -1.8 | done | can't tell from luck |
| trend_filter | 1312 | 50.1 | 50.9 | $-835.49 | -6.4% | $164.51 | -2.4 | done | losing for real |
| reversal_15m_0.10pct | 2288 | 50.8 | 50.6 | $-859.16 | -3.8% | $140.84 | -1.8 | done | can't tell from luck |
| value_ev5 | 1544 | 40.0 | 41.1 | $-958.01 | -6.2% | $41.99 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1871 | 50.0 | 51.2 | $-1305.74 | -7.0% | $-305.74 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2288 | 49.2 | 50.3 | $-1358.90 | -5.9% | $-358.90 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 3256 | 51.4 | 51.7 | $-1399.26 | -4.3% | $-399.26 | -2.5 | done | losing for real |
| coinflip | 3256 | 50.1 | 50.3 | $-1456.67 | -4.5% | $-456.67 | -2.6 | done | losing for real |
| always_up | 3256 | 47.5 | 49.7 | $-2840.51 | -8.7% | $-1840.51 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5078 | 48.3 | 49.1 | $-2932.64 |
| ETH | 5567 | 48.2 | 48.6 | $-3540.11 |
| SOL | 5835 | 48.2 | 48.6 | $-3319.81 |
| XRP | 5896 | 48.5 | 48.5 | $-3065.78 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
