# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 11:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1550 windows, 38091 settled trades, 411 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 785 | 34.1 | 35.3 | $-654.88 | -8.3% | $345.12 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3776 | 50.9 | 50.0 | $-986.02 | -2.6% | $13.98 | -1.6 | done | can't tell from luck |
| value_ev10 | 1875 | 38.3 | 39.1 | $-1075.53 | -5.7% | $-75.53 | -2.0 | done | losing for real |
| value_ev5 | 2820 | 40.4 | 41.1 | $-1479.18 | -5.2% | $-479.18 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 3169 | 51.0 | 51.0 | $-1544.76 | -4.9% | $-544.76 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 3169 | 49.0 | 49.2 | $-1650.89 | -5.2% | $-650.89 | -2.9 | done | losing for real |
| trend_filter | 2248 | 48.6 | 50.3 | $-1927.37 | -8.6% | $-927.37 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3776 | 49.1 | 50.2 | $-2357.25 | -6.2% | $-1357.25 | -3.9 | done | losing for real |
| coinflip | 5491 | 49.9 | 49.9 | $-2459.20 | -4.5% | $-1459.20 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5491 | 50.2 | 51.3 | $-3422.89 | -6.2% | $-2422.89 | -4.8 | done | losing for real |
| always_up | 5491 | 48.2 | 49.2 | $-3559.65 | -6.5% | $-2559.65 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9998 | 47.9 | 48.7 | $-5802.48 |
| ETH | 10783 | 48.0 | 47.8 | $-5730.91 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
