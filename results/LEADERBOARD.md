# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 12:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 786 windows, 21653 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 404 | 32.9 | 34.9 | $-391.45 | -9.7% | $608.55 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 1834 | 50.1 | 49.6 | $-715.86 | -3.9% | $284.14 | -1.7 | done | can't tell from luck |
| trend_filter | 1272 | 50.2 | 50.8 | $-747.72 | -5.9% | $252.28 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2211 | 51.0 | 50.6 | $-753.18 | -3.4% | $246.82 | -1.6 | done | can't tell from luck |
| value_ev10 | 986 | 37.3 | 39.1 | $-792.30 | -8.0% | $207.70 | -2.1 | done | losing for real |
| value_ev5 | 1493 | 39.7 | 41.1 | $-1020.62 | -6.8% | $-20.62 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1834 | 49.9 | 51.2 | $-1312.25 | -7.2% | $-312.25 | -3.1 | done | losing for real |
| coinflip | 3136 | 50.3 | 50.3 | $-1338.22 | -4.3% | $-338.22 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 2211 | 49.0 | 50.2 | $-1417.72 | -6.4% | $-417.72 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 3136 | 51.2 | 51.7 | $-1449.97 | -4.6% | $-449.97 | -2.7 | done | losing for real |
| always_up | 3136 | 47.4 | 49.6 | $-2691.02 | -8.6% | $-1691.02 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4920 | 48.3 | 49.1 | $-2906.87 |
| ETH | 5401 | 48.0 | 48.5 | $-3607.04 |
| SOL | 5638 | 48.2 | 48.6 | $-3201.42 |
| XRP | 5694 | 48.5 | 48.5 | $-2914.98 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
