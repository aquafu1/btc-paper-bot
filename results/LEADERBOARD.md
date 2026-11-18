# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 12:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 690 windows, 19099 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 367 | 34.1 | 34.9 | $-252.42 | -6.9% | $747.58 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1613 | 50.3 | 49.5 | $-439.40 | -2.7% | $560.60 | -1.1 | done | can't tell from luck |
| value_ev10 | 886 | 38.3 | 39.1 | $-538.58 | -6.1% | $461.42 | -1.5 | done | can't tell from luck |
| trend_filter | 1113 | 50.4 | 50.9 | $-582.44 | -5.2% | $417.56 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1961 | 51.4 | 50.8 | $-633.33 | -3.2% | $366.67 | -1.4 | done | can't tell from luck |
| value_ev5 | 1329 | 40.7 | 41.1 | $-638.70 | -4.8% | $361.30 | -1.5 | done | can't tell from luck |
| coinflip | 2752 | 50.1 | 50.3 | $-1190.92 | -4.3% | $-190.92 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1613 | 49.7 | 51.3 | $-1256.10 | -7.8% | $-256.10 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1961 | 48.6 | 50.0 | $-1278.73 | -6.5% | $-278.73 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 2752 | 50.8 | 51.8 | $-1504.09 | -5.5% | $-504.09 | -3.0 | done | losing for real |
| always_up | 2752 | 47.5 | 49.6 | $-2289.43 | -8.3% | $-1289.43 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4338 | 48.3 | 49.1 | $-2493.30 |
| ETH | 4757 | 48.3 | 48.5 | $-2729.53 |
| SOL | 4977 | 48.2 | 48.6 | $-2902.17 |
| XRP | 5027 | 48.5 | 48.3 | $-2479.16 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
