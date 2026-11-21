# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 10:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1018 windows, 28360 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 524 | 34.5 | 35.1 | $-292.61 | -5.6% | $707.39 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2892 | 51.1 | 50.5 | $-843.06 | -2.9% | $156.94 | -1.6 | done | can't tell from luck |
| value_ev10 | 1299 | 37.5 | 39.2 | $-959.33 | -7.4% | $40.67 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2444 | 50.0 | 49.6 | $-1019.34 | -4.2% | $-19.34 | -2.1 | done | losing for real |
| trend_filter | 1703 | 49.7 | 50.8 | $-1184.18 | -7.0% | $-184.18 | -2.9 | done | losing for real |
| value_ev5 | 1967 | 39.5 | 41.0 | $-1371.07 | -7.0% | $-371.07 | -2.6 | done | losing for real |
| coinflip | 4065 | 50.5 | 50.4 | $-1659.22 | -4.1% | $-659.22 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2444 | 50.0 | 51.0 | $-1681.18 | -6.9% | $-681.18 | -3.5 | done | losing for real |
| momentum_15m_0.10pct | 2892 | 48.9 | 50.3 | $-1979.98 | -6.8% | $-979.98 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4065 | 50.7 | 51.5 | $-2231.48 | -5.5% | $-1231.48 | -3.6 | done | losing for real |
| always_up | 4065 | 47.3 | 49.5 | $-3656.66 | -9.0% | $-2656.66 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6471 | 48.3 | 49.1 | $-3482.13 |
| ETH | 7047 | 48.1 | 48.5 | $-4429.60 |
| SOL | 7406 | 48.2 | 48.6 | $-4256.08 |
| XRP | 7436 | 48.1 | 48.4 | $-4710.30 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
