# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 8:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1345 windows, 35305 settled trades, 418 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 695 | 34.2 | 35.4 | $-538.07 | -7.7% | $461.93 | -1.6 | done | can't tell from luck |
| value_ev10 | 1701 | 38.8 | 39.2 | $-794.05 | -4.7% | $205.95 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3534 | 50.8 | 50.1 | $-1019.40 | -2.9% | $-19.40 | -1.7 | done | can't tell from luck |
| value_ev5 | 2569 | 40.5 | 41.1 | $-1301.12 | -5.1% | $-301.12 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2966 | 49.4 | 49.4 | $-1450.62 | -4.9% | $-450.62 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2966 | 50.6 | 50.9 | $-1553.36 | -5.2% | $-553.36 | -2.9 | done | losing for real |
| trend_filter | 2100 | 48.7 | 50.5 | $-1798.96 | -8.6% | $-798.96 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3534 | 49.2 | 50.3 | $-2217.48 | -6.3% | $-1217.48 | -3.8 | done | losing for real |
| coinflip | 5080 | 50.0 | 50.1 | $-2297.32 | -4.5% | $-1297.32 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5080 | 50.3 | 51.4 | $-3045.65 | -6.0% | $-2045.65 | -4.4 | done | losing for real |
| always_up | 5080 | 47.9 | 49.3 | $-3708.02 | -7.3% | $-2708.02 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8659 | 47.9 | 48.9 | $-5246.19 |
| ETH | 9336 | 48.2 | 48.2 | $-4893.63 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
