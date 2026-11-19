# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 9:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 774 windows, 21336 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 403 | 33.0 | 34.9 | $-381.45 | -9.5% | $618.55 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2176 | 51.2 | 50.6 | $-652.29 | -3.0% | $347.71 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 1803 | 49.9 | 49.6 | $-732.98 | -4.1% | $267.02 | -1.7 | done | can't tell from luck |
| value_ev10 | 979 | 37.5 | 39.1 | $-744.62 | -7.6% | $255.38 | -1.9 | done | can't tell from luck |
| trend_filter | 1253 | 49.9 | 50.8 | $-809.19 | -6.5% | $190.81 | -2.3 | done | losing for real |
| value_ev5 | 1479 | 39.8 | 41.0 | $-964.74 | -6.5% | $35.26 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1803 | 50.1 | 51.2 | $-1216.18 | -6.7% | $-216.18 | -2.9 | done | losing for real |
| coinflip | 3088 | 50.3 | 50.3 | $-1281.73 | -4.2% | $-281.73 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 2176 | 48.8 | 50.2 | $-1447.01 | -6.6% | $-447.01 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 3088 | 51.0 | 51.6 | $-1502.44 | -4.9% | $-502.44 | -2.8 | done | losing for real |
| always_up | 3088 | 47.0 | 49.5 | $-2895.64 | -9.4% | $-1895.64 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4842 | 48.2 | 49.1 | $-2933.27 |
| ETH | 5329 | 47.9 | 48.5 | $-3636.29 |
| SOL | 5555 | 48.0 | 48.5 | $-3291.47 |
| XRP | 5610 | 48.4 | 48.4 | $-2767.22 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
