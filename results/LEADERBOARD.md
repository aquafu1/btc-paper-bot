# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 10:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 921 windows, 25437 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 475 | 35.2 | 34.8 | $-145.74 | -3.1% | $854.26 | -0.5 | done | can't tell from luck |
| value_ev10 | 1160 | 38.2 | 39.1 | $-622.90 | -5.4% | $377.10 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2160 | 50.3 | 49.8 | $-814.69 | -3.8% | $185.31 | -1.8 | done | can't tell from luck |
| trend_filter | 1512 | 50.2 | 51.0 | $-975.90 | -6.5% | $24.10 | -2.6 | done | losing for real |
| value_ev5 | 1758 | 39.8 | 41.0 | $-1039.83 | -5.9% | $-39.83 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2592 | 50.5 | 50.5 | $-1074.08 | -4.1% | $-74.08 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 2592 | 49.5 | 50.3 | $-1401.26 | -5.4% | $-401.26 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2160 | 49.7 | 50.9 | $-1576.92 | -7.3% | $-576.92 | -3.5 | done | losing for real |
| coinflip | 3676 | 50.3 | 50.3 | $-1577.29 | -4.3% | $-577.29 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3676 | 51.1 | 51.6 | $-1798.50 | -4.9% | $-798.50 | -3.1 | done | losing for real |
| always_up | 3676 | 46.7 | 49.7 | $-3779.29 | -10.3% | $-2779.29 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5793 | 48.2 | 49.1 | $-3297.81 |
| ETH | 6326 | 48.2 | 48.5 | $-3919.32 |
| SOL | 6635 | 48.2 | 48.6 | $-3864.92 |
| XRP | 6683 | 48.3 | 48.5 | $-3724.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
