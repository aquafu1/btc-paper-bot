# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 12:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 125 windows, 3180 settled trades, 32 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 233 | 61.8 | 53.0 | $+331.07 | +14.2% | $1331.07 | +2.3 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 300 | 57.0 | 52.0 | $+218.10 | +7.3% | $1218.10 | +1.3 | done | can't tell from luck |
| momentum_5m_0.00pct | 493 | 51.9 | 50.8 | $-100.40 | -2.0% | $899.60 | -0.5 | done | can't tell from luck |
| value_ev20 | 61 | 26.2 | 36.4 | $-182.65 | -29.9% | $817.35 | -1.9 | Sun 5:15 AM | too few trades (61/200) |
| value_ev10 | 168 | 37.5 | 40.4 | $-194.30 | -11.6% | $805.70 | -1.3 | Thu 7:15 AM | too few trades (168/200) |
| coinflip | 493 | 50.3 | 51.0 | $-296.52 | -6.0% | $703.48 | -1.4 | done | can't tell from luck |
| trend_filter | 167 | 40.7 | 48.9 | $-330.28 | -19.8% | $669.72 | -2.5 | Thu 7:30 AM | too few trades (167/200) |
| value_ev5 | 239 | 37.2 | 41.9 | $-359.45 | -15.0% | $640.55 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 300 | 43.0 | 50.1 | $-511.14 | -17.0% | $488.86 | -3.0 | done | losing for real |
| momentum_60m_0.30pct | 233 | 38.2 | 49.2 | $-567.49 | -24.4% | $432.51 | -3.8 | done | losing for real |
| always_up | 493 | 46.0 | 50.2 | $-623.81 | -12.7% | $376.19 | -2.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 682 | 44.9 | 49.4 | $-806.86 |
| ETH | 781 | 44.7 | 48.7 | $-928.62 |
| SOL | 846 | 48.3 | 48.6 | $-584.58 |
| XRP | 871 | 50.1 | 48.9 | $-296.81 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
