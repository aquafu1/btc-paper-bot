# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 11:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 926 windows, 25613 settled trades, 25 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 475 | 35.2 | 34.8 | $-145.74 | -3.1% | $854.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1161 | 38.2 | 39.1 | $-632.90 | -5.5% | $367.10 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2182 | 50.1 | 49.8 | $-911.19 | -4.2% | $88.81 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2613 | 50.7 | 50.5 | $-993.59 | -3.8% | $6.41 | -1.9 | done | can't tell from luck |
| value_ev5 | 1762 | 39.8 | 41.0 | $-1057.50 | -6.0% | $-57.50 | -2.1 | done | losing for real |
| trend_filter | 1525 | 49.8 | 51.0 | $-1083.57 | -7.1% | $-83.57 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2613 | 49.3 | 50.3 | $-1507.33 | -5.8% | $-507.33 | -3.0 | done | losing for real |
| reversal_60m_0.30pct | 2182 | 49.9 | 50.9 | $-1507.41 | -6.9% | $-507.41 | -3.3 | done | losing for real |
| coinflip | 3700 | 50.3 | 50.3 | $-1572.03 | -4.2% | $-572.03 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3700 | 50.9 | 51.6 | $-1925.45 | -5.2% | $-925.45 | -3.3 | done | losing for real |
| always_up | 3700 | 46.8 | 49.7 | $-3742.67 | -10.1% | $-2742.67 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5834 | 48.1 | 49.1 | $-3367.52 |
| ETH | 6372 | 48.1 | 48.5 | $-4001.18 |
| SOL | 6682 | 48.1 | 48.6 | $-3917.08 |
| XRP | 6725 | 48.3 | 48.5 | $-3793.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
