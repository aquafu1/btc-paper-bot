# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 28, 6:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1673 windows, 39636 settled trades, 331 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 847 | 34.2 | 35.2 | $-664.92 | -7.9% | $335.08 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3891 | 50.8 | 49.9 | $-992.65 | -2.6% | $7.35 | -1.6 | done | can't tell from luck |
| value_ev10 | 1999 | 38.3 | 39.0 | $-1142.13 | -5.7% | $-142.13 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3249 | 51.1 | 50.9 | $-1416.87 | -4.4% | $-416.87 | -2.5 | done | losing for real |
| value_ev5 | 2983 | 40.3 | 41.0 | $-1647.97 | -5.5% | $-647.97 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3249 | 48.9 | 49.3 | $-1831.92 | -5.6% | $-831.92 | -3.2 | done | losing for real |
| trend_filter | 2316 | 48.3 | 50.3 | $-2131.37 | -9.2% | $-1131.37 | -4.5 | done | losing for real |
| momentum_15m_0.10pct | 3891 | 49.2 | 50.2 | $-2389.91 | -6.1% | $-1389.91 | -3.9 | done | losing for real |
| coinflip | 5737 | 49.9 | 49.9 | $-2518.38 | -4.4% | $-1518.38 | -3.3 | done | losing for real |
| always_up | 5737 | 48.3 | 49.0 | $-3552.65 | -6.2% | $-2552.65 | -4.6 | done | losing for real |
| momentum_5m_0.00pct | 5737 | 50.1 | 51.3 | $-3593.03 | -6.3% | $-2593.03 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10718 | 47.9 | 48.5 | $-6024.76 |
| ETH | 11608 | 47.8 | 47.6 | $-6272.82 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
