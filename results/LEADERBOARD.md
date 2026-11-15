# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 11:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 396 windows, 10836 settled trades, 64 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 199 | 36.7 | 36.5 | $-56.95 | -2.9% | $943.05 | -0.3 | Sat 11:30 PM | too few trades (199/200) |
| value_ev10 | 516 | 40.3 | 40.5 | $-185.67 | -3.6% | $814.33 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 918 | 50.5 | 49.8 | $-239.06 | -2.6% | $760.94 | -0.8 | done | can't tell from luck |
| value_ev5 | 763 | 41.9 | 42.1 | $-301.20 | -3.9% | $698.80 | -0.9 | done | can't tell from luck |
| trend_filter | 614 | 49.7 | 50.6 | $-352.33 | -5.7% | $647.67 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1090 | 49.1 | 49.8 | $-533.52 | -4.9% | $466.48 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1090 | 50.9 | 52.0 | $-650.29 | -6.0% | $349.71 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 918 | 49.5 | 52.1 | $-811.03 | -8.8% | $188.97 | -2.8 | done | losing for real |
| coinflip | 1576 | 50.0 | 50.8 | $-813.88 | -5.2% | $186.12 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1576 | 49.7 | 51.6 | $-1093.83 | -6.9% | $-93.83 | -2.9 | done | losing for real |
| always_up | 1576 | 46.4 | 50.8 | $-1891.92 | -12.0% | $-891.92 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2452 | 47.7 | 49.4 | $-1721.23 |
| ETH | 2718 | 48.0 | 48.9 | $-1660.78 |
| SOL | 2802 | 48.0 | 49.5 | $-2088.88 |
| XRP | 2864 | 48.9 | 49.2 | $-1458.81 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
