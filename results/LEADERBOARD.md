# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 9:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1351 windows, 35396 settled trades, 407 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 699 | 34.2 | 35.4 | $-551.96 | -7.9% | $448.04 | -1.6 | done | can't tell from luck |
| value_ev10 | 1708 | 38.7 | 39.2 | $-837.95 | -4.9% | $162.05 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3540 | 50.8 | 50.1 | $-1028.31 | -2.9% | $-28.31 | -1.7 | done | can't tell from luck |
| value_ev5 | 2579 | 40.4 | 41.1 | $-1348.47 | -5.2% | $-348.47 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 2974 | 49.4 | 49.5 | $-1465.27 | -4.9% | $-465.27 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2974 | 50.6 | 50.9 | $-1560.02 | -5.2% | $-560.02 | -2.9 | done | losing for real |
| trend_filter | 2106 | 48.6 | 50.4 | $-1829.16 | -8.7% | $-829.16 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3540 | 49.2 | 50.3 | $-2229.90 | -6.3% | $-1229.90 | -3.8 | done | losing for real |
| coinflip | 5092 | 49.9 | 50.0 | $-2322.43 | -4.6% | $-1322.43 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5092 | 50.3 | 51.3 | $-3043.39 | -6.0% | $-2043.39 | -4.4 | done | losing for real |
| always_up | 5092 | 47.9 | 49.3 | $-3704.82 | -7.3% | $-2704.82 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8702 | 47.8 | 48.8 | $-5324.29 |
| ETH | 9384 | 48.2 | 48.2 | $-5013.17 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
