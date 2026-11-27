# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 1:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1606 windows, 38834 settled trades, 398 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 819 | 34.3 | 35.1 | $-625.00 | -7.6% | $375.00 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3833 | 50.9 | 50.0 | $-973.42 | -2.5% | $26.58 | -1.6 | done | can't tell from luck |
| value_ev10 | 1939 | 38.4 | 39.0 | $-1045.80 | -5.4% | $-45.80 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 3208 | 51.0 | 50.9 | $-1482.17 | -4.6% | $-482.17 | -2.7 | done | losing for real |
| value_ev5 | 2904 | 40.4 | 41.0 | $-1483.27 | -5.1% | $-483.27 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 3208 | 49.0 | 49.2 | $-1732.97 | -5.4% | $-732.97 | -3.0 | done | losing for real |
| trend_filter | 2281 | 48.4 | 50.4 | $-2050.99 | -9.0% | $-1050.99 | -4.4 | done | losing for real |
| coinflip | 5603 | 50.1 | 49.9 | $-2326.74 | -4.2% | $-1326.74 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3833 | 49.1 | 50.2 | $-2387.66 | -6.2% | $-1387.66 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 5603 | 50.1 | 51.3 | $-3523.04 | -6.3% | $-2523.04 | -4.8 | done | losing for real |
| always_up | 5603 | 48.2 | 49.1 | $-3593.81 | -6.4% | $-2593.81 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10349 | 47.9 | 48.6 | $-5869.08 |
| ETH | 11175 | 48.0 | 47.7 | $-5771.56 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
