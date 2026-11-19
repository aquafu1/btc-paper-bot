# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 7:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 814 windows, 22350 settled trades, 26 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 413 | 33.4 | 35.0 | $-341.28 | -8.3% | $658.72 | -1.3 | done | can't tell from luck |
| value_ev10 | 1020 | 37.7 | 39.2 | $-711.12 | -7.0% | $288.88 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1869 | 49.9 | 49.6 | $-790.88 | -4.2% | $209.12 | -1.8 | done | can't tell from luck |
| trend_filter | 1309 | 50.0 | 50.9 | $-849.66 | -6.5% | $150.34 | -2.4 | done | losing for real |
| reversal_15m_0.10pct | 2286 | 50.8 | 50.6 | $-869.86 | -3.8% | $130.14 | -1.8 | done | can't tell from luck |
| value_ev5 | 1542 | 39.9 | 41.1 | $-953.25 | -6.2% | $46.75 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1869 | 50.1 | 51.2 | $-1285.74 | -6.9% | $-285.74 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2286 | 49.2 | 50.3 | $-1338.90 | -5.9% | $-338.90 | -2.8 | done | losing for real |
| momentum_5m_0.00pct | 3252 | 51.3 | 51.7 | $-1403.43 | -4.3% | $-403.43 | -2.5 | done | losing for real |
| coinflip | 3252 | 50.2 | 50.3 | $-1416.67 | -4.4% | $-416.67 | -2.5 | done | losing for real |
| always_up | 3252 | 47.4 | 49.7 | $-2859.92 | -8.8% | $-1859.92 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5072 | 48.3 | 49.1 | $-2918.33 |
| ETH | 5561 | 48.2 | 48.6 | $-3541.96 |
| SOL | 5827 | 48.2 | 48.6 | $-3298.13 |
| XRP | 5890 | 48.4 | 48.5 | $-3062.30 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
