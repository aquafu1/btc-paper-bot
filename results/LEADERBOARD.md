# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 28, 3:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1661 windows, 39508 settled trades, 362 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 842 | 34.3 | 35.2 | $-641.08 | -7.6% | $358.92 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3880 | 50.8 | 49.9 | $-1023.49 | -2.6% | $-23.49 | -1.6 | done | can't tell from luck |
| value_ev10 | 1991 | 38.3 | 39.0 | $-1160.45 | -5.8% | $-160.45 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3244 | 51.1 | 50.9 | $-1434.75 | -4.4% | $-434.75 | -2.6 | done | losing for real |
| value_ev5 | 2973 | 40.2 | 41.0 | $-1673.15 | -5.6% | $-673.15 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3244 | 48.9 | 49.3 | $-1824.73 | -5.6% | $-824.73 | -3.2 | done | losing for real |
| trend_filter | 2312 | 48.3 | 50.3 | $-2134.17 | -9.2% | $-1134.17 | -4.5 | done | losing for real |
| momentum_15m_0.10pct | 3880 | 49.2 | 50.2 | $-2364.50 | -6.1% | $-1364.50 | -3.8 | done | losing for real |
| coinflip | 5714 | 49.9 | 49.9 | $-2522.45 | -4.4% | $-1522.45 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5714 | 50.2 | 51.3 | $-3507.39 | -6.1% | $-2507.39 | -4.8 | done | losing for real |
| always_up | 5714 | 48.3 | 49.0 | $-3542.17 | -6.2% | $-2542.17 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10655 | 47.9 | 48.5 | $-6061.18 |
| ETH | 11543 | 47.9 | 47.6 | $-6182.92 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
