# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 10:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 825 windows, 22666 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 419 | 33.4 | 34.9 | $-360.80 | -8.6% | $639.20 | -1.3 | done | can't tell from luck |
| value_ev10 | 1038 | 37.6 | 39.1 | $-783.78 | -7.6% | $216.22 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1899 | 50.0 | 49.7 | $-822.72 | -4.3% | $177.28 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2312 | 50.9 | 50.6 | $-860.38 | -3.7% | $139.62 | -1.8 | done | can't tell from luck |
| trend_filter | 1336 | 49.9 | 50.9 | $-914.10 | -6.8% | $85.90 | -2.6 | done | losing for real |
| value_ev5 | 1572 | 39.8 | 41.1 | $-1045.66 | -6.7% | $-45.66 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1899 | 50.0 | 51.1 | $-1328.69 | -7.0% | $-328.69 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2312 | 49.1 | 50.3 | $-1414.29 | -6.1% | $-414.29 | -3.0 | done | losing for real |
| coinflip | 3293 | 50.2 | 50.3 | $-1473.76 | -4.5% | $-473.76 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3293 | 51.3 | 51.7 | $-1485.48 | -4.5% | $-485.48 | -2.7 | done | losing for real |
| always_up | 3293 | 47.4 | 49.6 | $-2892.13 | -8.8% | $-1892.13 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5151 | 48.2 | 49.1 | $-3158.14 |
| ETH | 5639 | 48.1 | 48.5 | $-3727.59 |
| SOL | 5910 | 48.3 | 48.6 | $-3349.59 |
| XRP | 5966 | 48.5 | 48.5 | $-3146.49 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
