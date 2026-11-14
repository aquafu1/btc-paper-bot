# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 8:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 338 windows, 9034 settled trades, 64 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 184 | 37.5 | 36.6 | $-38.35 | -2.1% | $961.65 | -0.2 | Sat 4:00 PM | too few trades (184/200) |
| reversal_60m_0.30pct | 721 | 53.3 | 51.9 | $-106.69 | -1.5% | $893.31 | -0.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 894 | 52.7 | 51.9 | $-250.13 | -2.8% | $749.87 | -0.9 | done | can't tell from luck |
| value_ev10 | 443 | 39.1 | 40.2 | $-295.27 | -6.7% | $704.73 | -1.2 | done | can't tell from luck |
| value_ev5 | 657 | 40.6 | 41.9 | $-459.71 | -7.0% | $540.29 | -1.6 | done | can't tell from luck |
| trend_filter | 488 | 45.3 | 50.3 | $-693.95 | -14.2% | $306.05 | -3.2 | done | losing for real |
| coinflip | 1344 | 50.1 | 50.8 | $-735.65 | -5.5% | $264.35 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 721 | 46.7 | 49.7 | $-758.25 | -10.5% | $241.75 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 894 | 47.3 | 49.8 | $-820.45 | -9.2% | $179.55 | -2.8 | done | losing for real |
| momentum_5m_0.00pct | 1344 | 48.7 | 51.3 | $-1210.94 | -9.0% | $-210.94 | -3.4 | done | losing for real |
| always_up | 1344 | 47.5 | 50.5 | $-1321.84 | -9.8% | $-321.84 | -3.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2020 | 46.8 | 49.2 | $-1763.39 |
| ETH | 2272 | 47.4 | 48.6 | $-1753.22 |
| SOL | 2349 | 47.9 | 49.2 | $-1865.91 |
| XRP | 2393 | 48.6 | 49.0 | $-1308.73 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
