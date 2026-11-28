# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 28, 4:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1665 windows, 39542 settled trades, 348 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 844 | 34.4 | 35.2 | $-634.92 | -7.5% | $365.08 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3883 | 50.8 | 49.9 | $-988.74 | -2.5% | $11.26 | -1.6 | done | can't tell from luck |
| value_ev10 | 1994 | 38.3 | 39.0 | $-1140.05 | -5.7% | $-140.05 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3244 | 51.1 | 50.9 | $-1434.75 | -4.4% | $-434.75 | -2.6 | done | losing for real |
| value_ev5 | 2977 | 40.3 | 41.0 | $-1635.89 | -5.5% | $-635.89 | -2.5 | done | losing for real |
| momentum_60m_0.30pct | 3244 | 48.9 | 49.3 | $-1824.73 | -5.6% | $-824.73 | -3.2 | done | losing for real |
| trend_filter | 2313 | 48.3 | 50.3 | $-2144.17 | -9.3% | $-1144.17 | -4.6 | done | losing for real |
| momentum_15m_0.10pct | 3883 | 49.2 | 50.2 | $-2394.50 | -6.2% | $-1394.50 | -3.9 | done | losing for real |
| coinflip | 5720 | 49.9 | 49.9 | $-2523.96 | -4.4% | $-1523.96 | -3.3 | done | losing for real |
| always_up | 5720 | 48.3 | 49.0 | $-3517.53 | -6.1% | $-2517.53 | -4.6 | done | losing for real |
| momentum_5m_0.00pct | 5720 | 50.2 | 51.3 | $-3567.39 | -6.2% | $-2567.39 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10668 | 47.9 | 48.5 | $-6033.55 |
| ETH | 11564 | 47.8 | 47.6 | $-6188.85 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
