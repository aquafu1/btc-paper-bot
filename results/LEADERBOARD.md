# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 4:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 848 windows, 23382 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 436 | 33.7 | 34.8 | $-314.39 | -7.2% | $685.61 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1975 | 50.4 | 49.7 | $-719.85 | -3.6% | $280.15 | -1.6 | done | can't tell from luck |
| value_ev10 | 1069 | 37.6 | 39.0 | $-770.77 | -7.2% | $229.23 | -1.9 | done | can't tell from luck |
| trend_filter | 1378 | 50.2 | 50.9 | $-889.35 | -6.5% | $110.65 | -2.5 | done | losing for real |
| reversal_15m_0.10pct | 2388 | 50.7 | 50.5 | $-922.55 | -3.9% | $77.45 | -1.9 | done | can't tell from luck |
| value_ev5 | 1615 | 39.8 | 41.0 | $-1073.32 | -6.6% | $-73.32 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 2388 | 49.3 | 50.4 | $-1436.10 | -6.0% | $-436.10 | -3.0 | done | losing for real |
| coinflip | 3386 | 50.2 | 50.3 | $-1519.68 | -4.5% | $-519.68 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1975 | 49.6 | 51.0 | $-1536.96 | -7.8% | $-536.96 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 3386 | 51.2 | 51.7 | $-1603.75 | -4.7% | $-603.75 | -2.9 | done | losing for real |
| always_up | 3386 | 46.8 | 49.5 | $-3328.82 | -9.8% | $-2328.82 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5329 | 48.2 | 49.0 | $-3122.25 |
| ETH | 5817 | 48.0 | 48.5 | $-3993.75 |
| SOL | 6092 | 48.2 | 48.5 | $-3683.60 |
| XRP | 6144 | 48.4 | 48.5 | $-3315.94 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
