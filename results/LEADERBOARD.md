# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 11:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 638 windows, 17644 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1493 | 51.0 | 49.6 | $-218.24 | -1.5% | $781.76 | -0.6 | done | can't tell from luck |
| value_ev20 | 333 | 34.2 | 35.3 | $-246.80 | -7.4% | $753.20 | -1.0 | done | can't tell from luck |
| trend_filter | 1019 | 50.4 | 50.8 | $-518.85 | -5.1% | $481.15 | -1.7 | done | can't tell from luck |
| value_ev10 | 812 | 38.4 | 39.5 | $-551.51 | -6.8% | $448.49 | -1.6 | done | can't tell from luck |
| value_ev5 | 1232 | 40.8 | 41.4 | $-660.01 | -5.4% | $339.99 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1815 | 51.0 | 51.0 | $-745.62 | -4.1% | $254.38 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 1815 | 49.0 | 50.0 | $-1070.98 | -5.9% | $-70.98 | -2.5 | done | losing for real |
| coinflip | 2544 | 50.1 | 50.5 | $-1197.77 | -4.7% | $-197.77 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1493 | 49.0 | 51.4 | $-1358.94 | -9.1% | $-358.94 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2544 | 50.7 | 51.7 | $-1360.55 | -5.3% | $-360.55 | -2.8 | done | losing for real |
| always_up | 2544 | 47.3 | 49.7 | $-2206.29 | -8.7% | $-1206.29 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4008 | 48.4 | 49.2 | $-2369.71 |
| ETH | 4415 | 48.3 | 48.6 | $-2594.10 |
| SOL | 4579 | 48.0 | 48.8 | $-2923.57 |
| XRP | 4642 | 48.5 | 48.5 | $-2248.16 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
