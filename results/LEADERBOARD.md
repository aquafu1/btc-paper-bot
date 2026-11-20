# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 5:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 950 windows, 26358 settled trades, 31 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 486 | 35.2 | 34.9 | $-144.35 | -3.0% | $855.65 | -0.5 | done | can't tell from luck |
| value_ev10 | 1197 | 38.2 | 39.1 | $-638.29 | -5.3% | $361.71 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 2696 | 51.2 | 50.6 | $-791.86 | -2.9% | $208.14 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2254 | 50.1 | 49.7 | $-873.20 | -3.9% | $126.80 | -1.8 | done | can't tell from luck |
| trend_filter | 1573 | 50.0 | 50.8 | $-1018.86 | -6.5% | $-18.86 | -2.6 | done | losing for real |
| value_ev5 | 1817 | 39.9 | 41.0 | $-1032.07 | -5.7% | $-32.07 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 2254 | 49.9 | 51.0 | $-1619.03 | -7.2% | $-619.03 | -3.5 | done | losing for real |
| coinflip | 3795 | 50.3 | 50.4 | $-1689.30 | -4.5% | $-689.30 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2696 | 48.8 | 50.2 | $-1848.70 | -6.9% | $-848.70 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 3795 | 50.9 | 51.5 | $-1922.07 | -5.1% | $-922.07 | -3.2 | done | losing for real |
| always_up | 3795 | 46.8 | 49.6 | $-3777.55 | -10.0% | $-2777.55 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6005 | 48.2 | 49.0 | $-3414.80 |
| ETH | 6556 | 48.1 | 48.5 | $-4027.95 |
| SOL | 6874 | 48.3 | 48.6 | $-3806.87 |
| XRP | 6923 | 48.2 | 48.5 | $-4105.66 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
