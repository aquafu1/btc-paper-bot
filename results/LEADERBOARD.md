# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 5:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 276 windows, 7268 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 715 | 55.0 | 52.2 | $+114.46 | +1.6% | $1114.46 | +0.4 | done | can't tell from luck |
| value_ev20 | 132 | 37.1 | 36.9 | $-49.35 | -3.7% | $950.65 | -0.3 | Sun 6:45 AM | too few trades (132/200) |
| reversal_60m_0.30pct | 583 | 52.3 | 52.2 | $-203.07 | -3.5% | $796.93 | -0.9 | done | can't tell from luck |
| value_ev10 | 353 | 39.1 | 40.8 | $-273.02 | -7.7% | $726.98 | -1.2 | done | can't tell from luck |
| value_ev5 | 516 | 40.9 | 42.4 | $-386.88 | -7.5% | $613.12 | -1.5 | done | can't tell from luck |
| trend_filter | 383 | 46.5 | 50.2 | $-450.31 | -11.8% | $549.69 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 583 | 47.7 | 49.7 | $-507.97 | -8.7% | $492.03 | -2.1 | done | losing for real |
| coinflip | 1096 | 49.8 | 50.9 | $-671.33 | -6.1% | $328.67 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1096 | 49.6 | 51.4 | $-822.85 | -7.5% | $177.15 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 715 | 45.0 | 49.7 | $-941.81 | -13.2% | $58.19 | -3.6 | done | losing for real |
| always_up | 1096 | 47.2 | 50.2 | $-1098.48 | -10.0% | $-98.48 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1624 | 46.8 | 49.5 | $-1523.26 |
| ETH | 1816 | 47.1 | 49.0 | $-1598.68 |
| SOL | 1879 | 48.4 | 49.4 | $-1340.08 |
| XRP | 1949 | 49.0 | 49.1 | $-828.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
