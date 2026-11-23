# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 3:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1181 windows, 32645 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 637 | 34.9 | 35.3 | $-369.65 | -5.8% | $630.35 | -1.1 | done | can't tell from luck |
| value_ev10 | 1547 | 38.5 | 39.2 | $-807.44 | -5.2% | $192.56 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3273 | 50.7 | 50.3 | $-1104.39 | -3.4% | $-104.39 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2748 | 49.6 | 49.4 | $-1212.76 | -4.4% | $-212.76 | -2.3 | done | losing for real |
| value_ev5 | 2340 | 40.2 | 41.1 | $-1296.14 | -5.5% | $-296.14 | -2.3 | done | losing for real |
| trend_filter | 1931 | 48.9 | 50.5 | $-1564.65 | -8.1% | $-564.65 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2748 | 50.4 | 51.0 | $-1692.32 | -6.2% | $-692.32 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3273 | 49.3 | 50.2 | $-1949.85 | -6.0% | $-949.85 | -3.4 | done | losing for real |
| coinflip | 4716 | 50.0 | 50.1 | $-2175.82 | -4.6% | $-1175.82 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4716 | 50.2 | 51.4 | $-2936.20 | -6.2% | $-1936.20 | -4.4 | done | losing for real |
| always_up | 4716 | 47.9 | 49.3 | $-3409.04 | -7.2% | $-2409.04 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7489 | 48.2 | 48.9 | $-4086.58 |
| ETH | 8096 | 48.1 | 48.4 | $-4860.16 |
| SOL | 8489 | 48.1 | 48.4 | $-4483.92 |
| XRP | 8571 | 48.1 | 48.2 | $-5087.61 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
