# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 10, 3:05 PM CT.** Running since -: 0 windows, 0 settled trades, 0 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| coinflip | 0 | - | - | - | - | - | - | - | no trades yet |
| always_up | 0 | - | - | - | - | - | - | - | no trades yet |
| trend_filter | 0 | - | - | - | - | - | - | - | no trades yet |
| momentum_15m_0.10pct | 0 | - | - | - | - | - | - | - | no trades yet |
| reversal_15m_0.10pct | 0 | - | - | - | - | - | - | - | no trades yet |
| momentum_60m_0.30pct | 0 | - | - | - | - | - | - | - | no trades yet |
| reversal_60m_0.30pct | 0 | - | - | - | - | - | - | - | no trades yet |
| momentum_5m_0.00pct | 0 | - | - | - | - | - | - | - | no trades yet |
| value_ev5 | 0 | - | - | - | - | - | - | - | no trades yet |
| value_ev10 | 0 | - | - | - | - | - | - | - | no trades yet |
| value_ev20 | 0 | - | - | - | - | - | - | - | no trades yet |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 0 | - | - | - |
| ETH | 0 | - | - | - |
| SOL | 0 | - | - | - |
| XRP | 0 | - | - | - |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
