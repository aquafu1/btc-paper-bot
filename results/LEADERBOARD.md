# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 1:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 126 windows, 3191 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 234 | 62.0 | 53.1 | $+336.30 | +14.4% | $1336.30 | +2.4 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 300 | 57.0 | 52.0 | $+218.10 | +7.3% | $1218.10 | +1.3 | done | can't tell from luck |
| momentum_5m_0.00pct | 496 | 52.2 | 50.8 | $-82.21 | -1.7% | $917.79 | -0.4 | done | can't tell from luck |
| value_ev20 | 61 | 26.2 | 36.4 | $-182.65 | -29.9% | $817.35 | -1.9 | Sun 5:15 AM | too few trades (61/200) |
| value_ev10 | 168 | 37.5 | 40.4 | $-194.30 | -11.6% | $805.70 | -1.3 | Thu 7:15 AM | too few trades (168/200) |
| coinflip | 496 | 50.4 | 51.1 | $-293.56 | -5.9% | $706.44 | -1.4 | done | can't tell from luck |
| trend_filter | 167 | 40.7 | 48.9 | $-330.28 | -19.8% | $669.72 | -2.5 | Thu 7:30 AM | too few trades (167/200) |
| value_ev5 | 239 | 37.2 | 41.9 | $-359.45 | -15.0% | $640.55 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 300 | 43.0 | 50.1 | $-511.14 | -17.0% | $488.86 | -3.0 | done | losing for real |
| momentum_60m_0.30pct | 234 | 38.0 | 49.1 | $-577.49 | -24.7% | $422.51 | -3.8 | done | losing for real |
| always_up | 496 | 45.8 | 50.2 | $-653.81 | -13.2% | $346.19 | -3.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 685 | 45.0 | 49.5 | $-805.46 |
| ETH | 786 | 44.7 | 48.7 | $-948.16 |
| SOL | 846 | 48.3 | 48.6 | $-584.58 |
| XRP | 874 | 50.1 | 49.0 | $-292.29 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
