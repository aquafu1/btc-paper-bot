# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 7:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1439 windows, 36653 settled trades, 401 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 740 | 34.5 | 35.3 | $-533.47 | -7.2% | $466.53 | -1.5 | done | can't tell from luck |
| value_ev10 | 1783 | 38.8 | 39.2 | $-801.81 | -4.5% | $198.19 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3660 | 50.9 | 50.0 | $-961.56 | -2.6% | $38.44 | -1.6 | done | can't tell from luck |
| value_ev5 | 2685 | 40.6 | 41.1 | $-1286.25 | -4.8% | $-286.25 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3073 | 49.2 | 49.3 | $-1538.96 | -5.0% | $-538.96 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 3073 | 50.8 | 51.0 | $-1560.64 | -5.1% | $-560.64 | -2.9 | done | losing for real |
| trend_filter | 2175 | 48.6 | 50.3 | $-1885.87 | -8.7% | $-885.87 | -4.1 | done | losing for real |
| coinflip | 5268 | 50.1 | 50.0 | $-2227.02 | -4.2% | $-1227.02 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3660 | 49.1 | 50.2 | $-2296.62 | -6.3% | $-1296.62 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5268 | 50.2 | 51.3 | $-3264.07 | -6.2% | $-2264.07 | -4.6 | done | losing for real |
| always_up | 5268 | 47.9 | 49.2 | $-3608.55 | -6.8% | $-2608.55 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9323 | 48.1 | 48.7 | $-4877.69 |
| ETH | 10020 | 48.0 | 48.0 | $-5502.89 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
