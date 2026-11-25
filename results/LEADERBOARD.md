# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 11:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1404 windows, 36168 settled trades, 381 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 726 | 34.8 | 35.3 | $-452.49 | -6.2% | $547.51 | -1.3 | done | can't tell from luck |
| value_ev10 | 1753 | 39.0 | 39.2 | $-724.58 | -4.1% | $275.42 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 3615 | 50.8 | 50.1 | $-1040.37 | -2.9% | $-40.37 | -1.7 | done | can't tell from luck |
| value_ev5 | 2643 | 40.7 | 41.1 | $-1203.44 | -4.6% | $-203.44 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 3034 | 49.3 | 49.3 | $-1458.07 | -4.8% | $-458.07 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 3034 | 50.7 | 51.0 | $-1567.76 | -5.2% | $-567.76 | -2.9 | done | losing for real |
| trend_filter | 2148 | 48.5 | 50.4 | $-1895.87 | -8.8% | $-895.87 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3615 | 49.2 | 50.2 | $-2196.95 | -6.1% | $-1196.95 | -3.7 | done | losing for real |
| coinflip | 5200 | 50.0 | 50.0 | $-2267.36 | -4.4% | $-1267.36 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5200 | 50.1 | 51.3 | $-3250.21 | -6.3% | $-2250.21 | -4.6 | done | losing for real |
| always_up | 5200 | 47.9 | 49.3 | $-3646.19 | -7.0% | $-2646.19 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9082 | 48.1 | 48.8 | $-4843.37 |
| ETH | 9776 | 48.0 | 48.0 | $-5275.68 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
