# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 3:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 989 windows, 27495 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 505 | 34.3 | 34.9 | $-285.26 | -5.6% | $714.74 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2808 | 51.1 | 50.4 | $-838.21 | -3.0% | $161.79 | -1.6 | done | can't tell from luck |
| value_ev10 | 1257 | 37.5 | 39.1 | $-881.38 | -7.0% | $118.62 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2363 | 49.9 | 49.7 | $-1073.32 | -4.5% | $-73.32 | -2.2 | done | losing for real |
| trend_filter | 1646 | 49.6 | 50.9 | $-1192.65 | -7.2% | $-192.65 | -3.0 | done | losing for real |
| value_ev5 | 1901 | 39.5 | 41.0 | $-1268.73 | -6.7% | $-268.73 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2363 | 50.1 | 50.9 | $-1546.32 | -6.5% | $-546.32 | -3.3 | done | losing for real |
| coinflip | 3948 | 50.3 | 50.3 | $-1776.54 | -4.5% | $-776.54 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2808 | 48.9 | 50.4 | $-1930.76 | -6.9% | $-930.76 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 3948 | 50.9 | 51.5 | $-2037.06 | -5.2% | $-1037.06 | -3.3 | done | losing for real |
| always_up | 3948 | 46.8 | 49.6 | $-3989.45 | -10.1% | $-2989.45 | -6.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6269 | 48.2 | 49.1 | $-3550.78 |
| ETH | 6832 | 48.0 | 48.5 | $-4480.72 |
| SOL | 7183 | 48.1 | 48.6 | $-4258.41 |
| XRP | 7211 | 48.1 | 48.5 | $-4529.77 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
