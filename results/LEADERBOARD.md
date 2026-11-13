# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 12:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 209 windows, 5430 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 534 | 57.3 | 52.8 | $+285.89 | +5.4% | $1285.89 | +1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 415 | 55.7 | 52.7 | $+104.76 | +2.5% | $1104.76 | +0.5 | done | can't tell from luck |
| value_ev20 | 104 | 33.7 | 36.9 | $-137.53 | -13.2% | $862.47 | -1.1 | Sun 4:30 AM | too few trades (104/200) |
| value_ev10 | 270 | 36.7 | 40.8 | $-377.15 | -14.0% | $622.85 | -2.0 | done | can't tell from luck |
| coinflip | 828 | 50.5 | 51.0 | $-432.21 | -5.2% | $567.79 | -1.6 | done | can't tell from luck |
| trend_filter | 280 | 43.6 | 49.8 | $-444.12 | -15.9% | $555.88 | -2.7 | done | losing for real |
| value_ev5 | 394 | 38.8 | 42.5 | $-498.18 | -12.6% | $501.82 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 828 | 50.4 | 51.4 | $-499.38 | -6.0% | $500.62 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 415 | 44.3 | 49.5 | $-589.06 | -14.2% | $410.94 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 534 | 42.7 | 49.5 | $-915.21 | -17.1% | $84.79 | -4.0 | done | losing for real |
| always_up | 828 | 45.5 | 50.2 | $-1111.99 | -13.4% | $-111.99 | -4.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1203 | 46.0 | 49.6 | $-1273.10 |
| ETH | 1355 | 46.3 | 48.8 | $-1324.37 |
| SOL | 1403 | 47.5 | 49.3 | $-1295.69 |
| XRP | 1469 | 49.2 | 49.2 | $-721.02 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
