# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 8:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1107 windows, 30612 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 583 | 34.3 | 35.1 | $-381.49 | -6.5% | $618.51 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 3087 | 51.2 | 50.4 | $-787.18 | -2.5% | $212.82 | -1.4 | done | can't tell from luck |
| value_ev10 | 1427 | 37.8 | 39.1 | $-951.09 | -6.7% | $48.91 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2598 | 49.8 | 49.4 | $-1061.73 | -4.1% | $-61.73 | -2.1 | done | losing for real |
| value_ev5 | 2163 | 39.9 | 41.0 | $-1326.06 | -6.1% | $-326.06 | -2.4 | done | losing for real |
| trend_filter | 1809 | 49.3 | 50.4 | $-1335.44 | -7.4% | $-335.44 | -3.2 | done | losing for real |
| coinflip | 4420 | 50.5 | 50.2 | $-1702.07 | -3.9% | $-702.07 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2598 | 50.2 | 51.1 | $-1710.29 | -6.6% | $-710.29 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3087 | 48.8 | 50.2 | $-2112.84 | -6.8% | $-1112.84 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4420 | 50.7 | 51.4 | $-2315.48 | -5.2% | $-1315.48 | -3.6 | done | losing for real |
| always_up | 4420 | 47.5 | 49.3 | $-3607.11 | -8.2% | $-2607.11 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7008 | 48.4 | 49.0 | $-3491.26 |
| ETH | 7580 | 48.1 | 48.4 | $-4568.49 |
| SOL | 7969 | 48.1 | 48.4 | $-4490.59 |
| XRP | 8055 | 48.2 | 48.2 | $-4740.43 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
