# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 1:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 932 windows, 25781 settled trades, 34 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 475 | 35.2 | 34.8 | $-145.74 | -3.1% | $854.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1165 | 38.0 | 39.1 | $-672.90 | -5.8% | $327.10 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2635 | 51.0 | 50.6 | $-897.98 | -3.4% | $102.02 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2199 | 50.1 | 49.8 | $-927.47 | -4.2% | $72.53 | -2.0 | done | can't tell from luck |
| trend_filter | 1530 | 49.9 | 51.0 | $-1060.97 | -6.9% | $-60.97 | -2.8 | done | losing for real |
| value_ev5 | 1771 | 39.7 | 41.0 | $-1106.70 | -6.2% | $-106.70 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 2199 | 49.9 | 50.9 | $-1537.97 | -7.0% | $-537.97 | -3.4 | done | losing for real |
| coinflip | 3724 | 50.4 | 50.4 | $-1561.70 | -4.2% | $-561.70 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2635 | 49.0 | 50.3 | $-1676.56 | -6.4% | $-676.56 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 3724 | 51.0 | 51.6 | $-1899.73 | -5.1% | $-899.73 | -3.2 | done | losing for real |
| always_up | 3724 | 46.8 | 49.7 | $-3832.98 | -10.3% | $-2832.98 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5877 | 48.1 | 49.1 | $-3456.04 |
| ETH | 6410 | 48.2 | 48.6 | $-4033.14 |
| SOL | 6725 | 48.1 | 48.6 | $-3984.79 |
| XRP | 6769 | 48.3 | 48.5 | $-3846.72 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
