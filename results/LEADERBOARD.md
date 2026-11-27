# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 8:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1537 windows, 37905 settled trades, 388 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 776 | 34.3 | 35.4 | $-616.25 | -7.9% | $383.75 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3760 | 50.9 | 50.0 | $-966.82 | -2.6% | $33.18 | -1.6 | done | can't tell from luck |
| value_ev10 | 1859 | 38.5 | 39.2 | $-1017.26 | -5.5% | $-17.26 | -1.9 | done | can't tell from luck |
| value_ev5 | 2802 | 40.5 | 41.1 | $-1421.63 | -5.1% | $-421.63 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3156 | 51.0 | 51.0 | $-1474.18 | -4.7% | $-474.18 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3156 | 49.0 | 49.2 | $-1695.26 | -5.4% | $-695.26 | -3.0 | done | losing for real |
| trend_filter | 2244 | 48.6 | 50.3 | $-1931.36 | -8.6% | $-931.36 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3760 | 49.1 | 50.2 | $-2355.46 | -6.3% | $-1355.46 | -3.9 | done | losing for real |
| coinflip | 5464 | 49.9 | 50.0 | $-2445.21 | -4.5% | $-1445.21 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5464 | 50.1 | 51.3 | $-3408.33 | -6.2% | $-2408.33 | -4.7 | done | losing for real |
| always_up | 5464 | 48.1 | 49.2 | $-3570.97 | -6.5% | $-2570.97 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9916 | 47.9 | 48.7 | $-5735.78 |
| ETH | 10679 | 48.1 | 47.9 | $-5582.72 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
