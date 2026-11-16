# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 10:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 539 windows, 14918 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1274 | 51.6 | 49.8 | $-132.53 | -1.0% | $867.47 | -0.4 | done | can't tell from luck |
| value_ev20 | 286 | 33.9 | 35.5 | $-272.64 | -9.5% | $727.36 | -1.2 | done | can't tell from luck |
| trend_filter | 871 | 50.6 | 50.9 | $-426.33 | -4.9% | $573.67 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1512 | 50.0 | 49.7 | $-590.49 | -3.9% | $409.51 | -1.5 | done | can't tell from luck |
| value_ev10 | 701 | 37.4 | 39.6 | $-690.63 | -9.9% | $309.37 | -2.2 | done | losing for real |
| value_ev5 | 1044 | 39.6 | 41.4 | $-896.07 | -8.6% | $103.93 | -2.4 | done | losing for real |
| reversal_15m_0.10pct | 1512 | 50.0 | 51.3 | $-1113.17 | -7.4% | $-113.17 | -2.9 | done | losing for real |
| coinflip | 2148 | 49.9 | 50.6 | $-1240.88 | -5.8% | $-240.88 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1274 | 48.4 | 51.3 | $-1311.97 | -10.3% | $-311.97 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2148 | 50.0 | 51.7 | $-1545.47 | -7.2% | $-545.47 | -3.5 | done | losing for real |
| always_up | 2148 | 46.7 | 50.1 | $-2416.63 | -11.3% | $-1416.63 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3382 | 47.5 | 49.2 | $-2766.28 |
| ETH | 3721 | 48.1 | 48.7 | $-2522.96 |
| SOL | 3890 | 47.6 | 48.9 | $-3001.89 |
| XRP | 3925 | 48.4 | 48.8 | $-2345.68 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
