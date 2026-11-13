# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 8:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 192 windows, 4913 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 479 | 58.5 | 52.6 | $+383.62 | +8.0% | $1383.62 | +1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 358 | 59.8 | 53.1 | $+337.19 | +9.4% | $1337.19 | +1.9 | done | can't tell from luck |
| value_ev20 | 95 | 31.6 | 37.0 | $-198.58 | -20.9% | $801.42 | -1.7 | Sun 6:00 AM | too few trades (95/200) |
| momentum_5m_0.00pct | 760 | 51.7 | 51.4 | $-271.21 | -3.6% | $728.79 | -1.0 | done | can't tell from luck |
| coinflip | 760 | 50.5 | 51.0 | $-414.41 | -5.5% | $585.59 | -1.6 | done | can't tell from luck |
| value_ev10 | 252 | 35.7 | 40.8 | $-433.19 | -17.2% | $566.81 | -2.4 | done | losing for real |
| trend_filter | 243 | 41.6 | 49.4 | $-457.37 | -18.8% | $542.63 | -2.9 | done | losing for real |
| value_ev5 | 369 | 38.2 | 42.6 | $-540.29 | -14.6% | $459.71 | -2.5 | done | losing for real |
| momentum_60m_0.30pct | 358 | 40.2 | 49.0 | $-772.17 | -21.6% | $227.83 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 479 | 41.5 | 49.7 | $-943.22 | -19.7% | $56.78 | -4.4 | done | losing for real |
| always_up | 760 | 46.2 | 50.2 | $-958.35 | -12.6% | $41.65 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1078 | 45.8 | 49.5 | $-1154.80 |
| ETH | 1221 | 45.9 | 48.8 | $-1396.41 |
| SOL | 1272 | 47.7 | 49.1 | $-1111.81 |
| XRP | 1342 | 49.6 | 49.2 | $-604.97 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
