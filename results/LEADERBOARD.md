# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 2:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1273 windows, 34240 settled trades, 393 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 670 | 34.2 | 35.3 | $-510.36 | -7.6% | $489.64 | -1.5 | done | can't tell from luck |
| value_ev10 | 1644 | 38.6 | 39.2 | $-823.77 | -5.0% | $176.23 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3431 | 50.7 | 50.2 | $-1192.27 | -3.5% | $-192.27 | -2.0 | done | losing for real |
| value_ev5 | 2484 | 40.5 | 41.1 | $-1266.74 | -5.1% | $-266.74 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2872 | 49.5 | 49.4 | $-1318.28 | -4.6% | $-318.28 | -2.5 | done | losing for real |
| trend_filter | 2028 | 49.0 | 50.4 | $-1617.01 | -8.0% | $-617.01 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2872 | 50.5 | 51.0 | $-1660.57 | -5.8% | $-660.57 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3431 | 49.3 | 50.2 | $-2024.89 | -5.9% | $-1024.89 | -3.5 | done | losing for real |
| coinflip | 4936 | 50.0 | 50.1 | $-2263.88 | -4.6% | $-1263.88 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4936 | 50.4 | 51.4 | $-2792.26 | -5.7% | $-1792.26 | -4.1 | done | losing for real |
| always_up | 4936 | 47.9 | 49.4 | $-3611.04 | -7.3% | $-2611.04 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8139 | 48.0 | 48.9 | $-4785.60 |
| ETH | 8791 | 48.2 | 48.3 | $-4711.22 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
