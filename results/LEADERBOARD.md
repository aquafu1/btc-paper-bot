# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 3:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1087 windows, 30062 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 565 | 34.7 | 35.2 | $-301.63 | -5.3% | $698.37 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 3037 | 51.2 | 50.5 | $-811.80 | -2.7% | $188.20 | -1.5 | done | can't tell from luck |
| value_ev10 | 1392 | 37.9 | 39.2 | $-887.02 | -6.4% | $112.98 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2555 | 49.8 | 49.5 | $-1034.72 | -4.0% | $-34.72 | -2.0 | done | losing for real |
| trend_filter | 1786 | 49.6 | 50.6 | $-1245.66 | -7.0% | $-245.66 | -3.0 | done | losing for real |
| value_ev5 | 2115 | 39.9 | 41.1 | $-1263.15 | -6.0% | $-263.15 | -2.3 | done | losing for real |
| coinflip | 4340 | 50.6 | 50.3 | $-1613.25 | -3.7% | $-613.25 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2555 | 50.2 | 51.1 | $-1696.50 | -6.6% | $-696.50 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3037 | 48.8 | 50.3 | $-2057.95 | -6.8% | $-1057.95 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4340 | 50.9 | 51.5 | $-2106.83 | -4.9% | $-1106.83 | -3.3 | done | losing for real |
| always_up | 4340 | 47.5 | 49.4 | $-3535.73 | -8.1% | $-2535.73 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6862 | 48.5 | 49.0 | $-3307.78 |
| ETH | 7446 | 48.2 | 48.5 | $-4403.35 |
| SOL | 7838 | 48.1 | 48.5 | $-4416.25 |
| XRP | 7916 | 48.3 | 48.3 | $-4426.86 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
