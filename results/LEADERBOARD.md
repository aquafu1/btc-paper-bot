# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 10:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1112 windows, 30756 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 586 | 34.3 | 35.1 | $-390.56 | -6.7% | $609.44 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 3101 | 51.3 | 50.4 | $-759.13 | -2.4% | $240.87 | -1.4 | done | can't tell from luck |
| value_ev10 | 1432 | 37.8 | 39.1 | $-980.15 | -6.8% | $19.85 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2611 | 49.7 | 49.4 | $-1100.46 | -4.2% | $-100.46 | -2.1 | done | losing for real |
| value_ev5 | 2171 | 39.8 | 41.0 | $-1363.96 | -6.3% | $-363.96 | -2.5 | done | losing for real |
| trend_filter | 1823 | 49.2 | 50.4 | $-1384.17 | -7.6% | $-384.17 | -3.3 | done | losing for real |
| reversal_60m_0.30pct | 2611 | 50.3 | 51.1 | $-1680.98 | -6.4% | $-680.98 | -3.4 | done | losing for real |
| coinflip | 4440 | 50.5 | 50.2 | $-1717.58 | -3.9% | $-717.58 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 3101 | 48.7 | 50.2 | $-2157.63 | -7.0% | $-1157.63 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 4440 | 50.6 | 51.4 | $-2408.88 | -5.4% | $-1408.88 | -3.7 | done | losing for real |
| always_up | 4440 | 47.5 | 49.3 | $-3588.15 | -8.1% | $-2588.15 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7039 | 48.4 | 49.0 | $-3556.72 |
| ETH | 7621 | 48.1 | 48.4 | $-4688.23 |
| SOL | 8008 | 48.0 | 48.4 | $-4576.87 |
| XRP | 8088 | 48.2 | 48.2 | $-4709.85 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
