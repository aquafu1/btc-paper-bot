# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 9:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 868 windows, 23920 settled trades, 76 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 448 | 35.0 | 34.9 | $-178.27 | -4.0% | $821.73 | -0.6 | done | can't tell from luck |
| value_ev10 | 1096 | 38.2 | 39.1 | $-627.29 | -5.7% | $372.71 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2020 | 50.1 | 49.7 | $-775.96 | -3.8% | $224.04 | -1.7 | done | can't tell from luck |
| trend_filter | 1402 | 50.1 | 50.9 | $-902.42 | -6.4% | $97.58 | -2.5 | done | losing for real |
| reversal_15m_0.10pct | 2442 | 50.6 | 50.5 | $-968.81 | -4.0% | $31.19 | -2.0 | done | can't tell from luck |
| value_ev5 | 1658 | 40.0 | 41.0 | $-989.69 | -6.0% | $10.31 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2442 | 49.4 | 50.4 | $-1384.92 | -5.7% | $-384.92 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2020 | 49.9 | 51.1 | $-1462.72 | -7.2% | $-462.72 | -3.3 | done | losing for real |
| coinflip | 3464 | 50.1 | 50.3 | $-1550.12 | -4.5% | $-550.12 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3464 | 51.2 | 51.7 | $-1586.97 | -4.6% | $-586.97 | -2.8 | done | losing for real |
| always_up | 3464 | 46.9 | 49.6 | $-3363.11 | -9.7% | $-2363.11 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5455 | 48.3 | 49.1 | $-2972.76 |
| ETH | 5950 | 48.1 | 48.5 | $-3860.38 |
| SOL | 6242 | 48.3 | 48.6 | $-3503.59 |
| XRP | 6273 | 48.3 | 48.5 | $-3453.54 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
