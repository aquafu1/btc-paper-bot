# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 6:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 100 windows, 2546 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 188 | 60.1 | 52.8 | $+203.65 | +10.8% | $1203.65 | +1.6 | Wed 8:00 PM | too few trades (188/200) |
| momentum_5m_0.00pct | 392 | 54.6 | 50.7 | $+145.86 | +3.7% | $1145.86 | +0.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 245 | 55.9 | 52.1 | $+119.88 | +4.9% | $1119.88 | +0.8 | done | can't tell from luck |
| value_ev20 | 50 | 28.0 | 36.5 | $-123.85 | -24.8% | $876.15 | -1.4 | Sun 3:15 AM | too few trades (50/200) |
| value_ev10 | 135 | 37.8 | 40.4 | $-145.89 | -10.8% | $854.11 | -1.1 | Thu 7:15 AM | too few trades (135/200) |
| trend_filter | 136 | 44.9 | 49.0 | $-158.60 | -11.7% | $841.40 | -1.3 | Thu 7:00 AM | too few trades (136/200) |
| coinflip | 392 | 50.8 | 51.4 | $-205.30 | -5.2% | $794.70 | -1.1 | done | can't tell from luck |
| value_ev5 | 183 | 36.1 | 41.8 | $-311.33 | -17.0% | $688.67 | -2.0 | Wed 9:00 PM | too few trades (183/200) |
| momentum_15m_0.10pct | 245 | 44.1 | 49.9 | $-358.64 | -14.6% | $641.36 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 188 | 39.9 | 49.1 | $-406.90 | -21.6% | $593.10 | -3.0 | Wed 8:00 PM | too few trades (188/200) |
| always_up | 392 | 46.9 | 50.4 | $-410.88 | -10.5% | $589.12 | -2.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 548 | 46.5 | 49.7 | $-383.42 |
| ETH | 623 | 46.4 | 48.8 | $-475.82 |
| SOL | 680 | 48.5 | 48.4 | $-453.80 |
| XRP | 695 | 50.1 | 49.0 | $-338.95 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
