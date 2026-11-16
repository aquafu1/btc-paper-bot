# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 1:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 500 windows, 13766 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 255 | 33.7 | 35.5 | $-229.21 | -9.0% | $770.79 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1170 | 51.1 | 49.9 | $-233.08 | -2.0% | $766.92 | -0.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1391 | 49.9 | 49.7 | $-536.26 | -3.9% | $463.74 | -1.4 | done | can't tell from luck |
| trend_filter | 809 | 49.7 | 50.8 | $-547.73 | -6.8% | $452.27 | -2.0 | done | can't tell from luck |
| value_ev10 | 647 | 37.9 | 39.8 | $-550.56 | -8.5% | $449.44 | -1.8 | done | can't tell from luck |
| value_ev5 | 957 | 40.1 | 41.6 | $-693.93 | -7.3% | $306.07 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1391 | 50.1 | 51.6 | $-993.77 | -7.1% | $6.23 | -2.7 | done | losing for real |
| coinflip | 1992 | 50.1 | 50.7 | $-1047.81 | -5.3% | $-47.81 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1170 | 48.9 | 51.3 | $-1074.88 | -9.2% | $-74.88 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1992 | 49.7 | 51.6 | $-1486.17 | -7.5% | $-486.17 | -3.5 | done | losing for real |
| always_up | 1992 | 46.2 | 50.2 | $-2402.14 | -12.1% | $-1402.14 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3105 | 47.3 | 49.2 | $-2574.62 |
| ETH | 3445 | 48.0 | 48.7 | $-2320.82 |
| SOL | 3590 | 47.7 | 49.1 | $-2725.49 |
| XRP | 3626 | 48.3 | 48.8 | $-2174.61 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
