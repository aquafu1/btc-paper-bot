# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 8:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 530 windows, 14633 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1245 | 51.6 | 49.9 | $-81.25 | -0.7% | $918.75 | -0.2 | done | can't tell from luck |
| value_ev20 | 278 | 34.9 | 35.6 | $-192.64 | -6.9% | $807.36 | -0.9 | done | can't tell from luck |
| trend_filter | 856 | 49.8 | 50.8 | $-531.51 | -6.2% | $468.49 | -1.9 | done | can't tell from luck |
| value_ev10 | 682 | 38.1 | 39.7 | $-535.95 | -7.9% | $464.05 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1485 | 49.9 | 49.7 | $-558.02 | -3.8% | $441.98 | -1.4 | done | can't tell from luck |
| value_ev5 | 1018 | 40.3 | 41.5 | $-689.50 | -6.8% | $310.50 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1485 | 50.1 | 51.4 | $-1035.26 | -7.0% | $-35.26 | -2.8 | done | losing for real |
| coinflip | 2113 | 49.7 | 50.6 | $-1222.90 | -5.8% | $-222.90 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1245 | 48.4 | 51.2 | $-1253.22 | -10.1% | $-253.22 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2113 | 49.4 | 51.6 | $-1699.91 | -8.0% | $-699.91 | -3.8 | done | losing for real |
| always_up | 2113 | 46.6 | 50.1 | $-2388.62 | -11.3% | $-1388.62 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3323 | 47.4 | 49.2 | $-2673.46 |
| ETH | 3644 | 48.0 | 48.7 | $-2429.27 |
| SOL | 3814 | 47.6 | 48.9 | $-2842.16 |
| XRP | 3852 | 48.4 | 48.8 | $-2243.88 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
