# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 2:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 601 windows, 16615 settled trades, 38 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 324 | 34.6 | 35.2 | $-214.70 | -6.6% | $785.30 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1406 | 51.1 | 49.6 | $-228.06 | -1.6% | $771.94 | -0.6 | done | can't tell from luck |
| value_ev10 | 777 | 38.2 | 39.4 | $-540.78 | -7.0% | $459.22 | -1.6 | done | can't tell from luck |
| trend_filter | 958 | 50.1 | 50.9 | $-566.54 | -5.9% | $433.46 | -1.9 | done | can't tell from luck |
| value_ev5 | 1165 | 40.5 | 41.2 | $-665.25 | -5.7% | $334.75 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1694 | 50.9 | 50.9 | $-731.05 | -4.3% | $268.95 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 1694 | 49.1 | 50.0 | $-1009.15 | -6.0% | $-9.15 | -2.5 | done | losing for real |
| coinflip | 2397 | 50.0 | 50.5 | $-1189.42 | -5.0% | $-189.42 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1406 | 48.9 | 51.4 | $-1307.71 | -9.3% | $-307.71 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2397 | 50.2 | 51.8 | $-1587.21 | -6.6% | $-587.21 | -3.4 | done | losing for real |
| always_up | 2397 | 47.3 | 49.8 | $-2170.33 | -9.1% | $-1170.33 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3774 | 48.0 | 49.2 | $-2486.35 |
| ETH | 4141 | 48.0 | 48.6 | $-2668.39 |
| SOL | 4317 | 47.9 | 48.7 | $-2885.61 |
| XRP | 4383 | 48.6 | 48.6 | $-2169.85 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
