# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 5:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 758 windows, 20893 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 394 | 33.8 | 34.9 | $-291.45 | -7.4% | $708.55 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2133 | 51.6 | 50.6 | $-455.16 | -2.1% | $544.84 | -1.0 | done | can't tell from luck |
| value_ev10 | 957 | 38.0 | 39.1 | $-597.58 | -6.2% | $402.42 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1766 | 49.9 | 49.6 | $-698.66 | -4.0% | $301.34 | -1.7 | done | can't tell from luck |
| value_ev5 | 1442 | 40.4 | 41.1 | $-776.64 | -5.4% | $223.36 | -1.7 | done | can't tell from luck |
| trend_filter | 1230 | 49.8 | 50.9 | $-825.35 | -6.7% | $174.65 | -2.4 | done | losing for real |
| coinflip | 3024 | 50.4 | 50.3 | $-1128.81 | -3.7% | $-128.81 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1766 | 50.1 | 51.2 | $-1186.22 | -6.7% | $-186.22 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2133 | 48.4 | 50.2 | $-1597.98 | -7.5% | $-597.98 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 3024 | 50.9 | 51.8 | $-1617.80 | -5.3% | $-617.80 | -3.0 | done | losing for real |
| always_up | 3024 | 46.9 | 49.6 | $-2907.28 | -9.6% | $-1907.28 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4733 | 48.2 | 49.1 | $-2908.74 |
| ETH | 5211 | 48.0 | 48.6 | $-3456.51 |
| SOL | 5438 | 48.0 | 48.6 | $-3208.04 |
| XRP | 5511 | 48.6 | 48.5 | $-2509.63 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
