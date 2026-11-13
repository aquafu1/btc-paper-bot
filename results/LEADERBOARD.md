# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 12:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 258 windows, 6769 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 673 | 55.6 | 52.2 | $+151.76 | +2.3% | $1151.76 | +0.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 542 | 53.3 | 52.2 | $-101.87 | -1.9% | $898.13 | -0.5 | done | can't tell from luck |
| value_ev20 | 119 | 33.6 | 36.7 | $-141.51 | -11.9% | $858.49 | -1.0 | Sun 11:15 AM | too few trades (119/200) |
| value_ev10 | 319 | 36.7 | 40.8 | $-425.19 | -13.3% | $574.81 | -2.0 | done | losing for real |
| trend_filter | 355 | 45.9 | 50.4 | $-475.04 | -13.4% | $524.96 | -2.6 | done | losing for real |
| value_ev5 | 474 | 39.5 | 42.4 | $-526.10 | -11.1% | $473.90 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 542 | 46.7 | 49.8 | $-602.46 | -11.1% | $397.54 | -2.6 | done | losing for real |
| coinflip | 1024 | 49.3 | 50.9 | $-771.33 | -7.5% | $228.67 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 1024 | 49.7 | 51.6 | $-811.44 | -7.9% | $188.56 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 673 | 44.4 | 49.8 | $-1001.18 | -14.9% | $-1.18 | -3.9 | done | losing for real |
| always_up | 1024 | 47.3 | 50.2 | $-1057.85 | -10.3% | $-57.85 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1512 | 46.5 | 49.6 | $-1601.63 |
| ETH | 1685 | 46.7 | 49.1 | $-1724.33 |
| SOL | 1755 | 48.1 | 49.3 | $-1418.55 |
| XRP | 1817 | 48.7 | 49.1 | $-1017.70 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
