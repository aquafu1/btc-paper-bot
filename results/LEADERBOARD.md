# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 4:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 371 windows, 10048 settled trades, 68 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 192 | 37.5 | 36.6 | $-14.22 | -0.7% | $985.78 | -0.1 | Sat 8:45 PM | too few trades (192/200) |
| value_ev10 | 489 | 40.7 | 40.5 | $-126.39 | -2.6% | $873.61 | -0.5 | done | can't tell from luck |
| value_ev5 | 721 | 42.0 | 42.1 | $-266.26 | -3.7% | $733.74 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 831 | 49.6 | 49.8 | $-392.37 | -4.7% | $607.63 | -1.4 | done | can't tell from luck |
| trend_filter | 554 | 48.9 | 50.5 | $-408.83 | -7.4% | $591.17 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1001 | 51.6 | 52.1 | $-483.21 | -4.8% | $516.79 | -1.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 831 | 50.4 | 52.0 | $-579.09 | -7.0% | $420.91 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 1001 | 48.4 | 49.7 | $-623.32 | -6.2% | $376.68 | -2.0 | done | can't tell from luck |
| coinflip | 1476 | 49.9 | 50.8 | $-807.42 | -5.5% | $192.58 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1476 | 49.7 | 51.5 | $-1048.51 | -7.1% | $-48.51 | -2.8 | done | losing for real |
| always_up | 1476 | 45.7 | 50.7 | $-1972.52 | -13.4% | $-972.52 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2261 | 47.4 | 49.4 | $-1777.18 |
| ETH | 2526 | 47.7 | 48.9 | $-1780.96 |
| SOL | 2602 | 48.0 | 49.4 | $-1865.07 |
| XRP | 2659 | 48.8 | 49.1 | $-1298.94 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
