# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 10:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1162 windows, 32126 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 620 | 34.7 | 35.3 | $-375.55 | -6.1% | $624.45 | -1.1 | done | can't tell from luck |
| value_ev10 | 1521 | 38.5 | 39.2 | $-813.32 | -5.3% | $186.68 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3220 | 50.7 | 50.4 | $-1097.50 | -3.4% | $-97.50 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2714 | 49.8 | 49.4 | $-1107.64 | -4.1% | $-107.64 | -2.1 | done | losing for real |
| value_ev5 | 2296 | 40.3 | 41.1 | $-1221.12 | -5.3% | $-221.12 | -2.2 | done | losing for real |
| trend_filter | 1901 | 49.0 | 50.5 | $-1492.25 | -7.8% | $-492.25 | -3.5 | done | losing for real |
| reversal_60m_0.30pct | 2714 | 50.2 | 51.1 | $-1741.67 | -6.4% | $-741.67 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3220 | 49.3 | 50.2 | $-1886.57 | -5.9% | $-886.57 | -3.4 | done | losing for real |
| coinflip | 4640 | 50.2 | 50.2 | $-1988.48 | -4.3% | $-988.48 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 4640 | 50.1 | 51.4 | $-2905.54 | -6.3% | $-1905.54 | -4.4 | done | losing for real |
| always_up | 4640 | 47.8 | 49.3 | $-3416.65 | -7.4% | $-2416.65 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7365 | 48.2 | 49.0 | $-3825.22 |
| ETH | 7963 | 48.2 | 48.4 | $-4568.38 |
| SOL | 8361 | 48.0 | 48.4 | $-4623.90 |
| XRP | 8437 | 48.1 | 48.2 | $-5028.79 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
