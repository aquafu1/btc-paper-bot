# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 11:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1262 windows, 34097 settled trades, 390 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 666 | 34.1 | 35.3 | $-534.16 | -8.0% | $465.84 | -1.6 | done | can't tell from luck |
| value_ev10 | 1632 | 38.5 | 39.2 | $-889.12 | -5.4% | $110.88 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3419 | 50.7 | 50.2 | $-1156.34 | -3.4% | $-156.34 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 2862 | 49.6 | 49.4 | $-1250.41 | -4.4% | $-250.41 | -2.3 | done | losing for real |
| value_ev5 | 2468 | 40.3 | 41.1 | $-1368.57 | -5.5% | $-368.57 | -2.3 | done | losing for real |
| trend_filter | 2021 | 49.0 | 50.4 | $-1594.48 | -7.9% | $-594.48 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2862 | 50.4 | 51.1 | $-1740.62 | -6.1% | $-740.62 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3419 | 49.3 | 50.2 | $-2065.76 | -6.0% | $-1065.76 | -3.6 | done | losing for real |
| coinflip | 4916 | 50.1 | 50.1 | $-2187.86 | -4.5% | $-1187.86 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4916 | 50.4 | 51.4 | $-2828.95 | -5.8% | $-1828.95 | -4.2 | done | losing for real |
| always_up | 4916 | 47.9 | 49.4 | $-3593.47 | -7.3% | $-2593.47 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8072 | 48.1 | 48.9 | $-4732.66 |
| ETH | 8715 | 48.2 | 48.3 | $-4892.84 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
