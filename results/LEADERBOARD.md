# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 5:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1382 windows, 35840 settled trades, 394 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 719 | 34.5 | 35.3 | $-522.79 | -7.3% | $477.21 | -1.5 | done | can't tell from luck |
| value_ev10 | 1741 | 38.8 | 39.2 | $-801.84 | -4.6% | $198.16 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3580 | 50.8 | 50.1 | $-1048.41 | -2.9% | $-48.41 | -1.7 | done | can't tell from luck |
| value_ev5 | 2619 | 40.4 | 41.1 | $-1313.93 | -5.0% | $-313.93 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 3004 | 49.3 | 49.3 | $-1474.17 | -4.9% | $-474.17 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3004 | 50.7 | 50.9 | $-1548.09 | -5.2% | $-548.09 | -2.9 | done | losing for real |
| trend_filter | 2128 | 48.5 | 50.4 | $-1889.89 | -8.9% | $-889.89 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3580 | 49.2 | 50.2 | $-2190.13 | -6.1% | $-1190.13 | -3.7 | done | losing for real |
| coinflip | 5155 | 50.0 | 50.0 | $-2198.87 | -4.3% | $-1198.87 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5155 | 50.1 | 51.3 | $-3221.43 | -6.2% | $-2221.43 | -4.6 | done | losing for real |
| always_up | 5155 | 47.9 | 49.3 | $-3704.92 | -7.2% | $-2704.92 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8926 | 47.9 | 48.8 | $-5069.47 |
| ETH | 9604 | 48.1 | 48.1 | $-5260.79 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
