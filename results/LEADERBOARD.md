# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 6:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1288 windows, 34473 settled trades, 410 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 679 | 33.9 | 35.3 | $-569.22 | -8.4% | $430.78 | -1.7 | done | can't tell from luck |
| value_ev10 | 1657 | 38.6 | 39.2 | $-854.06 | -5.2% | $145.94 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3459 | 50.7 | 50.2 | $-1119.81 | -3.2% | $-119.81 | -1.9 | done | can't tell from luck |
| value_ev5 | 2504 | 40.4 | 41.1 | $-1321.75 | -5.3% | $-321.75 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2888 | 49.4 | 49.4 | $-1365.74 | -4.7% | $-365.74 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2888 | 50.6 | 51.0 | $-1625.21 | -5.6% | $-625.21 | -3.1 | done | losing for real |
| trend_filter | 2038 | 49.0 | 50.5 | $-1651.53 | -8.1% | $-651.53 | -3.8 | done | losing for real |
| momentum_15m_0.10pct | 3459 | 49.3 | 50.3 | $-2124.32 | -6.1% | $-1124.32 | -3.7 | done | losing for real |
| coinflip | 4967 | 50.0 | 50.1 | $-2249.64 | -4.5% | $-1249.64 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4967 | 50.5 | 51.4 | $-2776.73 | -5.6% | $-1776.73 | -4.1 | done | losing for real |
| always_up | 4967 | 47.9 | 49.3 | $-3629.81 | -7.3% | $-2629.81 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8262 | 48.0 | 48.8 | $-4820.32 |
| ETH | 8901 | 48.2 | 48.2 | $-4883.29 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
