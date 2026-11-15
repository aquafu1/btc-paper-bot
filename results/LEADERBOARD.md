# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 1:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 405 windows, 11085 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 199 | 36.7 | 36.5 | $-56.95 | -2.9% | $943.05 | -0.3 | Sun 1:45 AM | too few trades (199/200) |
| value_ev10 | 519 | 40.5 | 40.5 | $-174.41 | -3.4% | $825.59 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 946 | 51.0 | 49.9 | $-183.07 | -1.9% | $816.93 | -0.6 | done | can't tell from luck |
| value_ev5 | 781 | 42.1 | 42.2 | $-283.76 | -3.6% | $716.24 | -0.9 | done | can't tell from luck |
| trend_filter | 626 | 50.2 | 50.6 | $-305.23 | -4.9% | $694.77 | -1.2 | done | can't tell from luck |
| momentum_15m_0.10pct | 1116 | 49.4 | 49.9 | $-487.95 | -4.4% | $512.05 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1116 | 50.6 | 52.0 | $-711.99 | -6.4% | $288.01 | -2.2 | done | losing for real |
| coinflip | 1612 | 50.1 | 50.9 | $-816.13 | -5.1% | $183.87 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 946 | 49.0 | 52.1 | $-887.29 | -9.4% | $112.71 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1612 | 49.9 | 51.6 | $-1072.78 | -6.7% | $-72.78 | -2.8 | done | losing for real |
| always_up | 1612 | 45.8 | 50.8 | $-2089.94 | -13.0% | $-1089.94 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2503 | 47.8 | 49.5 | $-1718.67 |
| ETH | 2785 | 47.9 | 49.0 | $-1723.53 |
| SOL | 2866 | 48.0 | 49.5 | $-2139.53 |
| XRP | 2931 | 48.9 | 49.3 | $-1487.75 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
