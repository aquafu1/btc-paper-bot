# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 11:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 302 windows, 8063 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 149 | 34.9 | 36.4 | $-144.69 | -9.7% | $855.31 | -0.9 | Sun 2:45 AM | too few trades (149/200) |
| reversal_15m_0.10pct | 800 | 53.0 | 51.9 | $-179.84 | -2.2% | $820.16 | -0.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 657 | 52.4 | 51.8 | $-234.74 | -3.6% | $765.26 | -1.0 | done | can't tell from luck |
| value_ev10 | 385 | 38.2 | 40.5 | $-381.48 | -9.9% | $618.52 | -1.7 | done | can't tell from luck |
| trend_filter | 443 | 46.0 | 50.2 | $-573.45 | -12.9% | $426.55 | -2.8 | done | losing for real |
| value_ev5 | 572 | 39.7 | 42.2 | $-592.78 | -10.4% | $407.22 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 657 | 47.6 | 49.9 | $-622.65 | -9.5% | $377.35 | -2.5 | done | losing for real |
| coinflip | 1200 | 50.0 | 50.9 | $-727.50 | -6.1% | $272.50 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 800 | 47.0 | 49.9 | $-798.78 | -10.0% | $201.22 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 1200 | 48.9 | 51.3 | $-1059.99 | -8.8% | $-59.99 | -3.2 | done | losing for real |
| always_up | 1200 | 47.4 | 50.3 | $-1206.35 | -10.1% | $-206.35 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1808 | 46.5 | 49.3 | $-1787.75 |
| ETH | 2019 | 47.1 | 48.8 | $-1902.54 |
| SOL | 2093 | 48.2 | 49.4 | $-1645.62 |
| XRP | 2143 | 48.7 | 49.1 | $-1186.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
