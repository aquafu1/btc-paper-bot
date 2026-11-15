# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 4:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 467 windows, 12831 settled trades, 30 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 237 | 35.0 | 35.9 | $-136.40 | -5.8% | $863.60 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1085 | 50.8 | 49.9 | $-272.41 | -2.5% | $727.59 | -0.8 | done | can't tell from luck |
| value_ev10 | 607 | 39.0 | 40.1 | $-363.06 | -6.0% | $636.94 | -1.2 | done | can't tell from luck |
| trend_filter | 742 | 49.6 | 50.7 | $-454.19 | -6.1% | $545.81 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1294 | 49.9 | 50.0 | $-478.91 | -3.7% | $521.09 | -1.3 | done | can't tell from luck |
| value_ev5 | 898 | 41.0 | 41.8 | $-495.95 | -5.5% | $504.05 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1294 | 50.1 | 51.6 | $-936.27 | -7.2% | $63.73 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1085 | 49.2 | 51.8 | $-1007.74 | -9.3% | $-7.74 | -3.2 | done | losing for real |
| coinflip | 1863 | 49.8 | 50.8 | $-1053.63 | -5.7% | $-53.63 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 1863 | 49.8 | 51.6 | $-1326.35 | -7.1% | $-326.35 | -3.2 | done | losing for real |
| always_up | 1863 | 46.4 | 50.4 | $-2140.72 | -11.5% | $-1140.72 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2902 | 47.6 | 49.2 | $-2236.21 |
| ETH | 3222 | 48.0 | 48.8 | $-2119.49 |
| SOL | 3335 | 47.7 | 49.3 | $-2564.97 |
| XRP | 3372 | 48.5 | 49.1 | $-1744.96 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
