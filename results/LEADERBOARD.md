# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 5:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1286 windows, 34437 settled trades, 399 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 679 | 33.9 | 35.3 | $-569.22 | -8.4% | $430.78 | -1.7 | done | can't tell from luck |
| value_ev10 | 1656 | 38.5 | 39.2 | $-866.26 | -5.2% | $133.74 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3454 | 50.8 | 50.2 | $-1114.02 | -3.2% | $-114.02 | -1.9 | done | can't tell from luck |
| value_ev5 | 2501 | 40.4 | 41.1 | $-1313.95 | -5.3% | $-313.95 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2886 | 49.4 | 49.4 | $-1367.94 | -4.7% | $-367.94 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2886 | 50.6 | 51.0 | $-1627.81 | -5.6% | $-627.81 | -3.1 | done | losing for real |
| trend_filter | 2035 | 49.0 | 50.5 | $-1643.73 | -8.1% | $-643.73 | -3.7 | done | losing for real |
| momentum_15m_0.10pct | 3454 | 49.2 | 50.3 | $-2134.31 | -6.2% | $-1134.31 | -3.7 | done | losing for real |
| coinflip | 4962 | 50.0 | 50.1 | $-2285.42 | -4.6% | $-1285.42 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 4962 | 50.5 | 51.4 | $-2786.72 | -5.6% | $-1786.72 | -4.1 | done | losing for real |
| always_up | 4962 | 47.8 | 49.3 | $-3684.02 | -7.4% | $-2684.02 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8238 | 48.0 | 48.8 | $-4903.55 |
| ETH | 8889 | 48.2 | 48.2 | $-4905.62 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
