# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 10:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1163 windows, 32157 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 620 | 34.7 | 35.3 | $-375.55 | -6.1% | $624.45 | -1.1 | done | can't tell from luck |
| value_ev10 | 1523 | 38.5 | 39.2 | $-809.07 | -5.3% | $190.93 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3222 | 50.8 | 50.4 | $-1083.13 | -3.4% | $-83.13 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2718 | 49.8 | 49.4 | $-1104.61 | -4.1% | $-104.61 | -2.1 | done | losing for real |
| value_ev5 | 2298 | 40.3 | 41.1 | $-1216.87 | -5.3% | $-216.87 | -2.1 | done | losing for real |
| trend_filter | 1904 | 49.0 | 50.4 | $-1498.00 | -7.9% | $-498.00 | -3.5 | done | losing for real |
| reversal_60m_0.30pct | 2718 | 50.2 | 51.1 | $-1747.30 | -6.4% | $-747.30 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3222 | 49.2 | 50.2 | $-1906.57 | -5.9% | $-906.57 | -3.4 | done | losing for real |
| coinflip | 4644 | 50.1 | 50.2 | $-2010.70 | -4.3% | $-1010.70 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 4644 | 50.1 | 51.4 | $-2921.29 | -6.3% | $-1921.29 | -4.4 | done | losing for real |
| always_up | 4644 | 47.8 | 49.3 | $-3413.63 | -7.4% | $-2413.63 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7373 | 48.2 | 49.0 | $-3851.90 |
| ETH | 7973 | 48.2 | 48.4 | $-4635.18 |
| SOL | 8369 | 48.1 | 48.4 | $-4558.42 |
| XRP | 8442 | 48.1 | 48.2 | $-5041.23 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
