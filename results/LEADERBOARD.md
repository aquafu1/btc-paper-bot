# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 10:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 297 windows, 7910 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 147 | 35.4 | 36.4 | $-124.69 | -8.5% | $875.31 | -0.8 | Sun 2:45 AM | too few trades (147/200) |
| reversal_15m_0.10pct | 785 | 53.2 | 51.9 | $-138.54 | -1.8% | $861.46 | -0.5 | done | can't tell from luck |
| reversal_60m_0.30pct | 639 | 51.8 | 51.9 | $-293.99 | -4.6% | $706.01 | -1.2 | done | can't tell from luck |
| value_ev10 | 382 | 38.5 | 40.4 | $-351.48 | -9.2% | $648.52 | -1.5 | done | can't tell from luck |
| trend_filter | 429 | 47.1 | 50.2 | $-471.01 | -11.0% | $528.99 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 639 | 48.2 | 49.8 | $-521.99 | -8.2% | $478.01 | -2.1 | done | losing for real |
| value_ev5 | 561 | 40.1 | 42.1 | $-522.73 | -9.3% | $477.27 | -1.9 | done | can't tell from luck |
| coinflip | 1181 | 50.3 | 50.9 | $-644.90 | -5.5% | $355.10 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 785 | 46.8 | 49.9 | $-816.33 | -10.4% | $183.67 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1181 | 49.4 | 51.3 | $-924.28 | -7.8% | $75.72 | -2.8 | done | losing for real |
| always_up | 1181 | 46.9 | 50.3 | $-1287.78 | -10.9% | $-287.78 | -3.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1773 | 46.8 | 49.4 | $-1632.56 |
| ETH | 1977 | 47.3 | 48.7 | $-1756.91 |
| SOL | 2053 | 48.3 | 49.3 | $-1558.47 |
| XRP | 2107 | 48.6 | 49.0 | $-1149.77 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
