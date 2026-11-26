# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 10:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1499 windows, 37422 settled trades, 389 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 759 | 34.3 | 35.4 | $-593.02 | -7.8% | $406.98 | -1.6 | done | can't tell from luck |
| value_ev10 | 1824 | 38.4 | 39.2 | $-1014.96 | -5.6% | $-14.96 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3722 | 50.8 | 50.1 | $-1068.57 | -2.9% | $-68.57 | -1.7 | done | can't tell from luck |
| value_ev5 | 2754 | 40.5 | 41.1 | $-1402.83 | -5.1% | $-402.83 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3129 | 51.1 | 51.0 | $-1437.96 | -4.6% | $-437.96 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3129 | 48.9 | 49.2 | $-1697.92 | -5.4% | $-697.92 | -3.0 | done | losing for real |
| trend_filter | 2219 | 48.6 | 50.3 | $-1909.82 | -8.6% | $-909.82 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3722 | 49.2 | 50.2 | $-2209.83 | -5.9% | $-1209.83 | -3.6 | done | losing for real |
| coinflip | 5388 | 50.0 | 50.0 | $-2357.20 | -4.4% | $-1357.20 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5388 | 50.2 | 51.3 | $-3296.84 | -6.1% | $-2296.84 | -4.6 | done | losing for real |
| always_up | 5388 | 48.0 | 49.2 | $-3599.11 | -6.7% | $-2599.11 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9691 | 48.0 | 48.7 | $-5363.05 |
| ETH | 10421 | 48.0 | 47.9 | $-5640.79 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
