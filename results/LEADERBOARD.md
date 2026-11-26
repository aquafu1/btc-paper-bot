# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 10:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1448 windows, 36758 settled trades, 383 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 742 | 34.4 | 35.3 | $-553.47 | -7.5% | $446.53 | -1.6 | done | can't tell from luck |
| value_ev10 | 1790 | 38.7 | 39.2 | $-846.32 | -4.7% | $153.68 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3668 | 50.9 | 50.0 | $-970.09 | -2.6% | $29.91 | -1.6 | done | can't tell from luck |
| value_ev5 | 2696 | 40.5 | 41.1 | $-1331.66 | -4.9% | $-331.66 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 3078 | 49.2 | 49.3 | $-1511.81 | -4.9% | $-511.81 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3078 | 50.8 | 51.0 | $-1592.86 | -5.2% | $-592.86 | -2.9 | done | losing for real |
| trend_filter | 2180 | 48.6 | 50.3 | $-1889.45 | -8.7% | $-889.45 | -4.1 | done | losing for real |
| coinflip | 5286 | 50.0 | 50.0 | $-2259.51 | -4.3% | $-1259.51 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3668 | 49.1 | 50.2 | $-2300.84 | -6.3% | $-1300.84 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5286 | 50.1 | 51.3 | $-3339.39 | -6.3% | $-2339.39 | -4.7 | done | losing for real |
| always_up | 5286 | 48.0 | 49.2 | $-3593.99 | -6.8% | $-2593.99 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9377 | 48.1 | 48.7 | $-5019.61 |
| ETH | 10071 | 48.0 | 48.0 | $-5585.55 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
