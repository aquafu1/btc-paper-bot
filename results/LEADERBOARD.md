# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 6:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 149 windows, 3784 settled trades, 38 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 266 | 59.8 | 53.0 | $+269.35 | +10.1% | $1269.35 | +1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 364 | 56.6 | 52.3 | $+201.34 | +5.5% | $1201.34 | +1.1 | done | can't tell from luck |
| momentum_5m_0.00pct | 590 | 52.5 | 51.3 | $-115.44 | -2.0% | $884.56 | -0.5 | done | can't tell from luck |
| value_ev20 | 74 | 32.4 | 37.2 | $-143.54 | -19.4% | $856.46 | -1.4 | Sun 2:15 AM | too few trades (74/200) |
| coinflip | 590 | 51.0 | 50.9 | $-268.14 | -4.5% | $731.86 | -1.1 | done | can't tell from luck |
| value_ev10 | 199 | 36.7 | 40.7 | $-292.43 | -14.7% | $707.57 | -1.8 | Thu 7:00 AM | too few trades (199/200) |
| trend_filter | 191 | 41.9 | 49.2 | $-347.78 | -18.2% | $652.22 | -2.5 | Thu 8:45 AM | too few trades (191/200) |
| value_ev5 | 290 | 37.9 | 42.4 | $-429.73 | -14.8% | $570.27 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 266 | 40.2 | 49.3 | $-562.03 | -21.1% | $437.97 | -3.5 | done | losing for real |
| momentum_15m_0.10pct | 364 | 43.4 | 50.0 | $-590.91 | -16.2% | $409.09 | -3.2 | done | losing for real |
| always_up | 590 | 46.1 | 50.0 | $-724.53 | -12.3% | $275.47 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 815 | 45.8 | 49.6 | $-858.75 |
| ETH | 932 | 45.4 | 48.8 | $-1042.97 |
| SOL | 991 | 48.3 | 48.8 | $-731.03 |
| XRP | 1046 | 50.2 | 49.1 | $-371.10 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
