# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 3:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1084 windows, 29969 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 563 | 34.5 | 35.2 | $-338.28 | -6.0% | $661.72 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3031 | 51.1 | 50.5 | $-850.27 | -2.8% | $149.73 | -1.5 | done | can't tell from luck |
| value_ev10 | 1385 | 37.8 | 39.2 | $-940.65 | -6.8% | $59.35 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2544 | 49.8 | 49.5 | $-1046.46 | -4.1% | $-46.46 | -2.1 | done | losing for real |
| trend_filter | 1781 | 49.6 | 50.6 | $-1217.27 | -6.8% | $-217.27 | -3.0 | done | losing for real |
| value_ev5 | 2106 | 39.8 | 41.1 | $-1318.39 | -6.3% | $-318.39 | -2.4 | done | losing for real |
| coinflip | 4328 | 50.5 | 50.3 | $-1692.80 | -3.9% | $-692.80 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2544 | 50.2 | 51.1 | $-1695.87 | -6.7% | $-695.87 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 4328 | 51.0 | 51.5 | $-2043.10 | -4.7% | $-1043.10 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3031 | 48.9 | 50.3 | $-2044.72 | -6.7% | $-1044.72 | -3.8 | done | losing for real |
| always_up | 4328 | 47.5 | 49.4 | $-3560.97 | -8.2% | $-2560.97 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6841 | 48.5 | 49.0 | $-3319.66 |
| ETH | 7422 | 48.2 | 48.5 | $-4444.15 |
| SOL | 7818 | 48.1 | 48.5 | $-4405.37 |
| XRP | 7888 | 48.3 | 48.3 | $-4579.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
