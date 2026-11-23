# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 2:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1225 windows, 33530 settled trades, 435 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 653 | 34.5 | 35.3 | $-453.45 | -6.9% | $546.55 | -1.4 | done | can't tell from luck |
| value_ev10 | 1602 | 38.8 | 39.2 | $-766.99 | -4.8% | $233.01 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3362 | 50.8 | 50.3 | $-1083.82 | -3.2% | $-83.82 | -1.9 | done | can't tell from luck |
| value_ev5 | 2422 | 40.5 | 41.1 | $-1202.22 | -5.0% | $-202.22 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2813 | 49.5 | 49.4 | $-1290.50 | -4.6% | $-290.50 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2813 | 50.5 | 51.1 | $-1665.47 | -5.9% | $-665.47 | -3.2 | done | losing for real |
| trend_filter | 1983 | 48.8 | 50.5 | $-1670.71 | -8.4% | $-670.71 | -3.8 | done | losing for real |
| momentum_15m_0.10pct | 3362 | 49.2 | 50.2 | $-2080.86 | -6.2% | $-1080.86 | -3.6 | done | losing for real |
| coinflip | 4840 | 50.0 | 50.1 | $-2237.19 | -4.6% | $-1237.19 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4840 | 50.3 | 51.4 | $-2924.18 | -6.0% | $-1924.18 | -4.3 | done | losing for real |
| always_up | 4840 | 47.9 | 49.3 | $-3536.80 | -7.3% | $-2536.80 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7802 | 48.1 | 48.9 | $-4393.98 |
| ETH | 8418 | 48.1 | 48.3 | $-4933.97 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
