# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 1:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 980 windows, 27216 settled trades, 66 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 502 | 34.5 | 34.9 | $-255.26 | -5.1% | $744.74 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2780 | 51.2 | 50.5 | $-764.99 | -2.8% | $235.01 | -1.5 | done | can't tell from luck |
| value_ev10 | 1245 | 37.8 | 39.1 | $-787.53 | -6.3% | $212.47 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2328 | 50.0 | 49.7 | $-947.26 | -4.1% | $52.74 | -2.0 | done | can't tell from luck |
| value_ev5 | 1884 | 39.8 | 41.0 | $-1124.87 | -6.0% | $-124.87 | -2.2 | done | losing for real |
| trend_filter | 1633 | 49.6 | 50.8 | $-1184.18 | -7.3% | $-184.18 | -3.0 | done | losing for real |
| reversal_60m_0.30pct | 2328 | 50.0 | 51.0 | $-1611.08 | -6.9% | $-611.08 | -3.4 | done | losing for real |
| coinflip | 3912 | 50.2 | 50.3 | $-1760.30 | -4.5% | $-760.30 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2780 | 48.8 | 50.3 | $-1960.29 | -7.1% | $-960.29 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3912 | 50.7 | 51.5 | $-2099.58 | -5.4% | $-1099.58 | -3.5 | done | losing for real |
| always_up | 3912 | 46.8 | 49.6 | $-3900.76 | -10.0% | $-2900.76 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6204 | 48.2 | 49.1 | $-3551.38 |
| ETH | 6765 | 48.0 | 48.5 | $-4362.29 |
| SOL | 7107 | 48.1 | 48.6 | $-4093.34 |
| XRP | 7140 | 48.2 | 48.4 | $-4389.08 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
