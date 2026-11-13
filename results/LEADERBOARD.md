# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 3:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 268 windows, 7024 settled trades, 34 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 692 | 55.1 | 52.3 | $+91.64 | +1.3% | $1091.64 | +0.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 559 | 53.1 | 52.3 | $-136.75 | -2.4% | $863.25 | -0.6 | done | can't tell from luck |
| value_ev20 | 123 | 33.3 | 36.6 | $-148.76 | -12.1% | $851.24 | -1.0 | Sun 12:00 PM | too few trades (123/200) |
| value_ev10 | 335 | 37.0 | 40.7 | $-409.76 | -12.2% | $590.24 | -1.9 | done | can't tell from luck |
| trend_filter | 364 | 45.9 | 50.1 | $-467.34 | -12.8% | $532.66 | -2.5 | done | losing for real |
| value_ev5 | 496 | 39.5 | 42.4 | $-523.79 | -10.6% | $476.21 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 559 | 46.9 | 49.6 | $-580.79 | -10.4% | $419.21 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 1068 | 49.8 | 51.4 | $-770.24 | -7.2% | $229.76 | -2.5 | done | losing for real |
| coinflip | 1068 | 49.3 | 50.9 | $-793.89 | -7.4% | $206.11 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 692 | 44.9 | 49.7 | $-920.94 | -13.3% | $79.06 | -3.5 | done | losing for real |
| always_up | 1068 | 47.6 | 50.2 | $-1012.65 | -9.5% | $-12.65 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1564 | 46.4 | 49.6 | $-1637.52 |
| ETH | 1754 | 46.8 | 49.0 | $-1756.66 |
| SOL | 1818 | 48.2 | 49.3 | $-1387.71 |
| XRP | 1888 | 48.9 | 49.1 | $-891.40 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
