# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 12:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 306 windows, 8185 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 666 | 52.9 | 51.7 | $-143.15 | -2.1% | $856.85 | -0.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 811 | 53.1 | 51.8 | $-149.84 | -1.8% | $850.16 | -0.6 | done | can't tell from luck |
| value_ev20 | 152 | 34.9 | 36.5 | $-150.14 | -9.9% | $849.86 | -1.0 | Sun 2:00 AM | too few trades (152/200) |
| value_ev10 | 395 | 38.2 | 40.5 | $-386.52 | -9.8% | $613.48 | -1.7 | done | can't tell from luck |
| value_ev5 | 584 | 39.7 | 42.2 | $-592.64 | -10.1% | $407.36 | -2.2 | done | losing for real |
| trend_filter | 452 | 45.6 | 50.4 | $-632.16 | -14.0% | $367.84 | -3.1 | done | losing for real |
| momentum_60m_0.30pct | 666 | 47.1 | 50.0 | $-695.35 | -10.4% | $304.65 | -2.8 | done | losing for real |
| coinflip | 1216 | 50.1 | 50.9 | $-714.14 | -5.9% | $285.86 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 811 | 46.9 | 49.9 | $-837.77 | -10.3% | $162.23 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1216 | 48.8 | 51.3 | $-1108.29 | -9.1% | $-108.29 | -3.3 | done | losing for real |
| always_up | 1216 | 47.5 | 50.4 | $-1233.98 | -10.1% | $-233.98 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1841 | 46.5 | 49.3 | $-1821.23 |
| ETH | 2047 | 47.1 | 48.8 | $-1891.76 |
| SOL | 2123 | 48.1 | 49.4 | $-1670.23 |
| XRP | 2174 | 48.6 | 49.1 | $-1260.75 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
