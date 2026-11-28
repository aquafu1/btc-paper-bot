# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 28, 12:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1648 windows, 39338 settled trades, 398 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 838 | 34.4 | 35.2 | $-623.68 | -7.4% | $376.32 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3867 | 50.8 | 49.9 | $-1027.22 | -2.7% | $-27.22 | -1.6 | done | can't tell from luck |
| value_ev10 | 1977 | 38.3 | 39.0 | $-1112.71 | -5.6% | $-112.71 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 3237 | 51.0 | 50.9 | $-1472.53 | -4.5% | $-472.53 | -2.6 | done | losing for real |
| value_ev5 | 2954 | 40.4 | 41.0 | $-1575.41 | -5.3% | $-575.41 | -2.5 | done | losing for real |
| momentum_60m_0.30pct | 3237 | 49.0 | 49.3 | $-1772.51 | -5.5% | $-772.51 | -3.1 | done | losing for real |
| trend_filter | 2303 | 48.5 | 50.4 | $-2064.47 | -9.0% | $-1064.47 | -4.4 | done | losing for real |
| momentum_15m_0.10pct | 3867 | 49.2 | 50.2 | $-2352.58 | -6.1% | $-1352.58 | -3.8 | done | losing for real |
| coinflip | 5686 | 49.9 | 49.9 | $-2524.08 | -4.4% | $-1524.08 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 5686 | 50.2 | 51.3 | $-3503.18 | -6.2% | $-2503.18 | -4.8 | done | losing for real |
| always_up | 5686 | 48.2 | 49.0 | $-3569.52 | -6.3% | $-2569.52 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10575 | 47.9 | 48.5 | $-5979.88 |
| ETH | 11453 | 47.9 | 47.6 | $-6033.76 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
