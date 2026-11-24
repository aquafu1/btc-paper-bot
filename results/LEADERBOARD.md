# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 1:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1319 windows, 34957 settled trades, 433 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 687 | 34.2 | 35.3 | $-530.82 | -7.7% | $469.18 | -1.5 | done | can't tell from luck |
| value_ev10 | 1685 | 38.8 | 39.2 | $-782.80 | -4.6% | $217.20 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3502 | 50.9 | 50.2 | $-1026.82 | -2.9% | $-26.82 | -1.7 | done | can't tell from luck |
| value_ev5 | 2543 | 40.5 | 41.1 | $-1260.73 | -5.0% | $-260.73 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2937 | 49.4 | 49.4 | $-1416.13 | -4.8% | $-416.13 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2937 | 50.6 | 50.9 | $-1554.14 | -5.3% | $-554.14 | -2.9 | done | losing for real |
| trend_filter | 2080 | 48.7 | 50.5 | $-1782.39 | -8.6% | $-782.39 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3502 | 49.1 | 50.2 | $-2197.46 | -6.3% | $-1197.46 | -3.8 | done | losing for real |
| coinflip | 5028 | 49.9 | 50.0 | $-2340.68 | -4.7% | $-1340.68 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5028 | 50.3 | 51.4 | $-2992.34 | -6.0% | $-1992.34 | -4.3 | done | losing for real |
| always_up | 5028 | 47.8 | 49.3 | $-3676.97 | -7.3% | $-2676.97 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8493 | 47.9 | 48.8 | $-5094.49 |
| ETH | 9154 | 48.2 | 48.2 | $-4882.54 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
