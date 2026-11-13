# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 9:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 244 windows, 6369 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 628 | 56.4 | 52.3 | $+249.37 | +4.0% | $1249.37 | +1.1 | done | can't tell from luck |
| reversal_60m_0.30pct | 501 | 54.9 | 52.3 | $+64.01 | +1.3% | $1064.01 | +0.3 | done | can't tell from luck |
| value_ev20 | 114 | 34.2 | 36.7 | $-120.27 | -10.6% | $879.73 | -0.9 | Sun 10:15 AM | too few trades (114/200) |
| value_ev10 | 309 | 37.2 | 40.9 | $-383.26 | -12.4% | $616.74 | -1.9 | done | can't tell from luck |
| trend_filter | 333 | 44.4 | 50.3 | $-510.59 | -15.3% | $489.41 | -2.9 | done | losing for real |
| value_ev5 | 451 | 39.2 | 42.5 | $-516.70 | -11.5% | $483.30 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 501 | 45.1 | 49.8 | $-678.70 | -13.5% | $321.30 | -3.1 | done | losing for real |
| coinflip | 968 | 49.4 | 50.9 | $-709.14 | -7.3% | $290.86 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 968 | 49.7 | 51.5 | $-735.13 | -7.6% | $264.87 | -2.5 | done | losing for real |
| always_up | 968 | 47.5 | 50.6 | $-993.69 | -10.3% | $6.31 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 628 | 43.6 | 49.8 | $-1008.87 | -16.1% | $-8.87 | -4.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1424 | 46.3 | 49.8 | $-1508.26 |
| ETH | 1587 | 46.5 | 49.1 | $-1665.13 |
| SOL | 1644 | 48.2 | 49.4 | $-1286.20 |
| XRP | 1714 | 48.8 | 49.2 | $-883.39 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
