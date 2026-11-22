# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 10:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1114 windows, 30809 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 587 | 34.4 | 35.1 | $-371.05 | -6.3% | $628.95 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 3107 | 51.3 | 50.4 | $-755.25 | -2.4% | $244.75 | -1.4 | done | can't tell from luck |
| value_ev10 | 1435 | 37.9 | 39.1 | $-937.36 | -6.5% | $62.64 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2614 | 49.7 | 49.4 | $-1110.95 | -4.2% | $-110.95 | -2.2 | done | losing for real |
| value_ev5 | 2175 | 39.9 | 41.0 | $-1311.66 | -6.0% | $-311.66 | -2.4 | done | losing for real |
| trend_filter | 1826 | 49.2 | 50.4 | $-1390.26 | -7.6% | $-390.26 | -3.3 | done | losing for real |
| reversal_60m_0.30pct | 2614 | 50.3 | 51.1 | $-1663.70 | -6.4% | $-663.70 | -3.3 | done | losing for real |
| coinflip | 4448 | 50.4 | 50.2 | $-1734.78 | -3.9% | $-734.78 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 3107 | 48.7 | 50.2 | $-2161.58 | -7.0% | $-1161.58 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 4448 | 50.6 | 51.4 | $-2464.97 | -5.5% | $-1464.97 | -3.8 | done | losing for real |
| always_up | 4448 | 47.6 | 49.3 | $-3527.72 | -7.9% | $-2527.72 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7052 | 48.4 | 49.0 | $-3599.06 |
| ETH | 7634 | 48.1 | 48.4 | $-4687.47 |
| SOL | 8017 | 48.0 | 48.4 | $-4526.83 |
| XRP | 8106 | 48.2 | 48.2 | $-4615.92 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
