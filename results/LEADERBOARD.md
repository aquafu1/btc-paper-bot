# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 8:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 531 windows, 14663 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1248 | 51.8 | 49.9 | $-50.95 | -0.4% | $949.05 | -0.1 | done | can't tell from luck |
| value_ev20 | 279 | 34.8 | 35.6 | $-202.64 | -7.3% | $797.36 | -0.9 | done | can't tell from luck |
| trend_filter | 859 | 49.9 | 50.8 | $-501.22 | -5.8% | $498.78 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1488 | 50.0 | 49.7 | $-527.72 | -3.5% | $472.28 | -1.4 | done | can't tell from luck |
| value_ev10 | 684 | 38.0 | 39.7 | $-555.95 | -8.1% | $444.05 | -1.8 | done | can't tell from luck |
| value_ev5 | 1021 | 40.2 | 41.5 | $-719.50 | -7.0% | $280.50 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1488 | 50.0 | 51.4 | $-1065.26 | -7.2% | $-65.26 | -2.8 | done | losing for real |
| coinflip | 2116 | 49.8 | 50.6 | $-1213.52 | -5.7% | $-213.52 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1248 | 48.2 | 51.2 | $-1283.22 | -10.3% | $-283.22 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2116 | 49.5 | 51.6 | $-1669.62 | -7.9% | $-669.62 | -3.8 | done | losing for real |
| always_up | 2116 | 46.6 | 50.1 | $-2358.33 | -11.1% | $-1358.33 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3323 | 47.4 | 49.2 | $-2673.46 |
| ETH | 3655 | 48.0 | 48.7 | $-2418.82 |
| SOL | 3824 | 47.6 | 48.9 | $-2837.57 |
| XRP | 3861 | 48.4 | 48.8 | $-2218.08 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
