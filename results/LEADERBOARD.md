# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 9:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 487 windows, 13383 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 247 | 34.8 | 35.8 | $-149.21 | -6.0% | $850.79 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1138 | 51.1 | 49.8 | $-186.36 | -1.6% | $813.64 | -0.6 | done | can't tell from luck |
| value_ev10 | 631 | 38.8 | 40.1 | $-390.56 | -6.2% | $609.44 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1346 | 50.1 | 49.9 | $-433.21 | -3.2% | $566.79 | -1.2 | done | can't tell from luck |
| value_ev5 | 931 | 40.8 | 41.8 | $-526.74 | -5.7% | $473.26 | -1.5 | done | can't tell from luck |
| trend_filter | 786 | 49.4 | 50.7 | $-537.15 | -6.8% | $462.85 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1346 | 49.9 | 51.6 | $-961.77 | -7.1% | $38.23 | -2.7 | done | losing for real |
| coinflip | 1940 | 49.9 | 50.8 | $-1032.41 | -5.3% | $-32.41 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1138 | 48.9 | 51.5 | $-1048.94 | -9.2% | $-48.94 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1940 | 49.5 | 51.6 | $-1487.38 | -7.7% | $-487.38 | -3.5 | done | losing for real |
| always_up | 1940 | 46.4 | 50.4 | $-2256.57 | -11.6% | $-1256.57 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3020 | 47.3 | 49.3 | $-2456.07 |
| ETH | 3355 | 48.0 | 48.8 | $-2197.94 |
| SOL | 3487 | 47.8 | 49.3 | $-2478.93 |
| XRP | 3521 | 48.5 | 49.0 | $-1877.35 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
