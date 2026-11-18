# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 12:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 739 windows, 20404 settled trades, 24 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 385 | 33.2 | 34.9 | $-352.66 | -9.2% | $647.34 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2088 | 51.7 | 50.7 | $-450.07 | -2.2% | $549.93 | -1.0 | done | can't tell from luck |
| value_ev10 | 933 | 37.8 | 39.1 | $-649.20 | -7.0% | $350.80 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1722 | 49.9 | 49.6 | $-671.97 | -3.9% | $328.03 | -1.6 | done | can't tell from luck |
| value_ev5 | 1408 | 40.4 | 41.1 | $-772.43 | -5.5% | $227.57 | -1.7 | done | can't tell from luck |
| trend_filter | 1202 | 49.8 | 50.9 | $-807.67 | -6.7% | $192.33 | -2.4 | done | losing for real |
| coinflip | 2952 | 50.4 | 50.3 | $-1123.08 | -3.8% | $-123.08 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1722 | 50.1 | 51.3 | $-1177.56 | -6.8% | $-177.56 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2088 | 48.3 | 50.1 | $-1537.00 | -7.4% | $-537.00 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2952 | 50.7 | 51.8 | $-1669.52 | -5.7% | $-669.52 | -3.2 | done | losing for real |
| always_up | 2952 | 47.1 | 49.6 | $-2675.88 | -9.1% | $-1675.88 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4623 | 48.1 | 49.1 | $-2922.01 |
| ETH | 5086 | 48.1 | 48.6 | $-3259.39 |
| SOL | 5313 | 48.1 | 48.7 | $-3102.17 |
| XRP | 5382 | 48.5 | 48.5 | $-2603.47 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
