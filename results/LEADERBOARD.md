# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 12:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1168 windows, 32272 settled trades, 70 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 623 | 35.0 | 35.3 | $-341.04 | -5.5% | $658.96 | -1.0 | done | can't tell from luck |
| value_ev10 | 1528 | 38.6 | 39.2 | $-772.45 | -5.1% | $227.55 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3235 | 50.8 | 50.4 | $-1076.64 | -3.3% | $-76.64 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2721 | 49.7 | 49.4 | $-1134.61 | -4.2% | $-134.61 | -2.2 | done | losing for real |
| value_ev5 | 2308 | 40.4 | 41.1 | $-1186.31 | -5.1% | $-186.31 | -2.1 | done | losing for real |
| trend_filter | 1909 | 49.0 | 50.5 | $-1490.90 | -7.8% | $-490.90 | -3.5 | done | losing for real |
| reversal_60m_0.30pct | 2721 | 50.3 | 51.1 | $-1719.62 | -6.3% | $-719.62 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3235 | 49.2 | 50.2 | $-1923.19 | -5.9% | $-923.19 | -3.4 | done | losing for real |
| coinflip | 4664 | 50.2 | 50.2 | $-2006.56 | -4.3% | $-1006.56 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 4664 | 50.2 | 51.4 | $-2846.53 | -6.1% | $-1846.53 | -4.3 | done | losing for real |
| always_up | 4664 | 47.9 | 49.3 | $-3350.65 | -7.2% | $-2350.65 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7405 | 48.3 | 49.0 | $-3789.92 |
| ETH | 8005 | 48.2 | 48.4 | $-4581.24 |
| SOL | 8395 | 48.1 | 48.4 | $-4466.44 |
| XRP | 8467 | 48.1 | 48.2 | $-5010.89 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
