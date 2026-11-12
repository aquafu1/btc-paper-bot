# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 12:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 170 windows, 4352 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 320 | 60.9 | 53.3 | $+383.96 | +12.0% | $1383.96 | +2.3 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 425 | 58.4 | 52.7 | $+351.87 | +8.3% | $1351.87 | +1.8 | done | can't tell from luck |
| value_ev20 | 80 | 35.0 | 37.1 | $-101.99 | -12.7% | $898.01 | -0.9 | Sun 6:30 AM | too few trades (80/200) |
| momentum_5m_0.00pct | 672 | 51.8 | 51.2 | $-188.50 | -2.8% | $811.50 | -0.8 | done | can't tell from luck |
| value_ev10 | 219 | 37.9 | 40.8 | $-261.47 | -11.9% | $738.53 | -1.5 | done | can't tell from luck |
| value_ev5 | 324 | 39.2 | 42.6 | $-392.86 | -12.1% | $607.14 | -2.0 | done | can't tell from luck |
| coinflip | 672 | 50.0 | 51.0 | $-412.69 | -6.1% | $587.31 | -1.6 | done | can't tell from luck |
| trend_filter | 223 | 40.4 | 49.1 | $-452.69 | -20.3% | $547.31 | -3.0 | done | losing for real |
| momentum_60m_0.30pct | 320 | 39.1 | 48.9 | $-733.80 | -22.9% | $266.20 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 425 | 41.6 | 49.5 | $-797.00 | -18.8% | $203.00 | -3.9 | done | losing for real |
| always_up | 672 | 46.0 | 50.0 | $-815.51 | -12.1% | $184.49 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 945 | 45.9 | 49.5 | $-900.21 |
| ETH | 1083 | 45.7 | 48.9 | $-1202.10 |
| SOL | 1143 | 47.9 | 49.0 | $-899.54 |
| XRP | 1181 | 49.9 | 49.1 | $-418.85 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
