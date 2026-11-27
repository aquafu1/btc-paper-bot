# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 8:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1539 windows, 37934 settled trades, 404 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 778 | 34.2 | 35.3 | $-636.25 | -8.2% | $363.75 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3763 | 50.9 | 50.0 | $-996.82 | -2.6% | $3.18 | -1.6 | done | can't tell from luck |
| value_ev10 | 1861 | 38.4 | 39.2 | $-1037.26 | -5.6% | $-37.26 | -2.0 | done | can't tell from luck |
| value_ev5 | 2805 | 40.5 | 41.1 | $-1430.91 | -5.1% | $-430.91 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3158 | 51.0 | 51.0 | $-1494.18 | -4.7% | $-494.18 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3158 | 49.0 | 49.2 | $-1674.24 | -5.3% | $-674.24 | -3.0 | done | losing for real |
| trend_filter | 2244 | 48.6 | 50.3 | $-1931.36 | -8.6% | $-931.36 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3763 | 49.1 | 50.2 | $-2329.57 | -6.2% | $-1329.57 | -3.8 | done | losing for real |
| coinflip | 5468 | 49.9 | 50.0 | $-2431.51 | -4.4% | $-1431.51 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5468 | 50.1 | 51.3 | $-3420.78 | -6.3% | $-2420.78 | -4.8 | done | losing for real |
| always_up | 5468 | 48.1 | 49.2 | $-3542.39 | -6.5% | $-2542.39 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9929 | 47.9 | 48.7 | $-5746.57 |
| ETH | 10695 | 48.1 | 47.9 | $-5594.47 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
