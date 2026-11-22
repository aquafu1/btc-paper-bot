# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 8:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1106 windows, 30593 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 583 | 34.3 | 35.1 | $-381.49 | -6.5% | $618.51 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 3084 | 51.2 | 50.4 | $-821.43 | -2.7% | $178.57 | -1.5 | done | can't tell from luck |
| value_ev10 | 1427 | 37.8 | 39.1 | $-951.09 | -6.7% | $48.91 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2598 | 49.8 | 49.4 | $-1061.73 | -4.1% | $-61.73 | -2.1 | done | losing for real |
| trend_filter | 1809 | 49.3 | 50.4 | $-1335.44 | -7.4% | $-335.44 | -3.2 | done | losing for real |
| value_ev5 | 2162 | 39.8 | 41.0 | $-1337.31 | -6.2% | $-337.31 | -2.4 | done | losing for real |
| coinflip | 4416 | 50.5 | 50.2 | $-1704.84 | -3.9% | $-704.84 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2598 | 50.2 | 51.1 | $-1710.29 | -6.6% | $-710.29 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3084 | 48.8 | 50.2 | $-2082.84 | -6.8% | $-1082.84 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4416 | 50.7 | 51.4 | $-2339.26 | -5.3% | $-1339.26 | -3.6 | done | losing for real |
| always_up | 4416 | 47.5 | 49.3 | $-3567.11 | -8.1% | $-2567.11 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7005 | 48.4 | 49.0 | $-3503.57 |
| ETH | 7575 | 48.1 | 48.4 | $-4561.73 |
| SOL | 7964 | 48.1 | 48.4 | $-4483.34 |
| XRP | 8049 | 48.2 | 48.2 | $-4744.18 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
