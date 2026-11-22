# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 8:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1107 windows, 30628 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 583 | 34.3 | 35.1 | $-381.49 | -6.5% | $618.51 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 3090 | 51.3 | 50.4 | $-758.60 | -2.5% | $241.40 | -1.4 | done | can't tell from luck |
| value_ev10 | 1427 | 37.8 | 39.1 | $-951.09 | -6.7% | $48.91 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2598 | 49.8 | 49.4 | $-1061.73 | -4.1% | $-61.73 | -2.1 | done | losing for real |
| value_ev5 | 2163 | 39.9 | 41.0 | $-1326.06 | -6.1% | $-326.06 | -2.4 | done | losing for real |
| trend_filter | 1810 | 49.3 | 50.4 | $-1345.44 | -7.4% | $-345.44 | -3.2 | done | losing for real |
| coinflip | 4423 | 50.5 | 50.2 | $-1694.21 | -3.8% | $-694.21 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2598 | 50.2 | 51.1 | $-1710.29 | -6.6% | $-710.29 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3090 | 48.7 | 50.2 | $-2142.84 | -6.9% | $-1142.84 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 4423 | 50.7 | 51.4 | $-2345.48 | -5.3% | $-1345.48 | -3.6 | done | losing for real |
| always_up | 4423 | 47.5 | 49.3 | $-3578.53 | -8.1% | $-2578.53 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7013 | 48.4 | 49.0 | $-3499.84 |
| ETH | 7580 | 48.1 | 48.4 | $-4568.49 |
| SOL | 7974 | 48.1 | 48.4 | $-4484.74 |
| XRP | 8061 | 48.2 | 48.2 | $-4742.69 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
