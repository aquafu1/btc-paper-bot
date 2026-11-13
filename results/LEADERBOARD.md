# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 5:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 276 windows, 7276 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 716 | 55.0 | 52.2 | $+124.14 | +1.7% | $1124.14 | +0.5 | done | can't tell from luck |
| value_ev20 | 132 | 37.1 | 36.9 | $-49.35 | -3.7% | $950.65 | -0.3 | Sun 7:00 AM | too few trades (132/200) |
| reversal_60m_0.30pct | 584 | 52.4 | 52.2 | $-193.39 | -3.3% | $806.61 | -0.8 | done | can't tell from luck |
| value_ev10 | 353 | 39.1 | 40.8 | $-273.02 | -7.7% | $726.98 | -1.2 | done | can't tell from luck |
| value_ev5 | 516 | 40.9 | 42.4 | $-386.88 | -7.5% | $613.12 | -1.5 | done | can't tell from luck |
| trend_filter | 384 | 46.4 | 50.2 | $-460.31 | -12.0% | $539.69 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 584 | 47.6 | 49.7 | $-517.97 | -8.9% | $482.03 | -2.2 | done | losing for real |
| coinflip | 1097 | 49.9 | 50.9 | $-661.65 | -6.0% | $338.35 | -2.0 | done | losing for real |
| momentum_5m_0.00pct | 1097 | 49.6 | 51.4 | $-832.85 | -7.6% | $167.15 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 716 | 45.0 | 49.7 | $-951.81 | -13.3% | $48.19 | -3.6 | done | losing for real |
| always_up | 1097 | 47.1 | 50.2 | $-1108.48 | -10.1% | $-108.48 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1632 | 46.8 | 49.5 | $-1544.22 |
| ETH | 1816 | 47.1 | 49.0 | $-1598.68 |
| SOL | 1879 | 48.4 | 49.4 | $-1340.08 |
| XRP | 1949 | 49.0 | 49.1 | $-828.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
