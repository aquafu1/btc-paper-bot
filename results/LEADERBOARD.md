# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 6:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 619 windows, 17110 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1448 | 51.4 | 49.6 | $-121.95 | -0.8% | $878.05 | -0.3 | done | can't tell from luck |
| value_ev20 | 328 | 34.1 | 35.3 | $-254.70 | -7.8% | $745.30 | -1.1 | done | can't tell from luck |
| trend_filter | 991 | 50.5 | 50.9 | $-501.42 | -5.1% | $498.58 | -1.6 | done | can't tell from luck |
| value_ev10 | 793 | 38.1 | 39.4 | $-597.33 | -7.5% | $402.67 | -1.7 | done | can't tell from luck |
| value_ev5 | 1196 | 40.2 | 41.3 | $-790.34 | -6.6% | $209.66 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1751 | 50.7 | 51.0 | $-834.37 | -4.8% | $165.63 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 1751 | 49.3 | 50.0 | $-928.14 | -5.3% | $71.86 | -2.2 | done | losing for real |
| coinflip | 2468 | 50.0 | 50.5 | $-1217.37 | -4.9% | $-217.37 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1448 | 48.6 | 51.4 | $-1425.08 | -9.8% | $-425.08 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 2468 | 50.4 | 51.7 | $-1538.68 | -6.2% | $-538.68 | -3.2 | done | losing for real |
| always_up | 2468 | 47.3 | 49.7 | $-2200.26 | -8.9% | $-1200.26 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3887 | 48.1 | 49.2 | $-2499.77 |
| ETH | 4281 | 48.0 | 48.6 | $-2782.06 |
| SOL | 4443 | 47.9 | 48.8 | $-2923.64 |
| XRP | 4499 | 48.5 | 48.6 | $-2204.17 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
