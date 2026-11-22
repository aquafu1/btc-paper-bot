# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 9:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1108 windows, 30664 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 585 | 34.4 | 35.1 | $-380.56 | -6.5% | $619.44 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 3094 | 51.3 | 50.4 | $-759.24 | -2.5% | $240.76 | -1.4 | done | can't tell from luck |
| value_ev10 | 1429 | 37.9 | 39.1 | $-950.15 | -6.6% | $49.85 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2601 | 49.8 | 49.4 | $-1053.53 | -4.1% | $-53.53 | -2.1 | done | losing for real |
| value_ev5 | 2166 | 39.8 | 41.0 | $-1335.13 | -6.2% | $-335.13 | -2.4 | done | losing for real |
| trend_filter | 1813 | 49.3 | 50.4 | $-1337.24 | -7.4% | $-337.24 | -3.2 | done | losing for real |
| coinflip | 4427 | 50.5 | 50.2 | $-1677.57 | -3.8% | $-677.57 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2601 | 50.2 | 51.1 | $-1719.36 | -6.6% | $-719.36 | -3.5 | done | losing for real |
| momentum_15m_0.10pct | 3094 | 48.7 | 50.2 | $-2144.64 | -6.9% | $-1144.64 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 4427 | 50.7 | 51.4 | $-2347.28 | -5.3% | $-1347.28 | -3.6 | done | losing for real |
| always_up | 4427 | 47.5 | 49.3 | $-3561.90 | -8.0% | $-2561.90 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7024 | 48.4 | 49.0 | $-3501.44 |
| ETH | 7585 | 48.1 | 48.4 | $-4563.19 |
| SOL | 7985 | 48.1 | 48.4 | $-4490.08 |
| XRP | 8070 | 48.2 | 48.2 | $-4711.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
