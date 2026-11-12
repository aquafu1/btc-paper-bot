# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 8:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 108 windows, 2773 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 213 | 60.1 | 53.0 | $+234.36 | +11.0% | $1234.36 | +1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 268 | 55.6 | 51.9 | $+127.29 | +4.7% | $1127.29 | +0.8 | done | can't tell from luck |
| momentum_5m_0.00pct | 425 | 53.2 | 50.8 | $+39.20 | +0.9% | $1039.20 | +0.2 | done | can't tell from luck |
| value_ev10 | 144 | 39.6 | 40.7 | $-102.04 | -7.1% | $897.96 | -0.7 | Thu 8:00 AM | too few trades (144/200) |
| value_ev20 | 50 | 28.0 | 36.5 | $-123.85 | -24.8% | $876.15 | -1.4 | Sun 12:15 PM | too few trades (50/200) |
| trend_filter | 144 | 42.4 | 49.0 | $-238.60 | -16.6% | $761.40 | -2.0 | Thu 8:00 AM | too few trades (144/200) |
| coinflip | 425 | 50.1 | 51.3 | $-262.18 | -6.2% | $737.82 | -1.3 | done | can't tell from luck |
| value_ev5 | 198 | 37.4 | 42.0 | $-284.27 | -14.4% | $715.73 | -1.8 | Wed 9:00 PM | too few trades (198/200) |
| momentum_15m_0.10pct | 268 | 44.4 | 50.2 | $-388.79 | -14.5% | $611.21 | -2.4 | done | losing for real |
| always_up | 425 | 47.3 | 50.3 | $-405.51 | -9.5% | $594.49 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 213 | 39.9 | 49.1 | $-449.02 | -21.1% | $550.98 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 603 | 46.1 | 49.7 | $-502.24 |
| ETH | 672 | 45.8 | 48.9 | $-612.23 |
| SOL | 741 | 48.6 | 48.6 | $-445.09 |
| XRP | 757 | 50.3 | 49.2 | $-293.85 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
