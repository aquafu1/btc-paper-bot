# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 8:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1011 windows, 28154 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 519 | 34.1 | 35.0 | $-322.56 | -6.2% | $677.44 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 2427 | 50.2 | 49.7 | $-893.06 | -3.7% | $106.94 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 2871 | 51.0 | 50.5 | $-914.03 | -3.2% | $85.97 | -1.7 | done | can't tell from luck |
| value_ev10 | 1289 | 37.3 | 39.1 | $-982.99 | -7.6% | $17.01 | -2.2 | done | losing for real |
| trend_filter | 1691 | 49.9 | 50.8 | $-1142.60 | -6.8% | $-142.60 | -2.9 | done | losing for real |
| value_ev5 | 1951 | 39.5 | 41.0 | $-1334.73 | -6.8% | $-334.73 | -2.6 | done | losing for real |
| coinflip | 4036 | 50.5 | 50.4 | $-1668.49 | -4.1% | $-668.49 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2427 | 49.8 | 51.0 | $-1788.58 | -7.4% | $-788.58 | -3.7 | done | losing for real |
| momentum_15m_0.10pct | 2871 | 49.0 | 50.3 | $-1893.07 | -6.6% | $-893.07 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4036 | 50.7 | 51.5 | $-2225.33 | -5.5% | $-1225.33 | -3.6 | done | losing for real |
| always_up | 4036 | 47.3 | 49.5 | $-3628.42 | -9.0% | $-2628.42 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6421 | 48.3 | 49.1 | $-3546.45 |
| ETH | 6992 | 48.1 | 48.5 | $-4451.19 |
| SOL | 7358 | 48.2 | 48.6 | $-4146.42 |
| XRP | 7383 | 48.1 | 48.4 | $-4649.81 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
