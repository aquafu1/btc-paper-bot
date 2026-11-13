# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 8:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 242 windows, 6324 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 624 | 56.2 | 52.3 | $+237.97 | +3.8% | $1237.97 | +1.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 497 | 54.9 | 52.4 | $+60.38 | +1.2% | $1060.38 | +0.3 | done | can't tell from luck |
| value_ev20 | 114 | 34.2 | 36.7 | $-120.27 | -10.6% | $879.73 | -0.9 | Sun 9:45 AM | too few trades (114/200) |
| value_ev10 | 307 | 37.5 | 40.9 | $-363.26 | -11.8% | $636.74 | -1.8 | done | can't tell from luck |
| trend_filter | 331 | 44.7 | 50.3 | $-490.59 | -14.8% | $509.41 | -2.8 | done | losing for real |
| value_ev5 | 447 | 39.1 | 42.5 | $-520.33 | -11.6% | $479.67 | -2.2 | done | losing for real |
| coinflip | 961 | 49.6 | 50.9 | $-655.61 | -6.8% | $344.39 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 497 | 45.1 | 49.7 | $-670.05 | -13.5% | $329.95 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 961 | 49.8 | 51.6 | $-708.02 | -7.4% | $291.98 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 624 | 43.8 | 49.9 | $-987.81 | -15.8% | $12.19 | -4.0 | done | losing for real |
| always_up | 961 | 47.5 | 50.5 | $-989.97 | -10.3% | $10.03 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1413 | 46.4 | 49.7 | $-1471.97 |
| ETH | 1575 | 46.6 | 49.0 | $-1618.52 |
| SOL | 1629 | 48.2 | 49.4 | $-1273.90 |
| XRP | 1707 | 48.9 | 49.2 | $-843.16 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
