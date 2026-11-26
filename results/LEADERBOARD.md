# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 12:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1506 windows, 37501 settled trades, 385 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 762 | 34.4 | 35.4 | $-577.73 | -7.6% | $422.27 | -1.6 | done | can't tell from luck |
| value_ev10 | 1830 | 38.5 | 39.2 | $-982.40 | -5.4% | $17.60 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3731 | 50.9 | 50.1 | $-988.85 | -2.7% | $11.15 | -1.6 | done | can't tell from luck |
| value_ev5 | 2761 | 40.5 | 41.1 | $-1380.27 | -5.0% | $-380.27 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3130 | 51.1 | 51.0 | $-1434.35 | -4.6% | $-434.35 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3130 | 48.9 | 49.2 | $-1707.92 | -5.5% | $-707.92 | -3.0 | done | losing for real |
| trend_filter | 2220 | 48.6 | 50.3 | $-1899.92 | -8.6% | $-899.92 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3731 | 49.1 | 50.2 | $-2279.93 | -6.1% | $-1279.93 | -3.8 | done | losing for real |
| coinflip | 5402 | 50.0 | 50.0 | $-2335.59 | -4.3% | $-1335.59 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5402 | 50.2 | 51.3 | $-3293.26 | -6.1% | $-2293.26 | -4.6 | done | losing for real |
| always_up | 5402 | 48.0 | 49.2 | $-3597.55 | -6.7% | $-2597.55 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9726 | 48.0 | 48.7 | $-5347.81 |
| ETH | 10465 | 48.0 | 47.9 | $-5545.74 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
