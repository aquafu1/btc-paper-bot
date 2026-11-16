# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 6:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 473 windows, 12968 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 238 | 35.3 | 35.9 | $-125.26 | -5.3% | $874.74 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1097 | 50.9 | 50.0 | $-271.76 | -2.5% | $728.24 | -0.8 | done | can't tell from luck |
| value_ev10 | 612 | 39.4 | 40.2 | $-324.93 | -5.3% | $675.07 | -1.1 | done | can't tell from luck |
| value_ev5 | 905 | 41.3 | 41.9 | $-447.62 | -4.9% | $552.38 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1308 | 50.0 | 50.1 | $-467.63 | -3.6% | $532.37 | -1.3 | done | can't tell from luck |
| trend_filter | 751 | 49.5 | 50.8 | $-481.85 | -6.4% | $518.15 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1308 | 50.0 | 51.4 | $-873.00 | -6.7% | $127.00 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1097 | 49.1 | 51.4 | $-945.72 | -8.6% | $54.28 | -2.9 | done | losing for real |
| coinflip | 1884 | 49.9 | 50.8 | $-1036.71 | -5.5% | $-36.71 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1884 | 49.6 | 51.7 | $-1395.64 | -7.4% | $-395.64 | -3.3 | done | losing for real |
| always_up | 1884 | 46.8 | 50.4 | $-2048.70 | -10.9% | $-1048.70 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2932 | 47.5 | 49.3 | $-2230.57 |
| ETH | 3249 | 48.1 | 48.9 | $-2098.61 |
| SOL | 3376 | 47.8 | 49.3 | $-2452.06 |
| XRP | 3411 | 48.7 | 49.1 | $-1637.58 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
