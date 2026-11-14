# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 9:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 340 windows, 9098 settled trades, 66 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 184 | 37.5 | 36.6 | $-38.35 | -2.1% | $961.65 | -0.2 | Sat 4:45 PM | too few trades (184/200) |
| reversal_60m_0.30pct | 729 | 52.7 | 51.9 | $-186.69 | -2.6% | $813.31 | -0.7 | done | can't tell from luck |
| value_ev10 | 443 | 39.1 | 40.2 | $-295.27 | -6.7% | $704.73 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 902 | 52.2 | 51.9 | $-330.13 | -3.7% | $669.87 | -1.2 | done | can't tell from luck |
| value_ev5 | 657 | 40.6 | 41.9 | $-459.71 | -7.0% | $540.29 | -1.6 | done | can't tell from luck |
| trend_filter | 496 | 46.2 | 50.2 | $-607.84 | -12.3% | $392.16 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 729 | 47.3 | 49.7 | $-672.13 | -9.2% | $327.87 | -2.5 | done | losing for real |
| coinflip | 1352 | 50.2 | 50.8 | $-689.72 | -5.1% | $310.28 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 902 | 47.8 | 49.8 | $-734.33 | -8.1% | $265.67 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 1352 | 49.0 | 51.3 | $-1124.82 | -8.3% | $-124.82 | -3.2 | done | losing for real |
| always_up | 1352 | 47.2 | 50.5 | $-1401.84 | -10.4% | $-401.84 | -3.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2036 | 47.0 | 49.2 | $-1715.24 |
| ETH | 2288 | 47.4 | 48.6 | $-1726.01 |
| SOL | 2365 | 47.9 | 49.3 | $-1845.59 |
| XRP | 2409 | 48.7 | 49.0 | $-1254.00 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
