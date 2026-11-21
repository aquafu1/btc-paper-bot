# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 12:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 978 windows, 27183 settled trades, 33 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 502 | 34.5 | 34.9 | $-255.26 | -5.1% | $744.74 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2775 | 51.3 | 50.5 | $-732.46 | -2.6% | $267.54 | -1.4 | done | can't tell from luck |
| value_ev10 | 1244 | 37.9 | 39.1 | $-777.53 | -6.3% | $222.47 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2326 | 50.1 | 49.7 | $-927.26 | -4.0% | $72.74 | -1.9 | done | can't tell from luck |
| value_ev5 | 1883 | 39.8 | 41.0 | $-1114.87 | -5.9% | $-114.87 | -2.2 | done | losing for real |
| trend_filter | 1631 | 49.7 | 50.8 | $-1164.18 | -7.1% | $-164.18 | -3.0 | done | losing for real |
| reversal_60m_0.30pct | 2326 | 49.9 | 51.0 | $-1628.45 | -7.0% | $-628.45 | -3.5 | done | losing for real |
| coinflip | 3907 | 50.2 | 50.3 | $-1747.66 | -4.5% | $-747.66 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2775 | 48.7 | 50.3 | $-1989.76 | -7.2% | $-989.76 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3907 | 50.7 | 51.5 | $-2109.15 | -5.4% | $-1109.15 | -3.5 | done | losing for real |
| always_up | 3907 | 46.8 | 49.6 | $-3947.69 | -10.1% | $-2947.69 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6199 | 48.2 | 49.1 | $-3562.25 |
| ETH | 6750 | 48.0 | 48.5 | $-4339.06 |
| SOL | 7102 | 48.1 | 48.6 | $-4104.25 |
| XRP | 7132 | 48.1 | 48.4 | $-4388.68 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
