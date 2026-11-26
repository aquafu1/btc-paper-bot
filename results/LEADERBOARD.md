# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 9:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1494 windows, 37343 settled trades, 375 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 758 | 34.3 | 35.4 | $-583.02 | -7.7% | $416.98 | -1.6 | done | can't tell from luck |
| value_ev10 | 1821 | 38.4 | 39.2 | $-984.96 | -5.4% | $15.04 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3713 | 50.8 | 50.1 | $-1040.10 | -2.8% | $-40.10 | -1.7 | done | can't tell from luck |
| value_ev5 | 2747 | 40.5 | 41.1 | $-1399.82 | -5.1% | $-399.82 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3120 | 51.0 | 51.0 | $-1507.24 | -4.8% | $-507.24 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 3120 | 49.0 | 49.2 | $-1629.55 | -5.2% | $-629.55 | -2.9 | done | losing for real |
| trend_filter | 2217 | 48.6 | 50.3 | $-1911.44 | -8.6% | $-911.44 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3713 | 49.2 | 50.2 | $-2238.21 | -6.0% | $-1238.21 | -3.7 | done | losing for real |
| coinflip | 5378 | 50.0 | 50.0 | $-2350.04 | -4.4% | $-1350.04 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5378 | 50.1 | 51.3 | $-3357.02 | -6.2% | $-2357.02 | -4.7 | done | losing for real |
| always_up | 5378 | 48.0 | 49.2 | $-3642.07 | -6.8% | $-2642.07 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9654 | 48.0 | 48.7 | $-5351.49 |
| ETH | 10379 | 47.9 | 47.9 | $-5707.74 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
