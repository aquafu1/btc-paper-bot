# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 7:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1391 windows, 35952 settled trades, 396 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 723 | 34.7 | 35.3 | $-483.87 | -6.7% | $516.13 | -1.4 | done | can't tell from luck |
| value_ev10 | 1746 | 38.9 | 39.2 | $-751.30 | -4.3% | $248.70 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3589 | 50.8 | 50.1 | $-1048.23 | -2.9% | $-48.23 | -1.7 | done | can't tell from luck |
| value_ev5 | 2629 | 40.5 | 41.1 | $-1255.71 | -4.8% | $-255.71 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3013 | 49.3 | 49.3 | $-1464.37 | -4.9% | $-464.37 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3013 | 50.7 | 50.9 | $-1563.13 | -5.2% | $-563.13 | -2.9 | done | losing for real |
| trend_filter | 2134 | 48.6 | 50.4 | $-1850.09 | -8.7% | $-850.09 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3589 | 49.2 | 50.2 | $-2193.25 | -6.1% | $-1193.25 | -3.7 | done | losing for real |
| coinflip | 5172 | 50.0 | 50.0 | $-2213.92 | -4.3% | $-1213.92 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5172 | 50.2 | 51.3 | $-3169.18 | -6.1% | $-2169.18 | -4.5 | done | losing for real |
| always_up | 5172 | 47.9 | 49.3 | $-3650.48 | -7.1% | $-2650.48 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8980 | 48.1 | 48.8 | $-4909.27 |
| ETH | 9662 | 48.1 | 48.1 | $-5150.04 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
