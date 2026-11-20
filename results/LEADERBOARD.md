# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 2:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 938 windows, 25938 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 476 | 35.1 | 34.8 | $-155.74 | -3.3% | $844.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1171 | 37.9 | 39.1 | $-713.12 | -6.1% | $286.88 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 2652 | 51.0 | 50.6 | $-881.41 | -3.3% | $118.59 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2216 | 50.1 | 49.9 | $-947.59 | -4.3% | $52.41 | -2.0 | done | losing for real |
| trend_filter | 1542 | 50.0 | 51.0 | $-1063.55 | -6.9% | $-63.55 | -2.8 | done | losing for real |
| value_ev5 | 1781 | 39.6 | 41.0 | $-1169.62 | -6.6% | $-169.62 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 2216 | 49.9 | 50.9 | $-1545.45 | -7.0% | $-545.45 | -3.4 | done | losing for real |
| coinflip | 3744 | 50.4 | 50.4 | $-1554.34 | -4.2% | $-554.34 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2652 | 49.0 | 50.3 | $-1726.45 | -6.5% | $-726.45 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3744 | 51.0 | 51.6 | $-1906.47 | -5.1% | $-906.47 | -3.2 | done | losing for real |
| always_up | 3744 | 46.7 | 49.7 | $-3870.46 | -10.3% | $-2870.46 | -6.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5910 | 48.1 | 49.1 | $-3505.30 |
| ETH | 6450 | 48.2 | 48.6 | $-4090.89 |
| SOL | 6768 | 48.2 | 48.6 | $-3997.54 |
| XRP | 6810 | 48.3 | 48.5 | $-3940.47 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
