# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 11:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 829 windows, 22776 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 422 | 33.2 | 34.9 | $-390.80 | -9.3% | $609.20 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2322 | 51.0 | 50.6 | $-811.75 | -3.5% | $188.25 | -1.7 | done | can't tell from luck |
| value_ev10 | 1042 | 37.4 | 39.1 | $-823.78 | -7.9% | $176.22 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 1913 | 49.9 | 49.6 | $-873.01 | -4.6% | $126.99 | -2.0 | done | losing for real |
| trend_filter | 1341 | 49.7 | 50.8 | $-964.10 | -7.2% | $35.90 | -2.7 | done | losing for real |
| value_ev5 | 1577 | 39.8 | 41.0 | $-1077.21 | -6.8% | $-77.21 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1913 | 50.1 | 51.1 | $-1331.17 | -7.0% | $-331.17 | -3.1 | done | losing for real |
| coinflip | 3308 | 50.3 | 50.3 | $-1431.66 | -4.3% | $-431.66 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 2322 | 49.0 | 50.2 | $-1496.81 | -6.4% | $-496.81 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 3308 | 51.2 | 51.6 | $-1555.78 | -4.7% | $-555.78 | -2.8 | done | losing for real |
| always_up | 3308 | 47.4 | 49.6 | $-2951.88 | -8.9% | $-1951.88 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5172 | 48.2 | 49.1 | $-3207.17 |
| ETH | 5669 | 48.0 | 48.5 | $-3846.04 |
| SOL | 5941 | 48.2 | 48.6 | $-3436.11 |
| XRP | 5994 | 48.4 | 48.5 | $-3218.63 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
