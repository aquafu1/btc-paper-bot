# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 1:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 214 windows, 5588 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 551 | 56.3 | 52.7 | $+205.14 | +3.7% | $1205.14 | +0.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 432 | 54.6 | 52.6 | $+31.71 | +0.7% | $1031.71 | +0.2 | done | can't tell from luck |
| value_ev20 | 105 | 34.3 | 37.0 | $-126.06 | -12.0% | $873.94 | -1.0 | Sun 5:45 AM | too few trades (105/200) |
| value_ev10 | 278 | 37.4 | 40.9 | $-348.28 | -12.5% | $651.72 | -1.8 | done | can't tell from luck |
| trend_filter | 291 | 45.0 | 50.0 | $-389.07 | -13.4% | $610.93 | -2.3 | done | losing for real |
| value_ev5 | 404 | 39.4 | 42.6 | $-471.45 | -11.7% | $528.55 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 848 | 50.6 | 51.5 | $-482.61 | -5.7% | $517.39 | -1.7 | done | can't tell from luck |
| coinflip | 848 | 50.1 | 51.0 | $-498.38 | -5.9% | $501.62 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 432 | 45.4 | 49.6 | $-532.27 | -12.3% | $467.73 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 551 | 43.7 | 49.7 | $-849.80 | -15.4% | $150.20 | -3.7 | done | losing for real |
| always_up | 848 | 46.7 | 50.2 | $-946.77 | -11.2% | $53.23 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1244 | 46.2 | 49.7 | $-1272.92 |
| ETH | 1392 | 46.6 | 48.9 | $-1284.93 |
| SOL | 1441 | 48.0 | 49.3 | $-1189.62 |
| XRP | 1511 | 49.5 | 49.3 | $-660.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
