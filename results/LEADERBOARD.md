# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 4:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1427 windows, 36498 settled trades, 429 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 735 | 34.6 | 35.3 | $-515.63 | -7.0% | $484.37 | -1.5 | done | can't tell from luck |
| value_ev10 | 1774 | 38.8 | 39.1 | $-813.63 | -4.6% | $186.37 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3643 | 50.8 | 50.1 | $-1033.47 | -2.8% | $-33.47 | -1.7 | done | can't tell from luck |
| value_ev5 | 2675 | 40.6 | 41.1 | $-1288.07 | -4.8% | $-288.07 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3062 | 49.2 | 49.3 | $-1528.56 | -5.0% | $-528.56 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3062 | 50.8 | 51.0 | $-1548.70 | -5.1% | $-548.70 | -2.9 | done | losing for real |
| trend_filter | 2166 | 48.6 | 50.3 | $-1885.16 | -8.7% | $-885.16 | -4.1 | done | losing for real |
| coinflip | 5246 | 50.1 | 50.0 | $-2219.11 | -4.2% | $-1219.11 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3643 | 49.2 | 50.2 | $-2235.49 | -6.1% | $-1235.49 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 5246 | 50.2 | 51.3 | $-3231.71 | -6.2% | $-2231.71 | -4.6 | done | losing for real |
| always_up | 5246 | 47.9 | 49.3 | $-3664.86 | -7.0% | $-2664.86 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9247 | 48.1 | 48.7 | $-4969.20 |
| ETH | 9941 | 48.0 | 48.0 | $-5410.96 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
