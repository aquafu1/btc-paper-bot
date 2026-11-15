# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 6:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 425 windows, 11677 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 210 | 34.8 | 36.4 | $-166.95 | -8.0% | $833.05 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 999 | 50.5 | 50.0 | $-336.33 | -3.4% | $663.67 | -1.1 | done | can't tell from luck |
| value_ev10 | 544 | 39.2 | 40.4 | $-361.49 | -6.6% | $638.51 | -1.3 | done | can't tell from luck |
| trend_filter | 667 | 49.5 | 50.7 | $-438.88 | -6.6% | $561.12 | -1.7 | done | can't tell from luck |
| value_ev5 | 818 | 41.2 | 42.1 | $-488.73 | -6.0% | $511.27 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1182 | 49.1 | 50.0 | $-646.00 | -5.5% | $354.00 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1182 | 50.9 | 51.8 | $-694.72 | -5.9% | $305.28 | -2.1 | done | losing for real |
| coinflip | 1692 | 50.5 | 51.0 | $-773.01 | -4.6% | $226.99 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 999 | 49.5 | 51.9 | $-856.15 | -8.6% | $143.85 | -2.8 | done | losing for real |
| momentum_5m_0.00pct | 1692 | 49.5 | 51.6 | $-1282.00 | -7.6% | $-282.00 | -3.2 | done | losing for real |
| always_up | 1692 | 46.0 | 50.7 | $-2152.14 | -12.7% | $-1152.14 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2645 | 47.6 | 49.4 | $-1976.13 |
| ETH | 2929 | 48.0 | 49.0 | $-1857.42 |
| SOL | 3028 | 47.7 | 49.5 | $-2579.96 |
| XRP | 3075 | 48.7 | 49.3 | $-1782.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
