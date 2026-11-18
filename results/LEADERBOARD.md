# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 5:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 759 windows, 20930 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 394 | 33.8 | 34.9 | $-291.45 | -7.4% | $708.55 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2138 | 51.5 | 50.6 | $-505.16 | -2.4% | $494.84 | -1.1 | done | can't tell from luck |
| value_ev10 | 959 | 38.0 | 39.1 | $-617.58 | -6.4% | $382.42 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1769 | 50.0 | 49.6 | $-680.22 | -3.8% | $319.78 | -1.6 | done | can't tell from luck |
| value_ev5 | 1446 | 40.2 | 41.1 | $-816.64 | -5.6% | $183.36 | -1.8 | done | can't tell from luck |
| trend_filter | 1230 | 49.8 | 50.9 | $-825.35 | -6.7% | $174.65 | -2.4 | done | losing for real |
| coinflip | 3029 | 50.4 | 50.3 | $-1146.67 | -3.8% | $-146.67 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1769 | 50.0 | 51.2 | $-1216.22 | -6.9% | $-216.22 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2138 | 48.5 | 50.2 | $-1566.29 | -7.3% | $-566.29 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3029 | 50.8 | 51.7 | $-1667.80 | -5.5% | $-667.80 | -3.1 | done | losing for real |
| always_up | 3029 | 47.0 | 49.7 | $-2875.60 | -9.5% | $-1875.60 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4742 | 48.1 | 49.1 | $-2937.82 |
| ETH | 5217 | 48.0 | 48.6 | $-3483.86 |
| SOL | 5455 | 48.0 | 48.6 | $-3278.39 |
| XRP | 5516 | 48.6 | 48.5 | $-2508.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
