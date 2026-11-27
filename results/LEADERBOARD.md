# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 7:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1535 windows, 37883 settled trades, 371 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 774 | 34.4 | 35.3 | $-596.25 | -7.7% | $403.75 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3758 | 50.9 | 50.0 | $-978.99 | -2.6% | $21.01 | -1.6 | done | can't tell from luck |
| value_ev10 | 1857 | 38.5 | 39.2 | $-997.26 | -5.4% | $2.74 | -1.9 | done | can't tell from luck |
| value_ev5 | 2800 | 40.5 | 41.1 | $-1401.63 | -5.0% | $-401.63 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3155 | 51.0 | 51.0 | $-1478.44 | -4.7% | $-478.44 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3155 | 49.0 | 49.2 | $-1685.26 | -5.3% | $-685.26 | -3.0 | done | losing for real |
| trend_filter | 2243 | 48.6 | 50.3 | $-1921.36 | -8.6% | $-921.36 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3758 | 49.1 | 50.2 | $-2335.46 | -6.2% | $-1335.46 | -3.8 | done | losing for real |
| coinflip | 5461 | 49.9 | 50.0 | $-2445.05 | -4.5% | $-1445.05 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5461 | 50.1 | 51.3 | $-3410.50 | -6.2% | $-2410.50 | -4.8 | done | losing for real |
| always_up | 5461 | 48.1 | 49.2 | $-3573.14 | -6.5% | $-2573.14 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9902 | 47.9 | 48.7 | $-5674.12 |
| ETH | 10671 | 48.1 | 47.9 | $-5564.99 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
