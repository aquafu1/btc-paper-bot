# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 10:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 826 windows, 22700 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 419 | 33.4 | 34.9 | $-360.80 | -8.6% | $639.20 | -1.3 | done | can't tell from luck |
| value_ev10 | 1038 | 37.6 | 39.1 | $-783.78 | -7.6% | $216.22 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1904 | 50.0 | 49.7 | $-817.75 | -4.3% | $182.25 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2316 | 50.9 | 50.6 | $-844.36 | -3.6% | $155.64 | -1.8 | done | can't tell from luck |
| trend_filter | 1337 | 49.9 | 50.9 | $-924.10 | -6.9% | $75.90 | -2.6 | done | losing for real |
| value_ev5 | 1572 | 39.8 | 41.1 | $-1045.66 | -6.7% | $-45.66 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1904 | 50.0 | 51.1 | $-1343.44 | -7.1% | $-343.44 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 2316 | 49.1 | 50.3 | $-1436.81 | -6.2% | $-436.81 | -3.0 | done | losing for real |
| coinflip | 3298 | 50.2 | 50.3 | $-1470.75 | -4.5% | $-470.75 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3298 | 51.2 | 51.7 | $-1518.75 | -4.6% | $-518.75 | -2.7 | done | losing for real |
| always_up | 3298 | 47.4 | 49.6 | $-2906.88 | -8.8% | $-1906.88 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5151 | 48.2 | 49.1 | $-3158.14 |
| ETH | 5653 | 48.1 | 48.5 | $-3774.19 |
| SOL | 5918 | 48.3 | 48.6 | $-3355.52 |
| XRP | 5978 | 48.5 | 48.5 | $-3165.24 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
