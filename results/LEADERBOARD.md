# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 10:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 346 windows, 9290 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 184 | 37.5 | 36.6 | $-38.35 | -2.1% | $961.65 | -0.2 | Sat 6:30 PM | too few trades (184/200) |
| value_ev10 | 455 | 40.2 | 40.3 | $-179.48 | -3.9% | $820.52 | -0.7 | done | can't tell from luck |
| value_ev5 | 673 | 41.8 | 42.0 | $-300.46 | -4.5% | $699.54 | -1.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 751 | 51.7 | 52.1 | $-337.62 | -4.5% | $662.38 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 920 | 52.0 | 52.0 | $-385.84 | -4.2% | $614.16 | -1.3 | done | can't tell from luck |
| momentum_60m_0.30pct | 751 | 48.3 | 49.6 | $-505.03 | -6.7% | $494.97 | -1.9 | done | can't tell from luck |
| trend_filter | 505 | 46.7 | 50.2 | $-550.93 | -10.9% | $449.07 | -2.5 | done | losing for real |
| coinflip | 1377 | 50.3 | 50.8 | $-647.84 | -4.7% | $352.16 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 920 | 48.0 | 49.7 | $-671.57 | -7.3% | $328.43 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1377 | 48.7 | 51.3 | $-1193.28 | -8.7% | $-193.28 | -3.3 | done | losing for real |
| always_up | 1377 | 46.6 | 50.6 | $-1582.77 | -11.5% | $-582.77 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2090 | 47.0 | 49.3 | $-1744.13 |
| ETH | 2335 | 47.5 | 48.7 | $-1692.64 |
| SOL | 2406 | 48.0 | 49.3 | $-1794.79 |
| XRP | 2459 | 48.8 | 49.1 | $-1161.62 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
