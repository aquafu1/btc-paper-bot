# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 11:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1358 windows, 35497 settled trades, 406 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 700 | 34.1 | 35.4 | $-561.96 | -8.0% | $438.04 | -1.6 | done | can't tell from luck |
| value_ev10 | 1716 | 38.7 | 39.2 | $-828.63 | -4.8% | $171.37 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3547 | 50.9 | 50.1 | $-976.66 | -2.8% | $23.34 | -1.6 | done | can't tell from luck |
| value_ev5 | 2590 | 40.4 | 41.1 | $-1320.62 | -5.1% | $-320.62 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2984 | 49.3 | 49.4 | $-1462.31 | -4.9% | $-462.31 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2984 | 50.7 | 50.9 | $-1549.88 | -5.2% | $-549.88 | -2.9 | done | losing for real |
| trend_filter | 2111 | 48.5 | 50.4 | $-1879.16 | -8.9% | $-879.16 | -4.2 | done | losing for real |
| coinflip | 5106 | 50.0 | 50.0 | $-2250.41 | -4.4% | $-1250.41 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3547 | 49.1 | 50.3 | $-2261.11 | -6.4% | $-1261.11 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5106 | 50.1 | 51.3 | $-3160.28 | -6.2% | $-2160.28 | -4.5 | done | losing for real |
| always_up | 5106 | 47.8 | 49.3 | $-3763.05 | -7.4% | $-2763.05 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8754 | 47.8 | 48.8 | $-5328.72 |
| ETH | 9433 | 48.1 | 48.2 | $-5101.13 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
