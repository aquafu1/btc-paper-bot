# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 3:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1180 windows, 32609 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 633 | 35.1 | 35.3 | $-329.65 | -5.2% | $670.35 | -1.0 | done | can't tell from luck |
| value_ev10 | 1543 | 38.6 | 39.2 | $-767.44 | -5.0% | $232.56 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3269 | 50.8 | 50.4 | $-1064.39 | -3.3% | $-64.39 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2747 | 49.6 | 49.4 | $-1216.81 | -4.4% | $-216.81 | -2.3 | done | losing for real |
| value_ev5 | 2336 | 40.3 | 41.1 | $-1256.14 | -5.4% | $-256.14 | -2.2 | done | losing for real |
| trend_filter | 1929 | 48.9 | 50.5 | $-1572.36 | -8.2% | $-572.36 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2747 | 50.4 | 51.1 | $-1682.32 | -6.1% | $-682.32 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3269 | 49.2 | 50.2 | $-1966.28 | -6.0% | $-966.28 | -3.5 | done | losing for real |
| coinflip | 4712 | 50.0 | 50.2 | $-2163.94 | -4.6% | $-1163.94 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4712 | 50.1 | 51.4 | $-2952.63 | -6.3% | $-1952.63 | -4.4 | done | losing for real |
| always_up | 4712 | 47.8 | 49.3 | $-3425.47 | -7.3% | $-2425.47 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7481 | 48.2 | 48.9 | $-4062.86 |
| ETH | 8088 | 48.1 | 48.4 | $-4824.13 |
| SOL | 8478 | 48.1 | 48.4 | $-4458.18 |
| XRP | 8562 | 48.1 | 48.2 | $-5052.25 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
