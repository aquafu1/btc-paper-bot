# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 8:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 194 windows, 4963 settled trades, 64 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 484 | 58.5 | 52.6 | $+380.75 | +7.9% | $1380.75 | +1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 360 | 59.4 | 53.0 | $+317.19 | +8.8% | $1317.19 | +1.8 | done | can't tell from luck |
| value_ev20 | 96 | 31.2 | 37.1 | $-208.58 | -21.7% | $791.42 | -1.8 | Sun 5:45 AM | too few trades (96/200) |
| momentum_5m_0.00pct | 768 | 51.4 | 51.3 | $-312.35 | -4.1% | $687.65 | -1.2 | done | can't tell from luck |
| coinflip | 768 | 50.4 | 51.0 | $-443.94 | -5.8% | $556.06 | -1.7 | done | can't tell from luck |
| trend_filter | 244 | 41.8 | 49.4 | $-451.35 | -18.5% | $548.65 | -2.9 | done | losing for real |
| value_ev10 | 257 | 35.4 | 40.9 | $-460.34 | -17.9% | $539.66 | -2.5 | done | losing for real |
| value_ev5 | 374 | 38.0 | 42.6 | $-567.45 | -15.2% | $432.55 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 360 | 40.6 | 49.1 | $-759.45 | -21.1% | $240.55 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 484 | 41.5 | 49.6 | $-954.35 | -19.7% | $45.65 | -4.4 | done | losing for real |
| always_up | 768 | 46.1 | 50.3 | $-991.22 | -12.9% | $8.78 | -3.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1088 | 45.7 | 49.5 | $-1206.09 |
| ETH | 1231 | 45.8 | 48.8 | $-1447.81 |
| SOL | 1290 | 47.8 | 49.1 | $-1120.33 |
| XRP | 1354 | 49.3 | 49.2 | $-676.88 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
