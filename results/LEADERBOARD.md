# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 10:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1257 windows, 34003 settled trades, 418 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 665 | 34.1 | 35.3 | $-524.16 | -7.9% | $475.84 | -1.6 | done | can't tell from luck |
| value_ev10 | 1628 | 38.4 | 39.2 | $-920.17 | -5.7% | $79.83 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3409 | 50.7 | 50.3 | $-1137.75 | -3.3% | $-137.75 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2853 | 49.6 | 49.4 | $-1282.64 | -4.5% | $-282.64 | -2.4 | done | losing for real |
| value_ev5 | 2461 | 40.3 | 41.1 | $-1369.62 | -5.6% | $-369.62 | -2.3 | done | losing for real |
| trend_filter | 2013 | 48.9 | 50.4 | $-1650.78 | -8.2% | $-650.78 | -3.8 | done | losing for real |
| reversal_60m_0.30pct | 2853 | 50.4 | 51.1 | $-1711.69 | -6.0% | $-711.69 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3409 | 49.3 | 50.2 | $-2082.93 | -6.1% | $-1082.93 | -3.6 | done | losing for real |
| coinflip | 4904 | 50.1 | 50.1 | $-2200.94 | -4.5% | $-1200.94 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4904 | 50.4 | 51.4 | $-2889.45 | -5.9% | $-1889.45 | -4.3 | done | losing for real |
| always_up | 4904 | 47.8 | 49.4 | $-3652.20 | -7.4% | $-2652.20 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8028 | 48.0 | 48.9 | $-4747.74 |
| ETH | 8665 | 48.1 | 48.3 | $-5090.36 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
