# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 8:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 108 windows, 2768 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 213 | 60.1 | 53.0 | $+234.36 | +11.0% | $1234.36 | +1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 267 | 55.8 | 51.9 | $+137.29 | +5.1% | $1137.29 | +0.9 | done | can't tell from luck |
| momentum_5m_0.00pct | 424 | 53.1 | 50.8 | $+29.90 | +0.7% | $1029.90 | +0.1 | done | can't tell from luck |
| value_ev10 | 144 | 39.6 | 40.7 | $-102.04 | -7.1% | $897.96 | -0.7 | Thu 7:45 AM | too few trades (144/200) |
| value_ev20 | 50 | 28.0 | 36.5 | $-123.85 | -24.8% | $876.15 | -1.4 | Sun 11:15 AM | too few trades (50/200) |
| trend_filter | 144 | 42.4 | 49.0 | $-238.60 | -16.6% | $761.40 | -2.0 | Thu 7:45 AM | too few trades (144/200) |
| coinflip | 424 | 50.0 | 51.3 | $-271.48 | -6.4% | $728.52 | -1.4 | done | can't tell from luck |
| value_ev5 | 198 | 37.4 | 42.0 | $-284.27 | -14.4% | $715.73 | -1.8 | Wed 8:45 PM | too few trades (198/200) |
| momentum_15m_0.10pct | 267 | 44.2 | 50.2 | $-398.09 | -14.9% | $601.91 | -2.5 | done | losing for real |
| always_up | 424 | 47.2 | 50.3 | $-414.81 | -9.8% | $585.19 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 213 | 39.9 | 49.1 | $-449.02 | -21.1% | $550.98 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 598 | 45.8 | 49.7 | $-529.44 |
| ETH | 672 | 45.8 | 48.9 | $-612.23 |
| SOL | 741 | 48.6 | 48.6 | $-445.09 |
| XRP | 757 | 50.3 | 49.2 | $-293.85 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
