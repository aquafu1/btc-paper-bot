# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 7:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 623 windows, 17224 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1458 | 51.4 | 49.6 | $-97.87 | -0.7% | $902.13 | -0.3 | done | can't tell from luck |
| value_ev20 | 329 | 34.0 | 35.3 | $-264.70 | -8.0% | $735.30 | -1.1 | done | can't tell from luck |
| trend_filter | 997 | 50.5 | 50.9 | $-501.18 | -5.0% | $498.82 | -1.6 | done | can't tell from luck |
| value_ev10 | 797 | 38.3 | 39.5 | $-574.18 | -7.2% | $425.82 | -1.7 | done | can't tell from luck |
| value_ev5 | 1203 | 40.5 | 41.4 | $-732.82 | -6.1% | $267.18 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1762 | 50.6 | 51.0 | $-881.05 | -5.0% | $118.95 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 1762 | 49.4 | 50.0 | $-894.04 | -5.1% | $105.96 | -2.1 | done | losing for real |
| coinflip | 2486 | 50.0 | 50.5 | $-1219.27 | -4.9% | $-219.27 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1458 | 48.6 | 51.4 | $-1461.76 | -10.0% | $-461.76 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 2486 | 50.4 | 51.7 | $-1518.98 | -6.1% | $-518.98 | -3.2 | done | losing for real |
| always_up | 2486 | 47.5 | 49.7 | $-2112.16 | -8.5% | $-1112.16 | -4.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3915 | 48.2 | 49.2 | $-2446.83 |
| ETH | 4315 | 48.1 | 48.6 | $-2643.17 |
| SOL | 4470 | 48.0 | 48.8 | $-2931.56 |
| XRP | 4524 | 48.5 | 48.6 | $-2236.45 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
