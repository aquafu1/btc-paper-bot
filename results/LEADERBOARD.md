# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 1:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 214 windows, 5597 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 552 | 56.3 | 52.7 | $+213.06 | +3.9% | $1213.06 | +1.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 433 | 54.7 | 52.6 | $+39.64 | +0.9% | $1039.64 | +0.2 | done | can't tell from luck |
| value_ev20 | 105 | 34.3 | 37.0 | $-126.06 | -12.0% | $873.94 | -1.0 | Sun 6:15 AM | too few trades (105/200) |
| value_ev10 | 279 | 37.3 | 40.9 | $-358.28 | -12.8% | $641.72 | -1.9 | done | can't tell from luck |
| trend_filter | 291 | 45.0 | 50.0 | $-389.07 | -13.4% | $610.93 | -2.3 | done | losing for real |
| momentum_5m_0.00pct | 849 | 50.6 | 51.5 | $-474.69 | -5.6% | $525.31 | -1.7 | done | can't tell from luck |
| value_ev5 | 405 | 39.3 | 42.6 | $-481.45 | -11.9% | $518.55 | -2.1 | done | losing for real |
| coinflip | 849 | 50.1 | 51.0 | $-508.38 | -6.0% | $491.62 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 433 | 45.3 | 49.6 | $-542.27 | -12.5% | $457.73 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 552 | 43.7 | 49.7 | $-859.80 | -15.6% | $140.20 | -3.7 | done | losing for real |
| always_up | 849 | 46.6 | 50.2 | $-956.77 | -11.3% | $43.23 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1244 | 46.2 | 49.7 | $-1272.92 |
| ETH | 1401 | 46.5 | 48.9 | $-1321.17 |
| SOL | 1441 | 48.0 | 49.3 | $-1189.62 |
| XRP | 1511 | 49.5 | 49.3 | $-660.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
