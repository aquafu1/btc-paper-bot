# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 9:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 630 windows, 17402 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1468 | 51.2 | 49.5 | $-151.57 | -1.0% | $848.43 | -0.4 | done | can't tell from luck |
| value_ev20 | 330 | 33.9 | 35.3 | $-274.70 | -8.3% | $725.30 | -1.2 | done | can't tell from luck |
| trend_filter | 1006 | 50.1 | 50.8 | $-573.57 | -5.7% | $426.43 | -1.8 | done | can't tell from luck |
| value_ev10 | 804 | 38.3 | 39.5 | $-575.74 | -7.2% | $424.26 | -1.7 | done | can't tell from luck |
| value_ev5 | 1218 | 40.6 | 41.4 | $-714.18 | -5.9% | $285.82 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1786 | 50.8 | 51.1 | $-853.01 | -4.8% | $146.99 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 1786 | 49.2 | 49.9 | $-959.14 | -5.4% | $40.86 | -2.3 | done | losing for real |
| coinflip | 2512 | 50.1 | 50.5 | $-1172.53 | -4.7% | $-172.53 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1468 | 48.8 | 51.4 | $-1419.32 | -9.7% | $-419.32 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2512 | 50.3 | 51.7 | $-1579.89 | -6.3% | $-579.89 | -3.3 | done | losing for real |
| always_up | 2512 | 47.3 | 49.7 | $-2214.60 | -8.8% | $-1214.60 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3949 | 48.2 | 49.2 | $-2481.23 |
| ETH | 4353 | 48.2 | 48.6 | $-2662.10 |
| SOL | 4519 | 47.9 | 48.8 | $-3017.87 |
| XRP | 4581 | 48.4 | 48.5 | $-2327.05 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
