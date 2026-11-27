# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 6:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1578 windows, 38445 settled trades, 382 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 807 | 34.3 | 35.1 | $-601.63 | -7.5% | $398.37 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3799 | 50.9 | 50.0 | $-961.13 | -2.5% | $38.87 | -1.6 | done | can't tell from luck |
| value_ev10 | 1907 | 38.5 | 39.0 | $-980.92 | -5.1% | $19.08 | -1.8 | done | can't tell from luck |
| value_ev5 | 2862 | 40.4 | 41.0 | $-1440.29 | -5.0% | $-440.29 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3184 | 51.0 | 50.9 | $-1503.91 | -4.7% | $-503.91 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3184 | 49.0 | 49.2 | $-1677.22 | -5.3% | $-677.22 | -3.0 | done | losing for real |
| trend_filter | 2262 | 48.5 | 50.3 | $-1981.52 | -8.8% | $-981.52 | -4.3 | done | losing for real |
| momentum_15m_0.10pct | 3799 | 49.1 | 50.2 | $-2368.36 | -6.2% | $-1368.36 | -3.9 | done | losing for real |
| coinflip | 5547 | 50.0 | 49.9 | $-2371.74 | -4.3% | $-1371.74 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5547 | 50.1 | 51.3 | $-3473.38 | -6.3% | $-2473.38 | -4.8 | done | losing for real |
| always_up | 5547 | 48.2 | 49.1 | $-3547.45 | -6.4% | $-2547.45 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10167 | 47.9 | 48.6 | $-5748.48 |
| ETH | 10968 | 48.0 | 47.7 | $-5574.85 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
