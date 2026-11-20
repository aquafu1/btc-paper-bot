# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 2:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 891 windows, 24600 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 462 | 35.7 | 34.9 | $-81.30 | -1.8% | $918.70 | -0.3 | done | can't tell from luck |
| value_ev10 | 1128 | 38.3 | 39.1 | $-589.52 | -5.2% | $410.48 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 2077 | 49.9 | 49.8 | $-948.30 | -4.6% | $51.70 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2513 | 50.6 | 50.4 | $-966.12 | -3.8% | $33.88 | -1.9 | done | can't tell from luck |
| value_ev5 | 1707 | 40.0 | 41.0 | $-984.05 | -5.8% | $15.95 | -2.0 | done | losing for real |
| trend_filter | 1449 | 49.9 | 51.0 | $-1011.24 | -7.0% | $-11.24 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2077 | 50.1 | 50.9 | $-1330.79 | -6.4% | $-330.79 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2513 | 49.4 | 50.4 | $-1417.39 | -5.6% | $-417.39 | -2.8 | done | losing for real |
| coinflip | 3558 | 50.3 | 50.3 | $-1513.39 | -4.3% | $-513.39 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3558 | 51.2 | 51.7 | $-1672.37 | -4.7% | $-672.37 | -2.9 | done | losing for real |
| always_up | 3558 | 47.0 | 49.6 | $-3432.32 | -9.6% | $-2432.32 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5611 | 48.3 | 49.1 | $-3007.81 |
| ETH | 6119 | 48.2 | 48.5 | $-3713.93 |
| SOL | 6418 | 48.2 | 48.5 | $-3650.02 |
| XRP | 6452 | 48.3 | 48.5 | $-3575.03 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
