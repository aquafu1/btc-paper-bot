# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 6:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 521 windows, 14355 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 269 | 34.6 | 35.6 | $-184.33 | -6.9% | $815.67 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1223 | 51.2 | 49.9 | $-192.73 | -1.6% | $807.27 | -0.6 | done | can't tell from luck |
| value_ev10 | 670 | 38.1 | 39.7 | $-516.39 | -7.7% | $483.61 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1453 | 49.8 | 49.6 | $-567.40 | -3.9% | $432.60 | -1.5 | done | can't tell from luck |
| trend_filter | 841 | 49.3 | 50.7 | $-587.53 | -7.0% | $412.47 | -2.1 | done | losing for real |
| value_ev5 | 995 | 40.0 | 41.5 | $-721.89 | -7.3% | $278.11 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1453 | 50.2 | 51.6 | $-989.76 | -6.8% | $10.24 | -2.7 | done | losing for real |
| coinflip | 2076 | 50.0 | 50.7 | $-1120.41 | -5.4% | $-120.41 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1223 | 48.8 | 51.4 | $-1137.68 | -9.3% | $-137.68 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 2076 | 49.3 | 51.6 | $-1684.96 | -8.1% | $-684.96 | -3.8 | done | losing for real |
| always_up | 2076 | 46.5 | 50.1 | $-2348.59 | -11.3% | $-1348.59 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3248 | 47.4 | 49.2 | $-2634.69 |
| ETH | 3582 | 47.9 | 48.7 | $-2420.38 |
| SOL | 3742 | 47.6 | 49.0 | $-2780.14 |
| XRP | 3783 | 48.3 | 48.8 | $-2216.46 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
