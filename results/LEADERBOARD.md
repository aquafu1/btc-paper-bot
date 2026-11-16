# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 5:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 519 windows, 14316 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1221 | 51.2 | 49.8 | $-192.81 | -1.6% | $807.19 | -0.6 | done | can't tell from luck |
| value_ev20 | 268 | 34.3 | 35.5 | $-194.82 | -7.3% | $805.18 | -0.9 | done | can't tell from luck |
| value_ev10 | 668 | 38.0 | 39.7 | $-516.88 | -7.7% | $483.12 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1451 | 49.8 | 49.6 | $-567.89 | -3.9% | $432.11 | -1.5 | done | can't tell from luck |
| trend_filter | 840 | 49.4 | 50.7 | $-577.53 | -6.9% | $422.47 | -2.0 | done | losing for real |
| value_ev5 | 992 | 39.9 | 41.5 | $-731.77 | -7.4% | $268.23 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1451 | 50.2 | 51.6 | $-987.37 | -6.8% | $12.63 | -2.7 | done | losing for real |
| coinflip | 2068 | 50.0 | 50.7 | $-1098.58 | -5.3% | $-98.58 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1221 | 48.8 | 51.4 | $-1137.24 | -9.3% | $-137.24 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 2068 | 49.4 | 51.6 | $-1663.33 | -8.0% | $-663.33 | -3.8 | done | losing for real |
| always_up | 2068 | 46.6 | 50.1 | $-2306.27 | -11.2% | $-1306.27 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3237 | 47.3 | 49.2 | $-2666.20 |
| ETH | 3576 | 48.0 | 48.7 | $-2379.68 |
| SOL | 3731 | 47.6 | 49.0 | $-2742.36 |
| XRP | 3772 | 48.4 | 48.8 | $-2186.24 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
