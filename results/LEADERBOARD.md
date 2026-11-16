# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 11:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 543 windows, 15071 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1291 | 51.6 | 49.7 | $-162.00 | -1.3% | $838.00 | -0.5 | done | can't tell from luck |
| value_ev20 | 292 | 33.2 | 35.2 | $-332.64 | -11.4% | $667.36 | -1.5 | done | can't tell from luck |
| trend_filter | 879 | 50.9 | 50.9 | $-415.22 | -4.7% | $584.78 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1527 | 49.8 | 49.7 | $-663.03 | -4.3% | $336.97 | -1.7 | done | can't tell from luck |
| value_ev10 | 710 | 36.9 | 39.4 | $-780.63 | -11.0% | $219.37 | -2.4 | done | losing for real |
| value_ev5 | 1056 | 39.2 | 41.3 | $-994.23 | -9.4% | $5.77 | -2.6 | done | losing for real |
| reversal_15m_0.10pct | 1527 | 50.2 | 51.2 | $-1094.54 | -7.2% | $-94.54 | -2.9 | done | losing for real |
| coinflip | 2166 | 49.9 | 50.6 | $-1285.88 | -5.9% | $-285.88 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1291 | 48.4 | 51.2 | $-1355.40 | -10.5% | $-355.40 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 2166 | 50.2 | 51.7 | $-1538.04 | -7.1% | $-538.04 | -3.4 | done | losing for real |
| always_up | 2166 | 46.8 | 50.1 | $-2439.08 | -11.3% | $-1439.08 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3411 | 47.5 | 49.2 | $-2837.02 |
| ETH | 3757 | 47.9 | 48.6 | $-2697.83 |
| SOL | 3937 | 47.7 | 48.7 | $-3100.75 |
| XRP | 3966 | 48.5 | 48.7 | $-2425.08 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
