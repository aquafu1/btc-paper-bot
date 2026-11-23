# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 2:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1227 windows, 33562 settled trades, 433 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 655 | 34.4 | 35.3 | $-473.45 | -7.2% | $526.55 | -1.4 | done | can't tell from luck |
| value_ev10 | 1605 | 38.7 | 39.2 | $-796.99 | -5.0% | $203.01 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3365 | 50.8 | 50.3 | $-1084.39 | -3.2% | $-84.39 | -1.9 | done | can't tell from luck |
| value_ev5 | 2425 | 40.5 | 41.1 | $-1232.22 | -5.1% | $-232.22 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2816 | 49.5 | 49.4 | $-1270.34 | -4.5% | $-270.34 | -2.4 | done | losing for real |
| trend_filter | 1983 | 48.8 | 50.5 | $-1670.71 | -8.4% | $-670.71 | -3.8 | done | losing for real |
| reversal_60m_0.30pct | 2816 | 50.5 | 51.1 | $-1681.99 | -6.0% | $-681.99 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3365 | 49.2 | 50.2 | $-2083.87 | -6.2% | $-1083.87 | -3.6 | done | losing for real |
| coinflip | 4844 | 50.0 | 50.1 | $-2229.47 | -4.6% | $-1229.47 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4844 | 50.2 | 51.4 | $-2950.70 | -6.1% | $-1950.70 | -4.4 | done | losing for real |
| always_up | 4844 | 47.9 | 49.3 | $-3549.81 | -7.3% | $-2549.81 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7817 | 48.1 | 48.9 | $-4444.58 |
| ETH | 8435 | 48.1 | 48.3 | $-4995.13 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
