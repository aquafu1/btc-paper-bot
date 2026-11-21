# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 11:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 974 windows, 27024 settled trades, 70 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 496 | 34.7 | 34.8 | $-219.50 | -4.4% | $780.50 | -0.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 2761 | 51.2 | 50.5 | $-739.25 | -2.7% | $260.75 | -1.4 | done | can't tell from luck |
| value_ev10 | 1232 | 37.8 | 39.1 | $-774.80 | -6.3% | $225.20 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2311 | 50.2 | 49.7 | $-863.30 | -3.7% | $136.70 | -1.8 | done | can't tell from luck |
| value_ev5 | 1869 | 39.8 | 41.0 | $-1113.54 | -6.0% | $-113.54 | -2.2 | done | losing for real |
| trend_filter | 1619 | 49.8 | 50.9 | $-1130.22 | -7.0% | $-130.22 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2311 | 49.8 | 50.9 | $-1681.35 | -7.3% | $-681.35 | -3.6 | done | losing for real |
| coinflip | 3888 | 50.2 | 50.3 | $-1808.03 | -4.7% | $-808.03 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2761 | 48.8 | 50.3 | $-1962.56 | -7.1% | $-962.56 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3888 | 50.7 | 51.5 | $-2142.05 | -5.5% | $-1142.05 | -3.5 | done | losing for real |
| always_up | 3888 | 46.8 | 49.6 | $-3881.49 | -10.0% | $-2881.49 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6158 | 48.1 | 49.1 | $-3553.53 |
| ETH | 6717 | 48.0 | 48.5 | $-4347.56 |
| SOL | 7057 | 48.2 | 48.6 | $-4039.54 |
| XRP | 7092 | 48.1 | 48.4 | $-4375.44 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
