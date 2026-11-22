# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 12:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1072 windows, 29664 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 553 | 34.4 | 35.1 | $-343.30 | -6.2% | $656.70 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3006 | 51.3 | 50.5 | $-754.53 | -2.5% | $245.47 | -1.4 | done | can't tell from luck |
| value_ev10 | 1368 | 37.6 | 39.2 | $-969.47 | -7.1% | $30.53 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2521 | 49.8 | 49.6 | $-1081.47 | -4.3% | $-81.47 | -2.2 | done | losing for real |
| trend_filter | 1765 | 49.6 | 50.7 | $-1236.23 | -7.0% | $-236.23 | -3.0 | done | losing for real |
| value_ev5 | 2081 | 39.7 | 41.0 | $-1357.46 | -6.5% | $-357.46 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2521 | 50.2 | 51.0 | $-1659.02 | -6.6% | $-659.02 | -3.4 | done | losing for real |
| coinflip | 4281 | 50.5 | 50.3 | $-1694.85 | -4.0% | $-694.85 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 4281 | 51.0 | 51.5 | $-2070.31 | -4.8% | $-1070.31 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3006 | 48.7 | 50.3 | $-2134.40 | -7.1% | $-1134.40 | -3.9 | done | losing for real |
| always_up | 4281 | 47.2 | 49.4 | $-3842.63 | -9.0% | $-2842.63 | -5.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6774 | 48.4 | 49.0 | $-3464.10 |
| ETH | 7337 | 48.1 | 48.5 | $-4613.19 |
| SOL | 7735 | 48.1 | 48.5 | $-4483.65 |
| XRP | 7818 | 48.2 | 48.3 | $-4582.72 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
