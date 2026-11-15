# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 9:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 436 windows, 11992 settled trades, 73 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1022 | 51.2 | 49.9 | $-168.16 | -1.6% | $831.84 | -0.5 | done | can't tell from luck |
| value_ev20 | 220 | 34.5 | 36.1 | $-178.23 | -8.1% | $821.77 | -0.9 | done | can't tell from luck |
| trend_filter | 689 | 50.2 | 50.6 | $-320.97 | -4.7% | $679.03 | -1.2 | done | can't tell from luck |
| value_ev10 | 563 | 39.1 | 40.2 | $-363.63 | -6.5% | $636.37 | -1.3 | done | can't tell from luck |
| value_ev5 | 840 | 41.3 | 41.9 | $-449.11 | -5.3% | $550.89 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1214 | 49.8 | 50.0 | $-499.56 | -4.1% | $500.44 | -1.4 | done | can't tell from luck |
| coinflip | 1736 | 50.5 | 50.9 | $-784.95 | -4.5% | $215.05 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1214 | 50.2 | 51.6 | $-848.85 | -7.0% | $151.15 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1022 | 48.8 | 51.8 | $-1017.25 | -10.0% | $-17.25 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 1736 | 49.8 | 51.6 | $-1207.75 | -7.0% | $-207.75 | -3.0 | done | losing for real |
| always_up | 1736 | 45.9 | 50.5 | $-2227.59 | -12.8% | $-1227.59 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2707 | 47.5 | 49.3 | $-2088.30 |
| ETH | 3011 | 48.1 | 48.8 | $-1831.75 |
| SOL | 3113 | 47.8 | 49.3 | $-2403.24 |
| XRP | 3161 | 48.7 | 49.2 | $-1742.74 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
