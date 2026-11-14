# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 9:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 292 windows, 7743 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 764 | 54.1 | 51.9 | $-25.89 | -0.3% | $974.11 | -0.1 | done | can't tell from luck |
| value_ev20 | 146 | 35.6 | 36.4 | $-114.69 | -7.9% | $885.31 | -0.7 | Sun 1:30 AM | too few trades (146/200) |
| reversal_60m_0.30pct | 622 | 52.3 | 51.9 | $-233.84 | -3.8% | $766.16 | -1.0 | done | can't tell from luck |
| value_ev10 | 377 | 38.5 | 40.4 | $-343.14 | -9.1% | $656.86 | -1.5 | done | can't tell from luck |
| trend_filter | 416 | 46.9 | 50.1 | $-461.97 | -11.1% | $538.03 | -2.3 | done | losing for real |
| value_ev5 | 552 | 40.0 | 42.1 | $-511.67 | -9.3% | $488.33 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 622 | 47.7 | 49.7 | $-550.68 | -8.9% | $449.32 | -2.2 | done | losing for real |
| coinflip | 1160 | 50.2 | 50.9 | $-651.69 | -5.6% | $348.31 | -2.0 | done | can't tell from luck |
| momentum_5m_0.00pct | 1160 | 49.5 | 51.3 | $-889.38 | -7.7% | $110.62 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 764 | 45.9 | 49.7 | $-894.03 | -11.7% | $105.97 | -3.3 | done | losing for real |
| always_up | 1160 | 47.4 | 50.3 | $-1149.37 | -9.9% | $-149.37 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1725 | 46.8 | 49.3 | $-1548.30 |
| ETH | 1933 | 47.3 | 48.7 | $-1682.79 |
| SOL | 2014 | 48.3 | 49.3 | $-1533.44 |
| XRP | 2071 | 48.8 | 49.0 | $-1061.84 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
