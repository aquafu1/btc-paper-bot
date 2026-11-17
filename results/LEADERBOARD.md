# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 3:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 607 windows, 16774 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1419 | 51.2 | 49.7 | $-193.71 | -1.4% | $806.29 | -0.5 | done | can't tell from luck |
| value_ev20 | 326 | 34.4 | 35.2 | $-234.70 | -7.2% | $765.30 | -1.0 | done | can't tell from luck |
| value_ev10 | 783 | 38.3 | 39.4 | $-528.33 | -6.7% | $471.67 | -1.6 | done | can't tell from luck |
| trend_filter | 969 | 50.3 | 51.0 | $-553.82 | -5.7% | $446.18 | -1.8 | done | can't tell from luck |
| value_ev5 | 1176 | 40.6 | 41.2 | $-662.39 | -5.6% | $337.61 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1711 | 50.7 | 50.9 | $-790.27 | -4.6% | $209.73 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1711 | 49.3 | 50.0 | $-952.55 | -5.6% | $47.45 | -2.3 | done | losing for real |
| coinflip | 2420 | 49.9 | 50.5 | $-1238.74 | -5.1% | $-238.74 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1419 | 48.8 | 51.3 | $-1346.24 | -9.5% | $-346.24 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2420 | 50.2 | 51.8 | $-1607.56 | -6.6% | $-607.56 | -3.4 | done | losing for real |
| always_up | 2420 | 47.0 | 49.8 | $-2328.53 | -9.6% | $-1328.53 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3817 | 48.0 | 49.2 | $-2521.15 |
| ETH | 4183 | 48.0 | 48.6 | $-2743.71 |
| SOL | 4360 | 47.9 | 48.7 | $-2901.09 |
| XRP | 4414 | 48.5 | 48.6 | $-2270.88 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
