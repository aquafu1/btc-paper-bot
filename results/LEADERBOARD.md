# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 6:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 98 windows, 2491 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 185 | 59.5 | 52.7 | $+183.74 | +9.9% | $1183.74 | +1.4 | Wed 8:00 PM | too few trades (185/200) |
| momentum_5m_0.00pct | 384 | 54.9 | 50.8 | $+163.41 | +4.3% | $1163.41 | +0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 238 | 56.3 | 52.3 | $+127.43 | +5.4% | $1127.43 | +0.9 | done | can't tell from luck |
| value_ev10 | 132 | 38.6 | 40.4 | $-115.89 | -8.8% | $884.11 | -0.9 | Thu 7:30 AM | too few trades (132/200) |
| trend_filter | 132 | 46.2 | 49.1 | $-118.60 | -9.0% | $881.40 | -1.0 | Thu 7:30 AM | too few trades (132/200) |
| value_ev20 | 50 | 28.0 | 36.5 | $-123.85 | -24.8% | $876.15 | -1.4 | Sun 1:15 AM | too few trades (50/200) |
| coinflip | 384 | 50.3 | 51.4 | $-234.12 | -6.1% | $765.88 | -1.2 | done | can't tell from luck |
| value_ev5 | 179 | 36.9 | 41.7 | $-271.33 | -15.2% | $728.67 | -1.8 | Wed 9:00 PM | too few trades (179/200) |
| momentum_15m_0.10pct | 238 | 43.7 | 49.7 | $-357.70 | -15.0% | $642.30 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 185 | 40.5 | 49.2 | $-376.90 | -20.4% | $623.10 | -2.8 | Wed 8:00 PM | too few trades (185/200) |
| always_up | 384 | 46.6 | 50.2 | $-416.03 | -10.8% | $583.97 | -2.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 535 | 46.9 | 49.7 | $-331.00 |
| ETH | 609 | 46.3 | 48.8 | $-470.35 |
| SOL | 666 | 48.6 | 48.4 | $-420.00 |
| XRP | 681 | 50.1 | 48.9 | $-318.49 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
