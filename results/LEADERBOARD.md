# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 4:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 946 windows, 26227 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 483 | 35.0 | 34.9 | $-173.29 | -3.6% | $826.71 | -0.6 | done | can't tell from luck |
| value_ev10 | 1188 | 38.0 | 39.1 | $-680.60 | -5.7% | $319.40 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2681 | 51.1 | 50.6 | $-854.51 | -3.2% | $145.49 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2244 | 50.1 | 49.8 | $-905.51 | -4.0% | $94.49 | -1.9 | done | can't tell from luck |
| trend_filter | 1563 | 50.0 | 50.9 | $-1022.93 | -6.5% | $-22.93 | -2.7 | done | losing for real |
| value_ev5 | 1806 | 39.9 | 41.0 | $-1054.38 | -5.8% | $-54.38 | -2.1 | done | losing for real |
| coinflip | 3779 | 50.4 | 50.3 | $-1595.09 | -4.2% | $-595.09 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2244 | 49.9 | 51.0 | $-1601.23 | -7.1% | $-601.23 | -3.5 | done | losing for real |
| momentum_15m_0.10pct | 2681 | 48.9 | 50.2 | $-1773.30 | -6.6% | $-773.30 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 3779 | 51.0 | 51.6 | $-1866.14 | -4.9% | $-866.14 | -3.1 | done | losing for real |
| always_up | 3779 | 46.8 | 49.6 | $-3768.79 | -10.0% | $-2768.79 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5983 | 48.2 | 49.0 | $-3428.01 |
| ETH | 6519 | 48.2 | 48.5 | $-4040.51 |
| SOL | 6838 | 48.2 | 48.6 | $-3829.61 |
| XRP | 6887 | 48.3 | 48.5 | $-3997.65 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
