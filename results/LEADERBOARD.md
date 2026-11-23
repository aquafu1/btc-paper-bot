# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 12:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1170 windows, 32342 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 623 | 35.0 | 35.3 | $-341.04 | -5.5% | $658.96 | -1.0 | done | can't tell from luck |
| value_ev10 | 1530 | 38.6 | 39.2 | $-792.45 | -5.2% | $207.55 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3242 | 50.8 | 50.4 | $-1069.84 | -3.3% | $-69.84 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2729 | 49.7 | 49.4 | $-1142.85 | -4.2% | $-142.85 | -2.2 | done | losing for real |
| value_ev5 | 2315 | 40.3 | 41.1 | $-1218.93 | -5.3% | $-218.93 | -2.1 | done | losing for real |
| trend_filter | 1916 | 49.1 | 50.5 | $-1489.13 | -7.8% | $-489.13 | -3.5 | done | losing for real |
| reversal_60m_0.30pct | 2729 | 50.3 | 51.1 | $-1723.19 | -6.3% | $-723.19 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3242 | 49.2 | 50.2 | $-1940.92 | -6.0% | $-940.92 | -3.4 | done | losing for real |
| coinflip | 4672 | 50.1 | 50.2 | $-2049.95 | -4.4% | $-1049.95 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 4672 | 50.2 | 51.4 | $-2832.66 | -6.1% | $-1832.66 | -4.3 | done | losing for real |
| always_up | 4672 | 47.9 | 49.3 | $-3358.89 | -7.2% | $-2358.89 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7421 | 48.3 | 49.0 | $-3821.02 |
| ETH | 8024 | 48.1 | 48.4 | $-4678.37 |
| SOL | 8412 | 48.1 | 48.4 | $-4453.07 |
| XRP | 8485 | 48.1 | 48.2 | $-5007.39 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
