# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 2:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 985 windows, 27368 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 503 | 34.4 | 34.9 | $-265.26 | -5.3% | $734.74 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2793 | 51.1 | 50.5 | $-828.11 | -3.0% | $171.89 | -1.6 | done | can't tell from luck |
| value_ev10 | 1253 | 37.6 | 39.1 | $-867.53 | -6.9% | $132.47 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 2348 | 49.9 | 49.7 | $-1042.08 | -4.4% | $-42.08 | -2.2 | done | losing for real |
| trend_filter | 1640 | 49.7 | 50.8 | $-1165.57 | -7.1% | $-165.57 | -3.0 | done | losing for real |
| value_ev5 | 1894 | 39.6 | 41.0 | $-1224.87 | -6.5% | $-224.87 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2348 | 50.1 | 51.0 | $-1562.45 | -6.7% | $-562.45 | -3.3 | done | losing for real |
| coinflip | 3932 | 50.4 | 50.3 | $-1687.52 | -4.3% | $-687.52 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2793 | 48.9 | 50.3 | $-1926.63 | -6.9% | $-926.63 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 3932 | 50.9 | 51.5 | $-1996.13 | -5.1% | $-996.13 | -3.3 | done | losing for real |
| always_up | 3932 | 46.7 | 49.6 | $-3995.58 | -10.2% | $-2995.58 | -6.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6241 | 48.2 | 49.1 | $-3491.11 |
| ETH | 6802 | 48.0 | 48.5 | $-4423.59 |
| SOL | 7146 | 48.1 | 48.6 | $-4206.82 |
| XRP | 7179 | 48.2 | 48.5 | $-4440.22 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
