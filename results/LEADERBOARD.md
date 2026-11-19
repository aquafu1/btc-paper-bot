# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 5:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 855 windows, 23594 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 443 | 34.3 | 34.8 | $-255.60 | -5.8% | $744.40 | -0.9 | done | can't tell from luck |
| value_ev10 | 1080 | 37.7 | 39.0 | $-751.99 | -7.0% | $248.01 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2000 | 50.2 | 49.7 | $-778.01 | -3.9% | $221.99 | -1.7 | done | can't tell from luck |
| trend_filter | 1389 | 50.2 | 50.9 | $-891.07 | -6.4% | $108.93 | -2.5 | done | losing for real |
| reversal_15m_0.10pct | 2408 | 50.6 | 50.5 | $-979.17 | -4.1% | $20.83 | -2.0 | done | losing for real |
| value_ev5 | 1630 | 39.8 | 41.0 | $-1071.69 | -6.6% | $-71.69 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2408 | 49.4 | 50.3 | $-1397.74 | -5.8% | $-397.74 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2000 | 49.8 | 51.1 | $-1497.53 | -7.5% | $-497.53 | -3.4 | done | losing for real |
| coinflip | 3412 | 50.2 | 50.3 | $-1504.93 | -4.4% | $-504.93 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3412 | 51.3 | 51.7 | $-1558.35 | -4.6% | $-558.35 | -2.8 | done | losing for real |
| always_up | 3412 | 46.9 | 49.5 | $-3304.94 | -9.7% | $-2304.94 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5376 | 48.3 | 49.0 | $-3001.54 |
| ETH | 5878 | 48.0 | 48.5 | $-3900.50 |
| SOL | 6152 | 48.2 | 48.5 | $-3638.74 |
| XRP | 6188 | 48.4 | 48.5 | $-3450.26 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
