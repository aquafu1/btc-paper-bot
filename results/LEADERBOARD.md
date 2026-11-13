# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 8:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 194 windows, 4971 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 485 | 58.4 | 52.6 | $+370.75 | +7.6% | $1370.75 | +1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 361 | 59.3 | 53.0 | $+307.19 | +8.5% | $1307.19 | +1.7 | done | can't tell from luck |
| value_ev20 | 96 | 31.2 | 37.1 | $-208.58 | -21.7% | $791.42 | -1.8 | Sun 6:15 AM | too few trades (96/200) |
| momentum_5m_0.00pct | 769 | 51.5 | 51.3 | $-304.74 | -4.0% | $695.26 | -1.1 | done | can't tell from luck |
| coinflip | 769 | 50.5 | 51.0 | $-436.33 | -5.7% | $563.67 | -1.6 | done | can't tell from luck |
| trend_filter | 245 | 42.0 | 49.4 | $-443.74 | -18.1% | $556.26 | -2.8 | done | losing for real |
| value_ev10 | 257 | 35.4 | 40.9 | $-460.34 | -17.9% | $539.66 | -2.5 | done | losing for real |
| value_ev5 | 374 | 38.0 | 42.6 | $-567.45 | -15.2% | $432.55 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 361 | 40.7 | 49.1 | $-751.84 | -20.8% | $248.16 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 485 | 41.6 | 49.6 | $-946.74 | -19.5% | $53.26 | -4.4 | done | losing for real |
| always_up | 769 | 46.0 | 50.2 | $-1001.22 | -13.0% | $-1.22 | -3.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1096 | 45.8 | 49.5 | $-1198.04 |
| ETH | 1231 | 45.8 | 48.8 | $-1447.81 |
| SOL | 1290 | 47.8 | 49.1 | $-1120.33 |
| XRP | 1354 | 49.3 | 49.2 | $-676.88 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
