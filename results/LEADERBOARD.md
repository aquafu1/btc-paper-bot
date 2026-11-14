# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 1:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 356 windows, 9592 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 186 | 37.1 | 36.6 | $-58.35 | -3.1% | $941.65 | -0.3 | Sat 8:00 PM | too few trades (186/200) |
| value_ev10 | 463 | 40.2 | 40.3 | $-191.42 | -4.1% | $808.58 | -0.7 | done | can't tell from luck |
| value_ev5 | 688 | 41.7 | 42.0 | $-320.39 | -4.7% | $679.61 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 952 | 52.2 | 52.0 | $-364.93 | -3.8% | $635.07 | -1.2 | done | can't tell from luck |
| reversal_60m_0.30pct | 787 | 51.3 | 52.0 | $-414.80 | -5.3% | $585.20 | -1.5 | done | can't tell from luck |
| trend_filter | 529 | 47.8 | 50.4 | $-500.19 | -9.5% | $499.81 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 787 | 48.7 | 49.7 | $-508.61 | -6.5% | $491.39 | -1.8 | done | can't tell from luck |
| coinflip | 1416 | 50.1 | 50.8 | $-751.06 | -5.3% | $248.94 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 952 | 47.8 | 49.7 | $-751.96 | -7.9% | $248.04 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 1416 | 49.3 | 51.5 | $-1127.58 | -8.0% | $-127.58 | -3.1 | done | losing for real |
| always_up | 1416 | 46.4 | 50.6 | $-1710.27 | -12.1% | $-710.27 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2149 | 47.2 | 49.3 | $-1773.99 |
| ETH | 2414 | 47.6 | 48.8 | $-1761.56 |
| SOL | 2487 | 48.0 | 49.4 | $-1850.96 |
| XRP | 2542 | 48.8 | 49.1 | $-1313.04 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
