# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 6:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 955 windows, 26468 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 487 | 35.1 | 34.9 | $-154.35 | -3.2% | $845.65 | -0.5 | done | can't tell from luck |
| value_ev10 | 1201 | 38.1 | 39.1 | $-678.29 | -5.6% | $321.71 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2705 | 51.2 | 50.6 | $-791.71 | -2.9% | $208.29 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2263 | 50.2 | 49.7 | $-875.64 | -3.9% | $124.36 | -1.8 | done | can't tell from luck |
| trend_filter | 1584 | 50.0 | 50.8 | $-1024.56 | -6.5% | $-24.56 | -2.6 | done | losing for real |
| value_ev5 | 1824 | 39.9 | 41.0 | $-1060.73 | -5.8% | $-60.73 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2263 | 49.8 | 51.0 | $-1631.89 | -7.2% | $-631.89 | -3.5 | done | losing for real |
| coinflip | 3812 | 50.3 | 50.4 | $-1689.62 | -4.4% | $-689.62 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 2705 | 48.8 | 50.2 | $-1863.81 | -6.9% | $-863.81 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 3812 | 50.9 | 51.5 | $-1911.63 | -5.0% | $-911.63 | -3.2 | done | losing for real |
| always_up | 3812 | 46.8 | 49.6 | $-3772.07 | -9.9% | $-2772.07 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6032 | 48.1 | 49.0 | $-3468.56 |
| ETH | 6575 | 48.1 | 48.5 | $-4030.14 |
| SOL | 6905 | 48.3 | 48.6 | $-3818.74 |
| XRP | 6956 | 48.2 | 48.5 | $-4136.87 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
