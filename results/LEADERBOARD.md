# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 9:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 292 windows, 7751 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 765 | 54.0 | 51.9 | $-35.89 | -0.5% | $964.11 | -0.1 | done | can't tell from luck |
| value_ev20 | 146 | 35.6 | 36.4 | $-114.69 | -7.9% | $885.31 | -0.7 | Sun 2:00 AM | too few trades (146/200) |
| reversal_60m_0.30pct | 623 | 52.3 | 51.9 | $-225.92 | -3.6% | $774.08 | -0.9 | done | can't tell from luck |
| value_ev10 | 377 | 38.5 | 40.4 | $-343.14 | -9.1% | $656.86 | -1.5 | done | can't tell from luck |
| trend_filter | 417 | 46.8 | 50.1 | $-471.97 | -11.3% | $528.03 | -2.4 | done | losing for real |
| value_ev5 | 552 | 40.0 | 42.1 | $-511.67 | -9.3% | $488.33 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 623 | 47.7 | 49.7 | $-560.68 | -9.0% | $439.32 | -2.3 | done | losing for real |
| coinflip | 1161 | 50.1 | 50.9 | $-661.69 | -5.7% | $338.31 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 765 | 46.0 | 49.7 | $-886.11 | -11.6% | $113.89 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1161 | 49.4 | 51.3 | $-899.38 | -7.7% | $100.62 | -2.7 | done | losing for real |
| always_up | 1161 | 47.5 | 50.3 | $-1141.45 | -9.8% | $-141.45 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1733 | 46.8 | 49.3 | $-1574.54 |
| ETH | 1933 | 47.3 | 48.7 | $-1682.79 |
| SOL | 2014 | 48.3 | 49.3 | $-1533.44 |
| XRP | 2071 | 48.8 | 49.0 | $-1061.84 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
