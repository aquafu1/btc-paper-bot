# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 10:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1499 windows, 37429 settled trades, 382 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 759 | 34.3 | 35.4 | $-593.02 | -7.8% | $406.98 | -1.6 | done | can't tell from luck |
| value_ev10 | 1825 | 38.4 | 39.2 | $-1000.82 | -5.5% | $-0.82 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3723 | 50.8 | 50.1 | $-1054.43 | -2.8% | $-54.43 | -1.7 | done | can't tell from luck |
| value_ev5 | 2755 | 40.5 | 41.1 | $-1388.69 | -5.0% | $-388.69 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3129 | 51.1 | 51.0 | $-1437.96 | -4.6% | $-437.96 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3129 | 48.9 | 49.2 | $-1697.92 | -5.4% | $-697.92 | -3.0 | done | losing for real |
| trend_filter | 2219 | 48.6 | 50.3 | $-1909.82 | -8.6% | $-909.82 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3723 | 49.2 | 50.2 | $-2219.83 | -6.0% | $-1219.83 | -3.7 | done | losing for real |
| coinflip | 5389 | 50.0 | 50.0 | $-2367.20 | -4.4% | $-1367.20 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5389 | 50.2 | 51.3 | $-3306.84 | -6.1% | $-2306.84 | -4.6 | done | losing for real |
| always_up | 5389 | 48.0 | 49.2 | $-3584.97 | -6.7% | $-2584.97 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9691 | 48.0 | 48.7 | $-5363.05 |
| ETH | 10428 | 48.0 | 47.9 | $-5614.22 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
