# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 11:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 687 windows, 19035 settled trades, 33 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 361 | 34.3 | 34.9 | $-223.12 | -6.2% | $776.88 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1606 | 50.4 | 49.6 | $-429.87 | -2.7% | $570.13 | -1.1 | done | can't tell from luck |
| value_ev10 | 879 | 38.5 | 39.2 | $-499.28 | -5.7% | $500.72 | -1.4 | done | can't tell from luck |
| trend_filter | 1111 | 50.4 | 50.9 | $-593.14 | -5.3% | $406.86 | -1.8 | done | can't tell from luck |
| value_ev5 | 1322 | 40.8 | 41.1 | $-599.40 | -4.5% | $400.60 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1959 | 51.4 | 50.8 | $-613.33 | -3.1% | $386.67 | -1.4 | done | can't tell from luck |
| coinflip | 2744 | 50.1 | 50.3 | $-1184.36 | -4.3% | $-184.36 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1606 | 49.6 | 51.3 | $-1258.69 | -7.8% | $-258.69 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1959 | 48.6 | 49.9 | $-1286.90 | -6.6% | $-286.90 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 2744 | 50.8 | 51.8 | $-1528.71 | -5.6% | $-528.71 | -3.0 | done | losing for real |
| always_up | 2744 | 47.6 | 49.6 | $-2269.90 | -8.3% | $-1269.90 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4325 | 48.3 | 49.1 | $-2482.60 |
| ETH | 4740 | 48.3 | 48.6 | $-2804.90 |
| SOL | 4962 | 48.2 | 48.6 | $-2842.56 |
| XRP | 5008 | 48.6 | 48.4 | $-2356.63 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
