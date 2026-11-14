# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 4:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 322 windows, 8624 settled trades, 38 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 700 | 53.3 | 51.7 | $-84.58 | -1.2% | $915.42 | -0.3 | done | can't tell from luck |
| value_ev20 | 163 | 33.7 | 36.8 | $-212.09 | -13.0% | $787.91 | -1.3 | Sat 11:45 PM | too few trades (163/200) |
| reversal_15m_0.10pct | 857 | 52.9 | 52.0 | $-218.21 | -2.5% | $781.79 | -0.8 | done | can't tell from luck |
| value_ev10 | 413 | 37.8 | 40.5 | $-449.41 | -10.9% | $550.59 | -1.9 | done | can't tell from luck |
| value_ev5 | 618 | 39.5 | 42.2 | $-659.40 | -10.7% | $340.60 | -2.3 | done | losing for real |
| trend_filter | 476 | 45.0 | 50.4 | $-718.15 | -15.1% | $281.85 | -3.4 | done | losing for real |
| momentum_60m_0.30pct | 700 | 46.7 | 49.9 | $-776.76 | -11.1% | $223.24 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 857 | 47.1 | 49.8 | $-812.10 | -9.5% | $187.90 | -2.8 | done | losing for real |
| coinflip | 1280 | 49.8 | 51.0 | $-823.75 | -6.4% | $176.25 | -2.4 | done | losing for real |
| always_up | 1280 | 47.7 | 50.5 | $-1253.27 | -9.8% | $-253.27 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 1280 | 48.4 | 51.4 | $-1261.09 | -9.9% | $-261.09 | -3.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1932 | 46.2 | 49.3 | $-2045.70 |
| ETH | 2166 | 46.7 | 48.8 | $-2163.49 |
| SOL | 2245 | 48.1 | 49.4 | $-1773.06 |
| XRP | 2281 | 48.7 | 49.2 | $-1286.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
