# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 4:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 274 windows, 7207 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 708 | 54.8 | 52.3 | $+72.88 | +1.0% | $1072.88 | +0.3 | done | can't tell from luck |
| value_ev20 | 130 | 36.2 | 36.9 | $-85.65 | -6.6% | $914.35 | -0.6 | Sun 8:00 AM | too few trades (130/200) |
| reversal_60m_0.30pct | 578 | 52.1 | 52.3 | $-250.22 | -4.3% | $749.78 | -1.1 | done | can't tell from luck |
| value_ev10 | 348 | 38.5 | 40.8 | $-320.17 | -9.2% | $679.83 | -1.5 | done | can't tell from luck |
| trend_filter | 379 | 47.0 | 50.1 | $-410.31 | -10.8% | $589.69 | -2.1 | done | losing for real |
| value_ev5 | 511 | 40.5 | 42.4 | $-434.03 | -8.5% | $565.97 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 578 | 47.9 | 49.6 | $-476.48 | -8.2% | $523.52 | -2.0 | done | losing for real |
| coinflip | 1089 | 49.8 | 50.9 | $-688.24 | -6.3% | $311.76 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1089 | 49.9 | 51.4 | $-773.21 | -7.1% | $226.79 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 708 | 45.2 | 49.7 | $-912.66 | -12.9% | $87.34 | -3.5 | done | losing for real |
| always_up | 1089 | 47.0 | 50.2 | $-1146.12 | -10.5% | $-146.12 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1618 | 46.8 | 49.5 | $-1524.72 |
| ETH | 1796 | 46.9 | 49.0 | $-1749.58 |
| SOL | 1862 | 48.5 | 49.3 | $-1309.53 |
| XRP | 1931 | 49.0 | 49.1 | $-840.39 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
