# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 10:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 921 windows, 25452 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 475 | 35.2 | 34.8 | $-145.74 | -3.1% | $854.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1161 | 38.2 | 39.1 | $-632.90 | -5.5% | $367.10 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2162 | 50.3 | 49.8 | $-834.69 | -3.9% | $165.31 | -1.8 | done | can't tell from luck |
| trend_filter | 1513 | 50.2 | 51.0 | $-985.90 | -6.5% | $14.10 | -2.6 | done | losing for real |
| value_ev5 | 1759 | 39.8 | 41.0 | $-1049.83 | -6.0% | $-49.83 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2593 | 50.5 | 50.5 | $-1064.00 | -4.1% | $-64.00 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2593 | 49.5 | 50.3 | $-1411.26 | -5.4% | $-411.26 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2162 | 49.7 | 50.9 | $-1561.84 | -7.2% | $-561.84 | -3.4 | done | losing for real |
| coinflip | 3678 | 50.3 | 50.3 | $-1582.28 | -4.3% | $-582.28 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3678 | 51.1 | 51.6 | $-1803.49 | -4.9% | $-803.49 | -3.1 | done | losing for real |
| always_up | 3678 | 46.7 | 49.7 | $-3764.21 | -10.2% | $-2764.21 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5801 | 48.2 | 49.1 | $-3317.58 |
| ETH | 6326 | 48.2 | 48.5 | $-3919.32 |
| SOL | 6635 | 48.2 | 48.6 | $-3864.92 |
| XRP | 6690 | 48.3 | 48.5 | $-3734.30 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
