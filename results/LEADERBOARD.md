# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 28, 6:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1674 windows, 39643 settled trades, 334 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 847 | 34.2 | 35.2 | $-664.92 | -7.9% | $335.08 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3892 | 50.8 | 49.9 | $-1002.65 | -2.6% | $-2.65 | -1.6 | done | can't tell from luck |
| value_ev10 | 2000 | 38.4 | 39.0 | $-1131.63 | -5.7% | $-131.63 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3249 | 51.1 | 50.9 | $-1416.87 | -4.4% | $-416.87 | -2.5 | done | losing for real |
| value_ev5 | 2984 | 40.3 | 41.0 | $-1637.46 | -5.5% | $-637.46 | -2.5 | done | losing for real |
| momentum_60m_0.30pct | 3249 | 48.9 | 49.3 | $-1831.92 | -5.6% | $-831.92 | -3.2 | done | losing for real |
| trend_filter | 2316 | 48.3 | 50.3 | $-2131.37 | -9.2% | $-1131.37 | -4.5 | done | losing for real |
| momentum_15m_0.10pct | 3892 | 49.2 | 50.2 | $-2379.41 | -6.1% | $-1379.41 | -3.8 | done | losing for real |
| coinflip | 5738 | 49.9 | 49.9 | $-2507.88 | -4.4% | $-1507.88 | -3.3 | done | losing for real |
| always_up | 5738 | 48.3 | 49.0 | $-3542.14 | -6.2% | $-2542.14 | -4.6 | done | losing for real |
| momentum_5m_0.00pct | 5738 | 50.1 | 51.3 | $-3582.53 | -6.2% | $-2582.53 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10718 | 47.9 | 48.5 | $-6024.76 |
| ETH | 11615 | 47.8 | 47.6 | $-6219.78 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
