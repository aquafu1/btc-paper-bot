# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 4:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 466 windows, 12781 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 237 | 35.0 | 35.9 | $-136.40 | -5.8% | $863.60 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1081 | 50.8 | 49.9 | $-276.35 | -2.6% | $723.65 | -0.8 | done | can't tell from luck |
| value_ev10 | 605 | 39.0 | 40.1 | $-367.60 | -6.1% | $632.40 | -1.2 | done | can't tell from luck |
| trend_filter | 738 | 49.7 | 50.7 | $-432.44 | -5.9% | $567.56 | -1.6 | done | can't tell from luck |
| value_ev5 | 895 | 41.0 | 41.8 | $-490.50 | -5.5% | $509.50 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1288 | 49.8 | 50.0 | $-500.02 | -3.9% | $499.98 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1288 | 50.2 | 51.6 | $-910.61 | -7.1% | $89.39 | -2.7 | done | losing for real |
| coinflip | 1856 | 49.9 | 50.8 | $-1001.88 | -5.4% | $-1.88 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1081 | 49.2 | 51.8 | $-1002.08 | -9.3% | $-2.08 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1856 | 49.8 | 51.6 | $-1293.52 | -7.0% | $-293.52 | -3.1 | done | losing for real |
| always_up | 1856 | 46.4 | 50.4 | $-2151.83 | -11.6% | $-1151.83 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2891 | 47.6 | 49.2 | $-2217.44 |
| ETH | 3207 | 48.1 | 48.8 | $-2059.73 |
| SOL | 3328 | 47.7 | 49.3 | $-2553.15 |
| XRP | 3355 | 48.6 | 49.1 | $-1732.91 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
