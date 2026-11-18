# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 8:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 722 windows, 19864 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 379 | 33.5 | 34.9 | $-314.03 | -8.3% | $685.97 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 2035 | 51.6 | 50.8 | $-509.40 | -2.5% | $490.60 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1663 | 50.0 | 49.5 | $-582.73 | -3.5% | $417.27 | -1.4 | done | can't tell from luck |
| value_ev10 | 912 | 38.0 | 39.1 | $-592.90 | -6.5% | $407.10 | -1.6 | done | can't tell from luck |
| value_ev5 | 1375 | 40.7 | 41.1 | $-656.89 | -4.8% | $343.11 | -1.5 | done | can't tell from luck |
| trend_filter | 1162 | 50.3 | 50.9 | $-658.12 | -5.7% | $341.88 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 1663 | 50.0 | 51.3 | $-1199.56 | -7.2% | $-199.56 | -3.0 | done | losing for real |
| coinflip | 2880 | 50.2 | 50.3 | $-1261.14 | -4.4% | $-261.14 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 2880 | 51.1 | 51.8 | $-1422.09 | -4.9% | $-422.09 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2035 | 48.4 | 50.0 | $-1453.92 | -7.1% | $-453.92 | -3.2 | done | losing for real |
| always_up | 2880 | 47.2 | 49.5 | $-2560.23 | -8.9% | $-1560.23 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4496 | 48.1 | 49.1 | $-2799.44 |
| ETH | 4946 | 48.2 | 48.5 | $-2971.58 |
| SOL | 5176 | 48.2 | 48.7 | $-3023.31 |
| XRP | 5246 | 48.6 | 48.4 | $-2416.67 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
