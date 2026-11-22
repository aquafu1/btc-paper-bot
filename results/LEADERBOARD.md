# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 3:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1133 windows, 31304 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 601 | 34.6 | 35.2 | $-363.62 | -6.1% | $636.38 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3151 | 51.1 | 50.5 | $-875.65 | -2.8% | $124.35 | -1.6 | done | can't tell from luck |
| value_ev10 | 1467 | 38.1 | 39.2 | $-913.03 | -6.2% | $86.97 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2643 | 49.6 | 49.4 | $-1146.32 | -4.3% | $-146.32 | -2.2 | done | losing for real |
| value_ev5 | 2219 | 40.0 | 41.1 | $-1304.50 | -5.9% | $-304.50 | -2.3 | done | losing for real |
| trend_filter | 1854 | 49.1 | 50.4 | $-1436.36 | -7.7% | $-436.36 | -3.4 | done | losing for real |
| reversal_60m_0.30pct | 2643 | 50.4 | 51.1 | $-1647.08 | -6.2% | $-647.08 | -3.3 | done | losing for real |
| coinflip | 4525 | 50.4 | 50.2 | $-1790.13 | -4.0% | $-790.13 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 3151 | 48.9 | 50.2 | $-2053.24 | -6.5% | $-1053.24 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4525 | 50.3 | 51.4 | $-2756.39 | -6.1% | $-1756.39 | -4.2 | done | losing for real |
| always_up | 4525 | 47.7 | 49.3 | $-3430.59 | -7.6% | $-2430.59 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7171 | 48.3 | 49.0 | $-3648.28 |
| ETH | 7761 | 48.2 | 48.4 | $-4596.00 |
| SOL | 8145 | 48.0 | 48.4 | $-4654.91 |
| XRP | 8227 | 48.1 | 48.2 | $-4817.73 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
