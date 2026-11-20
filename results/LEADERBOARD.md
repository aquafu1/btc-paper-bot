# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 10:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 922 windows, 25481 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 475 | 35.2 | 34.8 | $-145.74 | -3.1% | $854.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1161 | 38.2 | 39.1 | $-632.90 | -5.5% | $367.10 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2166 | 50.3 | 49.8 | $-832.37 | -3.8% | $167.63 | -1.8 | done | can't tell from luck |
| trend_filter | 1515 | 50.1 | 51.0 | $-1005.90 | -6.6% | $-5.90 | -2.7 | done | losing for real |
| reversal_15m_0.10pct | 2596 | 50.5 | 50.5 | $-1055.27 | -4.1% | $-55.27 | -2.1 | done | losing for real |
| value_ev5 | 1760 | 39.8 | 41.0 | $-1059.83 | -6.0% | $-59.83 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2596 | 49.5 | 50.3 | $-1423.08 | -5.5% | $-423.08 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2166 | 49.7 | 50.9 | $-1565.41 | -7.2% | $-565.41 | -3.4 | done | losing for real |
| coinflip | 3682 | 50.3 | 50.3 | $-1582.27 | -4.3% | $-582.27 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3682 | 51.0 | 51.6 | $-1843.49 | -5.0% | $-843.49 | -3.1 | done | losing for real |
| always_up | 3682 | 46.7 | 49.7 | $-3767.78 | -10.2% | $-2767.78 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5808 | 48.2 | 49.1 | $-3346.61 |
| ETH | 6340 | 48.2 | 48.5 | $-3960.91 |
| SOL | 6643 | 48.2 | 48.6 | $-3872.20 |
| XRP | 6690 | 48.3 | 48.5 | $-3734.30 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
