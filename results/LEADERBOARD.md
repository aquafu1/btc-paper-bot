# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 9:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1253 windows, 33966 settled trades, 400 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 665 | 34.1 | 35.3 | $-524.16 | -7.9% | $475.84 | -1.6 | done | can't tell from luck |
| value_ev10 | 1627 | 38.4 | 39.2 | $-910.17 | -5.6% | $89.83 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3405 | 50.7 | 50.3 | $-1162.03 | -3.4% | $-162.03 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 2849 | 49.6 | 49.4 | $-1262.64 | -4.4% | $-262.64 | -2.4 | done | losing for real |
| value_ev5 | 2460 | 40.3 | 41.1 | $-1359.62 | -5.5% | $-359.62 | -2.3 | done | losing for real |
| trend_filter | 2012 | 48.9 | 50.4 | $-1640.78 | -8.2% | $-640.78 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2849 | 50.4 | 51.1 | $-1733.74 | -6.1% | $-733.74 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3405 | 49.3 | 50.2 | $-2060.70 | -6.1% | $-1060.70 | -3.6 | done | losing for real |
| coinflip | 4898 | 50.0 | 50.1 | $-2218.98 | -4.5% | $-1218.98 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4898 | 50.4 | 51.4 | $-2868.39 | -5.9% | $-1868.39 | -4.2 | done | losing for real |
| always_up | 4898 | 47.8 | 49.4 | $-3687.12 | -7.5% | $-2687.12 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8010 | 48.0 | 48.9 | $-4765.95 |
| ETH | 8646 | 48.1 | 48.3 | $-5078.15 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
