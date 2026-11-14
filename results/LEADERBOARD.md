# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 7:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 285 windows, 7538 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 742 | 54.3 | 51.8 | $+34.04 | +0.5% | $1034.04 | +0.1 | done | can't tell from luck |
| value_ev20 | 140 | 35.0 | 36.4 | $-129.35 | -9.2% | $870.65 | -0.9 | Sun 3:30 AM | too few trades (140/200) |
| reversal_60m_0.30pct | 607 | 52.4 | 51.8 | $-197.75 | -3.3% | $802.25 | -0.8 | done | can't tell from luck |
| value_ev10 | 366 | 38.3 | 40.5 | $-355.03 | -9.7% | $644.97 | -1.6 | done | can't tell from luck |
| trend_filter | 400 | 46.8 | 50.4 | $-472.31 | -11.8% | $527.69 | -2.4 | done | losing for real |
| value_ev5 | 538 | 40.1 | 42.2 | $-493.56 | -9.2% | $506.44 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 607 | 47.6 | 49.8 | $-563.10 | -9.3% | $436.90 | -2.3 | done | losing for real |
| coinflip | 1132 | 49.8 | 50.8 | $-707.63 | -6.3% | $292.37 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1132 | 49.6 | 51.5 | $-866.33 | -7.7% | $133.67 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 742 | 45.7 | 49.9 | $-930.98 | -12.5% | $69.02 | -3.5 | done | losing for real |
| always_up | 1132 | 47.6 | 50.3 | $-1068.59 | -9.4% | $-68.59 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1679 | 46.9 | 49.4 | $-1541.66 |
| ETH | 1884 | 47.2 | 48.8 | $-1681.04 |
| SOL | 1957 | 48.2 | 49.3 | $-1543.40 |
| XRP | 2018 | 48.9 | 49.0 | $-984.49 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
