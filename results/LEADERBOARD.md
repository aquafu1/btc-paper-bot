# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 1:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 309 windows, 8261 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 818 | 53.3 | 51.8 | $-110.30 | -1.3% | $889.70 | -0.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 673 | 52.9 | 51.7 | $-131.55 | -2.0% | $868.45 | -0.5 | done | can't tell from luck |
| value_ev20 | 153 | 34.6 | 36.6 | $-160.14 | -10.5% | $839.86 | -1.0 | Sun 2:30 AM | too few trades (153/200) |
| value_ev10 | 396 | 38.1 | 40.5 | $-396.52 | -10.0% | $603.48 | -1.7 | done | can't tell from luck |
| value_ev5 | 589 | 39.4 | 42.2 | $-642.64 | -10.9% | $357.36 | -2.3 | done | losing for real |
| trend_filter | 454 | 45.4 | 50.4 | $-652.16 | -14.4% | $347.84 | -3.1 | done | losing for real |
| momentum_60m_0.30pct | 673 | 47.1 | 50.0 | $-705.90 | -10.5% | $294.10 | -2.8 | done | losing for real |
| coinflip | 1229 | 50.0 | 50.9 | $-747.23 | -6.1% | $252.77 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 818 | 46.7 | 50.0 | $-872.60 | -10.7% | $127.40 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 1229 | 48.7 | 51.4 | $-1149.90 | -9.4% | $-149.90 | -3.4 | done | losing for real |
| always_up | 1229 | 47.5 | 50.4 | $-1210.35 | -9.8% | $-210.35 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1855 | 46.5 | 49.3 | $-1825.09 |
| ETH | 2065 | 47.1 | 48.8 | $-1918.93 |
| SOL | 2155 | 47.9 | 49.4 | $-1780.46 |
| XRP | 2186 | 48.6 | 49.1 | $-1254.81 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
