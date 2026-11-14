# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 10:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 298 windows, 7945 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 789 | 53.4 | 51.9 | $-119.78 | -1.5% | $880.22 | -0.4 | done | can't tell from luck |
| value_ev20 | 148 | 35.1 | 36.5 | $-134.69 | -9.1% | $865.31 | -0.9 | Sun 2:30 AM | too few trades (148/200) |
| reversal_60m_0.30pct | 643 | 51.9 | 51.8 | $-275.23 | -4.3% | $724.77 | -1.1 | done | can't tell from luck |
| value_ev10 | 383 | 38.4 | 40.5 | $-361.48 | -9.4% | $638.52 | -1.6 | done | can't tell from luck |
| trend_filter | 433 | 46.9 | 50.3 | $-493.62 | -11.4% | $506.38 | -2.4 | done | losing for real |
| value_ev5 | 562 | 40.0 | 42.1 | $-532.73 | -9.5% | $467.27 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 643 | 48.1 | 49.8 | $-544.60 | -8.5% | $455.40 | -2.2 | done | losing for real |
| coinflip | 1185 | 50.3 | 50.9 | $-646.04 | -5.5% | $353.96 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 789 | 46.6 | 49.9 | $-838.94 | -10.6% | $161.06 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1185 | 49.4 | 51.3 | $-946.89 | -8.0% | $53.11 | -2.9 | done | losing for real |
| always_up | 1185 | 47.0 | 50.3 | $-1269.02 | -10.7% | $-269.02 | -3.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1781 | 46.8 | 49.4 | $-1659.73 |
| ETH | 1988 | 47.2 | 48.7 | $-1807.87 |
| SOL | 2061 | 48.3 | 49.3 | $-1552.59 |
| XRP | 2115 | 48.7 | 49.0 | $-1142.82 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
