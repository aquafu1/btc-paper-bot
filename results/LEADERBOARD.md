# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 6:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 187 windows, 4777 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 348 | 59.8 | 53.0 | $+341.49 | +9.8% | $1341.49 | +2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 464 | 57.1 | 52.4 | $+274.69 | +5.9% | $1274.69 | +1.3 | done | can't tell from luck |
| value_ev20 | 89 | 33.7 | 36.7 | $-138.58 | -15.6% | $861.42 | -1.2 | Sun 11:00 AM | too few trades (89/200) |
| momentum_5m_0.00pct | 744 | 52.0 | 51.4 | $-210.57 | -2.8% | $789.43 | -0.8 | done | can't tell from luck |
| value_ev10 | 239 | 37.2 | 40.7 | $-325.34 | -13.6% | $674.66 | -1.8 | done | can't tell from luck |
| coinflip | 744 | 50.3 | 50.9 | $-418.13 | -5.6% | $581.87 | -1.6 | done | can't tell from luck |
| trend_filter | 239 | 41.8 | 49.5 | $-437.44 | -18.3% | $562.56 | -2.8 | done | losing for real |
| value_ev5 | 354 | 39.0 | 42.5 | $-451.58 | -12.8% | $548.42 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 348 | 40.2 | 49.1 | $-746.81 | -21.5% | $253.19 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 464 | 42.9 | 49.8 | $-793.22 | -17.1% | $206.78 | -3.7 | done | losing for real |
| always_up | 744 | 46.1 | 50.1 | $-925.23 | -12.4% | $74.77 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1046 | 46.0 | 49.5 | $-1052.41 |
| ETH | 1188 | 46.0 | 48.8 | $-1309.31 |
| SOL | 1239 | 47.9 | 49.1 | $-1009.78 |
| XRP | 1304 | 49.9 | 49.2 | $-459.22 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
