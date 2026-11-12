# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 6:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 99 windows, 2525 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 188 | 60.1 | 52.8 | $+203.65 | +10.8% | $1203.65 | +1.6 | Wed 7:45 PM | too few trades (188/200) |
| momentum_5m_0.00pct | 388 | 54.4 | 50.7 | $+123.41 | +3.2% | $1123.41 | +0.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 241 | 55.6 | 52.2 | $+97.43 | +4.0% | $1097.43 | +0.7 | done | can't tell from luck |
| value_ev20 | 50 | 28.0 | 36.5 | $-123.85 | -24.8% | $876.15 | -1.4 | Sun 2:15 AM | too few trades (50/200) |
| value_ev10 | 135 | 37.8 | 40.4 | $-145.89 | -10.8% | $854.11 | -1.1 | Thu 7:00 AM | too few trades (135/200) |
| trend_filter | 135 | 45.2 | 48.9 | $-148.60 | -11.0% | $851.40 | -1.3 | Thu 7:00 AM | too few trades (135/200) |
| coinflip | 388 | 50.5 | 51.4 | $-224.21 | -5.8% | $775.79 | -1.2 | done | can't tell from luck |
| value_ev5 | 183 | 36.1 | 41.8 | $-311.33 | -17.0% | $688.67 | -2.0 | Wed 8:30 PM | too few trades (183/200) |
| momentum_15m_0.10pct | 241 | 44.4 | 49.8 | $-337.94 | -14.0% | $662.06 | -2.2 | done | losing for real |
| always_up | 388 | 47.2 | 50.3 | $-390.18 | -10.1% | $609.82 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 188 | 39.9 | 49.1 | $-406.90 | -21.6% | $593.10 | -3.0 | Wed 7:45 PM | too few trades (188/200) |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 543 | 46.6 | 49.7 | $-379.10 |
| ETH | 618 | 46.3 | 48.8 | $-489.92 |
| SOL | 674 | 48.5 | 48.4 | $-451.70 |
| XRP | 690 | 50.0 | 49.0 | $-343.69 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
