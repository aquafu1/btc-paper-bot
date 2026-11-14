# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 3:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 365 windows, 9864 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 189 | 38.1 | 36.4 | $+15.78 | +0.8% | $1015.78 | +0.1 | Sat 9:00 PM | too few trades (189/200) |
| value_ev10 | 478 | 41.2 | 40.3 | $-52.64 | -1.1% | $947.36 | -0.2 | done | can't tell from luck |
| value_ev5 | 707 | 42.4 | 42.0 | $-178.96 | -2.5% | $821.04 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 811 | 49.4 | 49.7 | $-395.81 | -4.9% | $604.19 | -1.4 | done | can't tell from luck |
| trend_filter | 548 | 48.9 | 50.5 | $-402.24 | -7.3% | $597.76 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 979 | 51.6 | 52.1 | $-481.61 | -4.9% | $518.39 | -1.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 811 | 50.6 | 52.0 | $-537.12 | -6.6% | $462.88 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 979 | 48.4 | 49.6 | $-583.24 | -6.0% | $416.76 | -1.9 | done | can't tell from luck |
| coinflip | 1454 | 50.0 | 50.8 | $-752.18 | -5.2% | $247.82 | -2.0 | done | losing for real |
| momentum_5m_0.00pct | 1454 | 49.6 | 51.5 | $-1043.79 | -7.2% | $-43.79 | -2.8 | done | losing for real |
| always_up | 1454 | 45.7 | 50.7 | $-1947.41 | -13.4% | $-947.41 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2219 | 47.3 | 49.3 | $-1743.31 |
| ETH | 2484 | 47.7 | 48.8 | $-1695.98 |
| SOL | 2553 | 48.1 | 49.4 | $-1725.56 |
| XRP | 2608 | 48.9 | 49.1 | $-1194.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
