# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 10:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1595 windows, 38688 settled trades, 396 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 816 | 34.4 | 35.1 | $-595.00 | -7.3% | $405.00 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3817 | 50.9 | 50.0 | $-1023.04 | -2.7% | $-23.04 | -1.6 | done | can't tell from luck |
| value_ev10 | 1926 | 38.4 | 39.0 | $-1039.67 | -5.4% | $-39.67 | -1.9 | done | can't tell from luck |
| value_ev5 | 2889 | 40.4 | 41.0 | $-1480.38 | -5.1% | $-480.38 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3201 | 51.0 | 50.9 | $-1481.17 | -4.6% | $-481.17 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3201 | 49.0 | 49.2 | $-1729.43 | -5.4% | $-729.43 | -3.0 | done | losing for real |
| trend_filter | 2275 | 48.5 | 50.3 | $-2020.54 | -8.9% | $-1020.54 | -4.3 | done | losing for real |
| coinflip | 5582 | 50.1 | 49.9 | $-2328.56 | -4.2% | $-1328.56 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3817 | 49.1 | 50.2 | $-2341.64 | -6.1% | $-1341.64 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5582 | 50.1 | 51.3 | $-3492.64 | -6.3% | $-2492.64 | -4.8 | done | losing for real |
| always_up | 5582 | 48.2 | 49.1 | $-3561.47 | -6.4% | $-2561.47 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10279 | 48.0 | 48.6 | $-5803.13 |
| ETH | 11099 | 48.0 | 47.7 | $-5706.19 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
