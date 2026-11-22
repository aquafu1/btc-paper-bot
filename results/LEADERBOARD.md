# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 7:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1100 windows, 30442 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 579 | 34.5 | 35.0 | $-341.49 | -5.9% | $658.51 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3073 | 51.1 | 50.5 | $-847.55 | -2.8% | $152.45 | -1.5 | done | can't tell from luck |
| value_ev10 | 1417 | 38.1 | 39.1 | $-851.09 | -6.0% | $148.91 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2587 | 49.6 | 49.4 | $-1150.95 | -4.4% | $-150.95 | -2.3 | done | losing for real |
| value_ev5 | 2148 | 40.0 | 41.0 | $-1220.70 | -5.7% | $-220.70 | -2.2 | done | losing for real |
| trend_filter | 1802 | 49.3 | 50.4 | $-1347.14 | -7.5% | $-347.14 | -3.2 | done | losing for real |
| reversal_60m_0.30pct | 2587 | 50.4 | 51.1 | $-1613.63 | -6.2% | $-613.63 | -3.3 | done | losing for real |
| coinflip | 4392 | 50.5 | 50.2 | $-1647.24 | -3.8% | $-647.24 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 3073 | 48.9 | 50.2 | $-2038.77 | -6.6% | $-1038.77 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4392 | 50.8 | 51.4 | $-2266.10 | -5.2% | $-1266.10 | -3.5 | done | losing for real |
| always_up | 4392 | 47.5 | 49.3 | $-3488.03 | -7.9% | $-2488.03 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6967 | 48.4 | 49.0 | $-3379.79 |
| ETH | 7541 | 48.2 | 48.4 | $-4450.91 |
| SOL | 7924 | 48.1 | 48.4 | $-4382.92 |
| XRP | 8010 | 48.2 | 48.2 | $-4599.07 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
