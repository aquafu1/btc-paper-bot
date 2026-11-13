# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 4:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 275 windows, 7239 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 711 | 55.0 | 52.2 | $+119.66 | +1.7% | $1119.66 | +0.5 | done | can't tell from luck |
| value_ev20 | 132 | 37.1 | 36.9 | $-49.35 | -3.7% | $950.65 | -0.3 | Sun 6:15 AM | too few trades (132/200) |
| reversal_60m_0.30pct | 581 | 52.3 | 52.2 | $-203.44 | -3.5% | $796.56 | -0.9 | done | can't tell from luck |
| value_ev10 | 351 | 39.0 | 40.8 | $-273.38 | -7.8% | $726.62 | -1.2 | done | can't tell from luck |
| value_ev5 | 514 | 40.9 | 42.4 | $-387.25 | -7.5% | $612.75 | -1.5 | done | can't tell from luck |
| trend_filter | 382 | 46.6 | 50.2 | $-440.31 | -11.5% | $559.69 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 581 | 47.7 | 49.7 | $-506.48 | -8.7% | $493.52 | -2.1 | done | losing for real |
| coinflip | 1092 | 49.7 | 50.8 | $-688.48 | -6.3% | $311.52 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1092 | 49.7 | 51.4 | $-803.21 | -7.4% | $196.79 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 711 | 45.0 | 49.7 | $-942.66 | -13.3% | $57.34 | -3.6 | done | losing for real |
| always_up | 1092 | 47.2 | 50.2 | $-1099.33 | -10.1% | $-99.33 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1618 | 46.8 | 49.5 | $-1524.72 |
| ETH | 1807 | 47.0 | 48.9 | $-1651.24 |
| SOL | 1872 | 48.5 | 49.4 | $-1307.10 |
| XRP | 1942 | 49.1 | 49.1 | $-791.19 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
