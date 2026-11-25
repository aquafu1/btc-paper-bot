# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 1:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1364 windows, 35571 settled trades, 403 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 704 | 34.1 | 35.4 | $-572.68 | -8.1% | $427.32 | -1.7 | done | can't tell from luck |
| value_ev10 | 1721 | 38.6 | 39.2 | $-849.34 | -4.9% | $150.66 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3556 | 50.9 | 50.1 | $-956.27 | -2.7% | $43.73 | -1.6 | done | can't tell from luck |
| value_ev5 | 2596 | 40.4 | 41.1 | $-1351.33 | -5.2% | $-351.33 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2984 | 49.3 | 49.4 | $-1462.31 | -4.9% | $-462.31 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2984 | 50.7 | 50.9 | $-1549.88 | -5.2% | $-549.88 | -2.9 | done | losing for real |
| trend_filter | 2116 | 48.6 | 50.4 | $-1860.35 | -8.8% | $-860.35 | -4.1 | done | losing for real |
| coinflip | 5118 | 50.0 | 50.0 | $-2245.91 | -4.4% | $-1245.91 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3556 | 49.1 | 50.2 | $-2269.41 | -6.4% | $-1269.41 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5118 | 50.1 | 51.3 | $-3196.14 | -6.2% | $-2196.14 | -4.6 | done | losing for real |
| always_up | 5118 | 47.8 | 49.3 | $-3751.45 | -7.3% | $-2751.45 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8791 | 47.8 | 48.8 | $-5338.45 |
| ETH | 9470 | 48.1 | 48.1 | $-5142.39 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
