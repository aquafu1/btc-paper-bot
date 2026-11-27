# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 8:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1539 windows, 37944 settled trades, 394 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 778 | 34.2 | 35.3 | $-636.25 | -8.2% | $363.75 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3764 | 50.9 | 50.0 | $-1006.82 | -2.7% | $-6.82 | -1.6 | done | can't tell from luck |
| value_ev10 | 1862 | 38.4 | 39.2 | $-1047.26 | -5.6% | $-47.26 | -2.0 | done | can't tell from luck |
| value_ev5 | 2806 | 40.5 | 41.1 | $-1440.91 | -5.1% | $-440.91 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3159 | 51.0 | 51.0 | $-1504.18 | -4.8% | $-504.18 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3159 | 49.0 | 49.2 | $-1669.17 | -5.3% | $-669.17 | -3.0 | done | losing for real |
| trend_filter | 2245 | 48.6 | 50.3 | $-1926.29 | -8.6% | $-926.29 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3764 | 49.1 | 50.2 | $-2324.50 | -6.2% | $-1324.50 | -3.8 | done | losing for real |
| coinflip | 5469 | 50.0 | 50.0 | $-2426.45 | -4.4% | $-1426.45 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5469 | 50.2 | 51.3 | $-3415.71 | -6.2% | $-2415.71 | -4.8 | done | losing for real |
| always_up | 5469 | 48.1 | 49.2 | $-3537.32 | -6.5% | $-2537.32 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9939 | 47.9 | 48.7 | $-5756.16 |
| ETH | 10695 | 48.1 | 47.9 | $-5594.47 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
