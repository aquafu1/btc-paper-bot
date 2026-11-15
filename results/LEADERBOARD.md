# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 12:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 403 windows, 11055 settled trades, 30 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 199 | 36.7 | 36.5 | $-56.95 | -2.9% | $943.05 | -0.3 | Sun 1:30 AM | too few trades (199/200) |
| value_ev10 | 519 | 40.5 | 40.5 | $-174.41 | -3.4% | $825.59 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 942 | 50.7 | 49.9 | $-214.41 | -2.3% | $785.59 | -0.7 | done | can't tell from luck |
| value_ev5 | 780 | 42.1 | 42.2 | $-293.06 | -3.8% | $706.94 | -0.9 | done | can't tell from luck |
| trend_filter | 626 | 50.2 | 50.6 | $-305.23 | -4.9% | $694.77 | -1.2 | done | can't tell from luck |
| momentum_15m_0.10pct | 1113 | 49.4 | 49.9 | $-475.73 | -4.3% | $524.27 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1113 | 50.6 | 52.0 | $-720.22 | -6.5% | $279.78 | -2.3 | done | losing for real |
| coinflip | 1607 | 50.1 | 50.9 | $-804.36 | -5.0% | $195.64 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 942 | 49.3 | 52.1 | $-847.29 | -9.0% | $152.71 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 1607 | 50.0 | 51.6 | $-1022.78 | -6.4% | $-22.78 | -2.6 | done | losing for real |
| always_up | 1607 | 46.0 | 50.8 | $-2039.94 | -12.7% | $-1039.94 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2491 | 47.9 | 49.5 | $-1672.50 |
| ETH | 2780 | 47.9 | 49.0 | $-1691.14 |
| SOL | 2859 | 48.0 | 49.5 | $-2105.09 |
| XRP | 2925 | 48.9 | 49.3 | $-1485.65 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
