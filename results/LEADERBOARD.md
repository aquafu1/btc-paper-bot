# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 11:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 543 windows, 15053 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1289 | 51.7 | 49.8 | $-142.00 | -1.1% | $858.00 | -0.4 | done | can't tell from luck |
| value_ev20 | 290 | 33.4 | 35.4 | $-312.64 | -10.8% | $687.36 | -1.4 | done | can't tell from luck |
| trend_filter | 879 | 50.9 | 50.9 | $-415.22 | -4.7% | $584.78 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1526 | 49.8 | 49.7 | $-665.07 | -4.4% | $334.93 | -1.7 | done | can't tell from luck |
| value_ev10 | 708 | 37.0 | 39.5 | $-760.63 | -10.7% | $239.37 | -2.4 | done | losing for real |
| value_ev5 | 1054 | 39.3 | 41.3 | $-974.23 | -9.2% | $25.77 | -2.6 | done | losing for real |
| reversal_15m_0.10pct | 1526 | 50.2 | 51.3 | $-1084.54 | -7.1% | $-84.54 | -2.9 | done | losing for real |
| coinflip | 2164 | 49.8 | 50.6 | $-1290.25 | -6.0% | $-290.25 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1289 | 48.3 | 51.2 | $-1359.77 | -10.5% | $-359.77 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 2164 | 50.1 | 51.7 | $-1542.41 | -7.1% | $-542.41 | -3.5 | done | losing for real |
| always_up | 2164 | 46.8 | 50.1 | $-2419.08 | -11.2% | $-1419.08 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3411 | 47.5 | 49.2 | $-2837.02 |
| ETH | 3757 | 47.9 | 48.6 | $-2697.83 |
| SOL | 3927 | 47.7 | 48.8 | $-3048.92 |
| XRP | 3958 | 48.5 | 48.8 | $-2382.06 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
