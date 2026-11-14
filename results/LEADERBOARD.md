# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 10:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 298 windows, 7937 settled trades, 64 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 788 | 53.3 | 51.8 | $-127.39 | -1.6% | $872.61 | -0.5 | done | can't tell from luck |
| value_ev20 | 148 | 35.1 | 36.5 | $-134.69 | -9.1% | $865.31 | -0.9 | Sun 2:15 AM | too few trades (148/200) |
| reversal_60m_0.30pct | 642 | 51.9 | 51.8 | $-282.84 | -4.4% | $717.16 | -1.2 | done | can't tell from luck |
| value_ev10 | 383 | 38.4 | 40.5 | $-361.48 | -9.4% | $638.52 | -1.6 | done | can't tell from luck |
| trend_filter | 432 | 47.0 | 50.3 | $-483.62 | -11.2% | $516.38 | -2.4 | done | losing for real |
| value_ev5 | 562 | 40.0 | 42.1 | $-532.73 | -9.5% | $467.27 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 642 | 48.1 | 49.8 | $-534.60 | -8.3% | $465.40 | -2.2 | done | losing for real |
| coinflip | 1184 | 50.3 | 50.9 | $-636.04 | -5.4% | $363.96 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 788 | 46.7 | 49.9 | $-828.94 | -10.5% | $171.06 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1184 | 49.4 | 51.4 | $-936.89 | -7.9% | $63.11 | -2.8 | done | losing for real |
| always_up | 1184 | 47.0 | 50.3 | $-1276.63 | -10.8% | $-276.63 | -3.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1773 | 46.8 | 49.4 | $-1632.56 |
| ETH | 1988 | 47.2 | 48.7 | $-1807.87 |
| SOL | 2061 | 48.3 | 49.3 | $-1552.59 |
| XRP | 2115 | 48.7 | 49.0 | $-1142.82 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
