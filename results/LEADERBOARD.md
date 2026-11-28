# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 9:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1636 windows, 39188 settled trades, 375 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 833 | 34.5 | 35.2 | $-601.28 | -7.2% | $398.72 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3858 | 50.8 | 49.9 | $-1037.63 | -2.7% | $-37.63 | -1.7 | done | can't tell from luck |
| value_ev10 | 1967 | 38.4 | 39.0 | $-1085.62 | -5.5% | $-85.62 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 3226 | 51.0 | 50.9 | $-1502.37 | -4.7% | $-502.37 | -2.7 | done | losing for real |
| value_ev5 | 2938 | 40.4 | 41.0 | $-1528.16 | -5.2% | $-528.16 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 3226 | 49.0 | 49.2 | $-1741.86 | -5.4% | $-741.86 | -3.1 | done | losing for real |
| trend_filter | 2296 | 48.5 | 50.4 | $-2039.36 | -8.9% | $-1039.36 | -4.4 | done | losing for real |
| momentum_15m_0.10pct | 3858 | 49.2 | 50.2 | $-2348.33 | -6.1% | $-1348.33 | -3.8 | done | losing for real |
| coinflip | 5662 | 50.0 | 49.9 | $-2437.47 | -4.3% | $-1437.47 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5662 | 50.2 | 51.3 | $-3497.82 | -6.2% | $-2497.82 | -4.8 | done | losing for real |
| always_up | 5662 | 48.2 | 49.1 | $-3548.63 | -6.3% | $-2548.63 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10500 | 48.0 | 48.6 | $-5857.42 |
| ETH | 11378 | 47.9 | 47.6 | $-5926.88 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
