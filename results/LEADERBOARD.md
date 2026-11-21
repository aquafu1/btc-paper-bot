# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 4:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 993 windows, 27611 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 505 | 34.3 | 34.9 | $-285.26 | -5.6% | $714.74 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2818 | 51.0 | 50.4 | $-900.75 | -3.2% | $99.25 | -1.7 | done | can't tell from luck |
| value_ev10 | 1259 | 37.5 | 39.1 | $-901.38 | -7.2% | $98.62 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2375 | 49.8 | 49.7 | $-1096.76 | -4.6% | $-96.76 | -2.3 | done | losing for real |
| trend_filter | 1657 | 49.5 | 50.8 | $-1224.66 | -7.4% | $-224.66 | -3.1 | done | losing for real |
| value_ev5 | 1909 | 39.5 | 41.0 | $-1284.56 | -6.7% | $-284.56 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2375 | 50.2 | 50.9 | $-1541.83 | -6.5% | $-541.83 | -3.2 | done | losing for real |
| coinflip | 3965 | 50.2 | 50.3 | $-1791.30 | -4.5% | $-791.30 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2818 | 49.0 | 50.4 | $-1874.40 | -6.7% | $-874.40 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 3965 | 50.8 | 51.5 | $-2129.07 | -5.4% | $-1129.07 | -3.5 | done | losing for real |
| always_up | 3965 | 46.9 | 49.6 | $-3926.07 | -9.9% | $-2926.07 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6299 | 48.2 | 49.1 | $-3549.44 |
| ETH | 6858 | 48.0 | 48.5 | $-4493.09 |
| SOL | 7214 | 48.1 | 48.6 | $-4285.45 |
| XRP | 7240 | 48.1 | 48.5 | $-4628.07 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
