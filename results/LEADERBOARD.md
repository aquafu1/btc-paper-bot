# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 10:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 827 windows, 22713 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 419 | 33.4 | 34.9 | $-360.80 | -8.6% | $639.20 | -1.3 | done | can't tell from luck |
| value_ev10 | 1038 | 37.6 | 39.1 | $-783.78 | -7.6% | $216.22 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1906 | 50.1 | 49.7 | $-803.01 | -4.2% | $196.99 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 2317 | 50.9 | 50.6 | $-838.08 | -3.6% | $161.92 | -1.7 | done | can't tell from luck |
| trend_filter | 1337 | 49.9 | 50.9 | $-924.10 | -6.9% | $75.90 | -2.6 | done | losing for real |
| value_ev5 | 1573 | 39.9 | 41.1 | $-1037.21 | -6.6% | $-37.21 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1906 | 49.9 | 51.1 | $-1363.44 | -7.2% | $-363.44 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 2317 | 49.1 | 50.3 | $-1446.81 | -6.2% | $-446.81 | -3.0 | done | losing for real |
| coinflip | 3300 | 50.2 | 50.3 | $-1456.02 | -4.4% | $-456.02 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3300 | 51.2 | 51.7 | $-1538.75 | -4.7% | $-538.75 | -2.8 | done | losing for real |
| always_up | 3300 | 47.4 | 49.6 | $-2926.88 | -8.9% | $-1926.88 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5157 | 48.2 | 49.1 | $-3162.76 |
| ETH | 5653 | 48.1 | 48.5 | $-3774.19 |
| SOL | 5925 | 48.3 | 48.6 | $-3376.69 |
| XRP | 5978 | 48.5 | 48.5 | $-3165.24 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
