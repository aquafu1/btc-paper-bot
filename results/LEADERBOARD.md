# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 7:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 333 windows, 8869 settled trades, 69 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 706 | 53.4 | 51.7 | $-65.73 | -0.9% | $934.27 | -0.3 | done | can't tell from luck |
| value_ev20 | 175 | 36.0 | 36.6 | $-103.62 | -5.9% | $896.38 | -0.6 | Sat 7:45 PM | too few trades (175/200) |
| reversal_15m_0.10pct | 878 | 52.8 | 51.9 | $-219.39 | -2.5% | $780.61 | -0.8 | done | can't tell from luck |
| value_ev10 | 431 | 38.5 | 40.3 | $-353.92 | -8.2% | $646.08 | -1.4 | done | can't tell from luck |
| value_ev5 | 640 | 40.3 | 42.1 | $-515.35 | -8.1% | $484.65 | -1.8 | done | can't tell from luck |
| coinflip | 1324 | 50.2 | 50.9 | $-724.93 | -5.5% | $275.07 | -2.0 | done | losing for real |
| trend_filter | 483 | 44.9 | 50.3 | $-738.73 | -15.3% | $261.27 | -3.5 | done | losing for real |
| momentum_60m_0.30pct | 706 | 46.6 | 50.0 | $-805.92 | -11.4% | $194.08 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 878 | 47.2 | 49.8 | $-837.16 | -9.5% | $162.84 | -2.9 | done | losing for real |
| always_up | 1324 | 47.6 | 50.3 | $-1239.62 | -9.4% | $-239.62 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 1324 | 48.3 | 51.3 | $-1274.05 | -9.6% | $-274.05 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1976 | 46.7 | 49.3 | $-1835.48 |
| ETH | 2223 | 47.1 | 48.7 | $-1884.93 |
| SOL | 2317 | 47.8 | 49.3 | $-1864.36 |
| XRP | 2353 | 48.6 | 49.0 | $-1293.63 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
