# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 6:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 148 windows, 3733 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 260 | 60.4 | 53.1 | $+296.73 | +11.4% | $1296.73 | +2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 359 | 56.0 | 52.2 | $+167.82 | +4.7% | $1167.82 | +0.9 | done | can't tell from luck |
| momentum_5m_0.00pct | 584 | 53.1 | 51.4 | $-55.44 | -0.9% | $944.56 | -0.2 | done | can't tell from luck |
| value_ev20 | 74 | 32.4 | 37.2 | $-143.54 | -19.4% | $856.46 | -1.4 | Sun 12:45 AM | too few trades (74/200) |
| coinflip | 584 | 51.4 | 50.9 | $-226.39 | -3.9% | $773.61 | -1.0 | done | can't tell from luck |
| value_ev10 | 195 | 37.4 | 40.7 | $-252.43 | -12.9% | $747.57 | -1.6 | Thu 7:15 AM | too few trades (195/200) |
| trend_filter | 189 | 42.3 | 49.3 | $-327.78 | -17.3% | $672.22 | -2.4 | Thu 8:45 AM | too few trades (189/200) |
| value_ev5 | 285 | 38.6 | 42.3 | $-379.73 | -13.3% | $620.27 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 359 | 44.0 | 50.1 | $-540.91 | -15.1% | $459.09 | -2.9 | done | losing for real |
| momentum_60m_0.30pct | 260 | 39.6 | 49.3 | $-570.07 | -21.9% | $429.93 | -3.6 | done | losing for real |
| always_up | 584 | 46.2 | 49.9 | $-697.15 | -11.9% | $302.85 | -3.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 798 | 46.0 | 49.6 | $-796.32 |
| ETH | 923 | 45.6 | 48.8 | $-986.44 |
| SOL | 982 | 48.6 | 48.8 | $-672.88 |
| XRP | 1030 | 50.6 | 49.1 | $-273.26 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
