# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 2:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 984 windows, 27354 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 503 | 34.4 | 34.9 | $-265.26 | -5.3% | $734.74 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2793 | 51.1 | 50.5 | $-828.11 | -3.0% | $171.89 | -1.6 | done | can't tell from luck |
| value_ev10 | 1251 | 37.6 | 39.1 | $-847.53 | -6.8% | $152.47 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2346 | 49.9 | 49.7 | $-1022.08 | -4.4% | $-22.08 | -2.1 | done | losing for real |
| trend_filter | 1640 | 49.7 | 50.8 | $-1165.57 | -7.1% | $-165.57 | -3.0 | done | losing for real |
| value_ev5 | 1892 | 39.6 | 41.0 | $-1204.87 | -6.4% | $-204.87 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 2346 | 50.1 | 50.9 | $-1576.13 | -6.7% | $-576.13 | -3.3 | done | losing for real |
| coinflip | 3930 | 50.3 | 50.3 | $-1701.20 | -4.3% | $-701.20 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2793 | 48.9 | 50.3 | $-1926.63 | -6.9% | $-926.63 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 3930 | 50.9 | 51.5 | $-2009.80 | -5.1% | $-1009.80 | -3.3 | done | losing for real |
| always_up | 3930 | 46.8 | 49.6 | $-3975.58 | -10.1% | $-2975.58 | -6.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6241 | 48.2 | 49.1 | $-3491.11 |
| ETH | 6795 | 48.0 | 48.5 | $-4405.10 |
| SOL | 7146 | 48.1 | 48.6 | $-4206.82 |
| XRP | 7172 | 48.2 | 48.5 | $-4419.74 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
