# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 10:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 299 windows, 7967 settled trades, 68 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 148 | 35.1 | 36.5 | $-134.69 | -9.1% | $865.31 | -0.9 | Sun 2:30 AM | too few trades (148/200) |
| reversal_15m_0.10pct | 791 | 53.2 | 51.8 | $-139.78 | -1.8% | $860.22 | -0.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 646 | 52.2 | 51.9 | $-253.51 | -3.9% | $746.49 | -1.0 | done | can't tell from luck |
| value_ev10 | 383 | 38.4 | 40.5 | $-361.48 | -9.4% | $638.52 | -1.6 | done | can't tell from luck |
| trend_filter | 435 | 46.7 | 50.3 | $-513.62 | -11.8% | $486.38 | -2.5 | done | losing for real |
| value_ev5 | 563 | 40.0 | 42.2 | $-542.73 | -9.6% | $457.27 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 646 | 47.8 | 49.8 | $-574.60 | -8.9% | $425.40 | -2.3 | done | losing for real |
| coinflip | 1188 | 50.3 | 50.9 | $-659.30 | -5.5% | $340.70 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 791 | 46.8 | 49.9 | $-823.96 | -10.4% | $176.04 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1188 | 49.3 | 51.3 | $-960.16 | -8.1% | $39.84 | -2.9 | done | losing for real |
| always_up | 1188 | 47.1 | 50.3 | $-1247.30 | -10.5% | $-247.30 | -3.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1781 | 46.8 | 49.4 | $-1659.73 |
| ETH | 1996 | 47.1 | 48.8 | $-1833.13 |
| SOL | 2069 | 48.4 | 49.4 | $-1548.92 |
| XRP | 2121 | 48.7 | 49.1 | $-1169.35 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
