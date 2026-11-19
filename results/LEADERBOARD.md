# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 2:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 842 windows, 23177 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 425 | 33.2 | 34.9 | $-395.63 | -9.3% | $604.37 | -1.5 | done | can't tell from luck |
| value_ev10 | 1056 | 37.4 | 39.2 | $-854.86 | -8.1% | $145.14 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 1954 | 50.1 | 49.7 | $-855.55 | -4.4% | $144.45 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2367 | 50.8 | 50.6 | $-920.05 | -3.9% | $79.95 | -1.9 | done | can't tell from luck |
| trend_filter | 1364 | 49.9 | 50.8 | $-937.33 | -6.9% | $62.67 | -2.6 | done | losing for real |
| value_ev5 | 1601 | 39.7 | 41.1 | $-1147.40 | -7.2% | $-147.40 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1954 | 49.9 | 51.1 | $-1438.25 | -7.4% | $-438.25 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 2367 | 49.2 | 50.3 | $-1458.16 | -6.2% | $-458.16 | -3.0 | done | losing for real |
| coinflip | 3363 | 50.2 | 50.3 | $-1524.54 | -4.5% | $-524.54 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3363 | 51.2 | 51.6 | $-1581.04 | -4.7% | $-581.04 | -2.8 | done | losing for real |
| always_up | 3363 | 47.0 | 49.6 | $-3210.11 | -9.5% | $-2210.11 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5266 | 48.1 | 49.1 | $-3395.70 |
| ETH | 5773 | 48.0 | 48.5 | $-4053.27 |
| SOL | 6047 | 48.2 | 48.6 | $-3555.04 |
| XRP | 6091 | 48.4 | 48.5 | $-3318.91 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
