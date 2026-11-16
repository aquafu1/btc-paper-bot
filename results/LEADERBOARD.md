# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 12:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 545 windows, 15129 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1295 | 51.5 | 49.7 | $-187.62 | -1.4% | $812.38 | -0.5 | done | can't tell from luck |
| value_ev20 | 298 | 32.9 | 35.2 | $-362.88 | -12.2% | $637.12 | -1.6 | done | can't tell from luck |
| trend_filter | 882 | 50.8 | 50.9 | $-430.84 | -4.9% | $569.16 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1530 | 49.9 | 49.7 | $-664.47 | -4.3% | $335.53 | -1.7 | done | can't tell from luck |
| value_ev10 | 717 | 36.7 | 39.4 | $-820.87 | -11.4% | $179.13 | -2.6 | done | losing for real |
| value_ev5 | 1063 | 39.0 | 41.2 | $-1034.47 | -9.7% | $-34.47 | -2.7 | done | losing for real |
| reversal_15m_0.10pct | 1530 | 50.1 | 51.2 | $-1109.31 | -7.3% | $-109.31 | -2.9 | done | losing for real |
| coinflip | 2173 | 49.8 | 50.5 | $-1327.59 | -6.1% | $-327.59 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 1295 | 48.5 | 51.2 | $-1353.50 | -10.5% | $-353.50 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 2173 | 50.2 | 51.7 | $-1552.07 | -7.1% | $-552.07 | -3.5 | done | losing for real |
| always_up | 2173 | 46.7 | 50.0 | $-2479.32 | -11.4% | $-1479.32 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3427 | 47.5 | 49.2 | $-2832.28 |
| ETH | 3771 | 47.8 | 48.6 | $-2795.67 |
| SOL | 3945 | 47.6 | 48.7 | $-3153.52 |
| XRP | 3986 | 48.4 | 48.6 | $-2541.46 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
