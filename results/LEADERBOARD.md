# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 4:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 898 windows, 24782 settled trades, 37 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 464 | 35.6 | 34.8 | $-101.30 | -2.2% | $898.70 | -0.3 | done | can't tell from luck |
| value_ev10 | 1137 | 38.3 | 39.1 | $-604.14 | -5.3% | $395.86 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2093 | 49.9 | 49.8 | $-961.40 | -4.6% | $38.60 | -2.1 | done | losing for real |
| value_ev5 | 1718 | 39.9 | 41.0 | $-997.05 | -5.8% | $2.95 | -2.0 | done | losing for real |
| trend_filter | 1465 | 50.0 | 51.0 | $-1014.54 | -6.9% | $-14.54 | -2.7 | done | losing for real |
| reversal_15m_0.10pct | 2527 | 50.4 | 50.4 | $-1041.35 | -4.1% | $-41.35 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2527 | 49.6 | 50.4 | $-1351.50 | -5.3% | $-351.50 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2093 | 50.1 | 50.9 | $-1357.05 | -6.5% | $-357.05 | -3.0 | done | losing for real |
| coinflip | 3586 | 50.3 | 50.3 | $-1552.74 | -4.3% | $-552.74 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3586 | 51.3 | 51.7 | $-1619.02 | -4.5% | $-619.02 | -2.8 | done | losing for real |
| always_up | 3586 | 46.9 | 49.6 | $-3498.29 | -9.8% | $-2498.29 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5648 | 48.3 | 49.1 | $-2994.11 |
| ETH | 6166 | 48.3 | 48.5 | $-3715.71 |
| SOL | 6469 | 48.2 | 48.6 | $-3665.17 |
| XRP | 6499 | 48.3 | 48.5 | $-3723.40 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
