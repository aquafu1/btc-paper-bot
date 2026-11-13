# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 8:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 242 windows, 6315 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 623 | 56.2 | 52.3 | $+230.09 | +3.7% | $1230.09 | +1.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 496 | 55.0 | 52.4 | $+70.38 | +1.4% | $1070.38 | +0.3 | done | can't tell from luck |
| value_ev20 | 114 | 34.2 | 36.7 | $-120.27 | -10.6% | $879.73 | -0.9 | Sun 9:30 AM | too few trades (114/200) |
| value_ev10 | 306 | 37.6 | 40.8 | $-353.26 | -11.5% | $646.74 | -1.7 | done | can't tell from luck |
| trend_filter | 331 | 44.7 | 50.3 | $-490.59 | -14.8% | $509.41 | -2.8 | done | losing for real |
| value_ev5 | 446 | 39.2 | 42.5 | $-510.33 | -11.4% | $489.67 | -2.1 | done | losing for real |
| coinflip | 960 | 49.7 | 50.9 | $-645.61 | -6.7% | $354.39 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 496 | 45.0 | 49.7 | $-677.93 | -13.7% | $322.07 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 960 | 49.9 | 51.6 | $-698.02 | -7.3% | $301.98 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 623 | 43.8 | 49.9 | $-977.81 | -15.7% | $22.19 | -4.0 | done | losing for real |
| always_up | 960 | 47.4 | 50.5 | $-997.85 | -10.4% | $2.15 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1413 | 46.4 | 49.7 | $-1471.97 |
| ETH | 1575 | 46.6 | 49.0 | $-1618.52 |
| SOL | 1629 | 48.2 | 49.4 | $-1273.90 |
| XRP | 1698 | 49.0 | 49.2 | $-806.80 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
