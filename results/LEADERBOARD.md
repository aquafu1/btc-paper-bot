# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 9:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 917 windows, 25316 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 473 | 34.9 | 34.8 | $-191.30 | -4.0% | $808.70 | -0.7 | done | can't tell from luck |
| value_ev10 | 1157 | 38.0 | 39.1 | $-678.14 | -5.9% | $321.86 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 2146 | 50.0 | 49.8 | $-932.50 | -4.3% | $67.50 | -2.0 | done | losing for real |
| trend_filter | 1504 | 50.0 | 51.0 | $-1015.56 | -6.8% | $-15.56 | -2.7 | done | losing for real |
| reversal_15m_0.10pct | 2577 | 50.6 | 50.5 | $-1041.75 | -4.0% | $-41.75 | -2.1 | done | losing for real |
| value_ev5 | 1753 | 39.6 | 41.0 | $-1122.75 | -6.4% | $-122.75 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 2577 | 49.4 | 50.3 | $-1443.51 | -5.6% | $-443.51 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2146 | 50.0 | 50.9 | $-1459.26 | -6.8% | $-459.26 | -3.2 | done | losing for real |
| coinflip | 3661 | 50.3 | 50.3 | $-1561.04 | -4.3% | $-561.04 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3661 | 51.1 | 51.6 | $-1768.17 | -4.8% | $-768.17 | -3.0 | done | losing for real |
| always_up | 3661 | 46.9 | 49.7 | $-3651.63 | -10.0% | $-2651.63 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5764 | 48.2 | 49.1 | $-3308.58 |
| ETH | 6302 | 48.1 | 48.5 | $-3920.16 |
| SOL | 6602 | 48.2 | 48.6 | $-3866.38 |
| XRP | 6648 | 48.3 | 48.5 | $-3770.50 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
