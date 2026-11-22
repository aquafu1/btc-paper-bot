# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 6:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1097 windows, 30347 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 575 | 34.4 | 35.0 | $-350.36 | -6.1% | $649.64 | -1.1 | done | can't tell from luck |
| value_ev10 | 1408 | 38.1 | 39.1 | $-853.68 | -6.1% | $146.32 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3063 | 51.0 | 50.5 | $-936.01 | -3.1% | $63.99 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2580 | 49.7 | 49.4 | $-1102.56 | -4.3% | $-102.56 | -2.2 | done | losing for real |
| value_ev5 | 2139 | 40.0 | 41.0 | $-1223.29 | -5.7% | $-223.29 | -2.2 | done | losing for real |
| trend_filter | 1799 | 49.4 | 50.5 | $-1317.14 | -7.3% | $-317.14 | -3.2 | done | losing for real |
| reversal_60m_0.30pct | 2580 | 50.3 | 51.1 | $-1652.59 | -6.4% | $-652.59 | -3.3 | done | losing for real |
| coinflip | 4380 | 50.5 | 50.2 | $-1670.72 | -3.8% | $-670.72 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 3063 | 49.0 | 50.2 | $-1960.38 | -6.4% | $-960.38 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4380 | 50.8 | 51.4 | $-2231.03 | -5.1% | $-1231.03 | -3.5 | done | losing for real |
| always_up | 4380 | 47.5 | 49.3 | $-3521.60 | -8.0% | $-2521.60 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6941 | 48.4 | 49.0 | $-3392.41 |
| ETH | 7519 | 48.2 | 48.4 | $-4427.21 |
| SOL | 7903 | 48.1 | 48.4 | $-4420.59 |
| XRP | 7984 | 48.2 | 48.2 | $-4579.16 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
