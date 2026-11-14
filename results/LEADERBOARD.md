# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 7:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 334 windows, 8906 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 177 | 36.7 | 36.6 | $-73.87 | -4.2% | $926.13 | -0.4 | Sat 6:45 PM | too few trades (177/200) |
| reversal_60m_0.30pct | 710 | 53.1 | 51.7 | $-105.73 | -1.5% | $894.27 | -0.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 881 | 52.7 | 52.0 | $-249.39 | -2.8% | $750.61 | -0.9 | done | can't tell from luck |
| value_ev10 | 433 | 38.8 | 40.3 | $-324.17 | -7.5% | $675.83 | -1.3 | done | can't tell from luck |
| value_ev5 | 643 | 40.6 | 42.0 | $-471.16 | -7.3% | $528.84 | -1.6 | done | can't tell from luck |
| trend_filter | 487 | 45.4 | 50.3 | $-683.95 | -14.0% | $316.05 | -3.2 | done | losing for real |
| coinflip | 1328 | 50.2 | 50.9 | $-694.59 | -5.2% | $305.41 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 710 | 46.9 | 49.9 | $-751.14 | -10.6% | $248.86 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 881 | 47.3 | 49.8 | $-796.82 | -9.0% | $203.18 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 1328 | 48.5 | 51.2 | $-1219.27 | -9.2% | $-219.27 | -3.5 | done | losing for real |
| always_up | 1328 | 47.4 | 50.3 | $-1279.62 | -9.6% | $-279.62 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1987 | 46.8 | 49.3 | $-1733.22 |
| ETH | 2234 | 47.3 | 48.7 | $-1809.19 |
| SOL | 2324 | 47.8 | 49.3 | $-1836.61 |
| XRP | 2361 | 48.7 | 49.1 | $-1270.70 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
