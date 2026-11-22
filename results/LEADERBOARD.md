# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 9:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1060 windows, 29318 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 547 | 34.6 | 35.1 | $-310.90 | -5.7% | $689.10 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2968 | 51.2 | 50.4 | $-789.81 | -2.7% | $210.19 | -1.5 | done | can't tell from luck |
| value_ev10 | 1357 | 37.7 | 39.2 | $-953.77 | -7.0% | $46.23 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2489 | 49.7 | 49.6 | $-1183.67 | -4.8% | $-183.67 | -2.4 | done | losing for real |
| trend_filter | 1745 | 49.4 | 50.7 | $-1334.67 | -7.6% | $-334.67 | -3.3 | done | losing for real |
| value_ev5 | 2059 | 39.6 | 41.0 | $-1359.36 | -6.6% | $-359.36 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2489 | 50.3 | 51.0 | $-1558.08 | -6.3% | $-558.08 | -3.2 | done | losing for real |
| coinflip | 4232 | 50.5 | 50.3 | $-1712.39 | -4.0% | $-712.39 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2968 | 48.8 | 50.3 | $-2071.06 | -7.0% | $-1071.06 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4232 | 50.9 | 51.5 | $-2211.59 | -5.2% | $-1211.59 | -3.5 | done | losing for real |
| always_up | 4232 | 47.3 | 49.4 | $-3711.17 | -8.8% | $-2711.17 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6688 | 48.4 | 49.0 | $-3446.77 |
| ETH | 7253 | 48.1 | 48.5 | $-4579.29 |
| SOL | 7651 | 48.0 | 48.5 | $-4505.38 |
| XRP | 7726 | 48.2 | 48.3 | $-4665.04 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
