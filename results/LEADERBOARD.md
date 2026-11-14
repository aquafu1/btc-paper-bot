# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 10:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 346 windows, 9282 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 184 | 37.5 | 36.6 | $-38.35 | -2.1% | $961.65 | -0.2 | Sat 6:15 PM | too few trades (184/200) |
| value_ev10 | 455 | 40.2 | 40.3 | $-179.48 | -3.9% | $820.52 | -0.7 | done | can't tell from luck |
| value_ev5 | 673 | 41.8 | 42.0 | $-300.46 | -4.5% | $699.54 | -1.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 750 | 51.6 | 52.1 | $-345.87 | -4.6% | $654.13 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 919 | 51.9 | 52.0 | $-394.09 | -4.3% | $605.91 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 750 | 48.4 | 49.6 | $-495.03 | -6.6% | $504.97 | -1.8 | done | can't tell from luck |
| trend_filter | 504 | 46.8 | 50.2 | $-540.93 | -10.7% | $459.07 | -2.4 | done | losing for real |
| coinflip | 1376 | 50.4 | 50.8 | $-637.84 | -4.6% | $362.16 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 919 | 48.1 | 49.7 | $-661.57 | -7.2% | $338.43 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1376 | 48.8 | 51.4 | $-1183.28 | -8.6% | $-183.28 | -3.3 | done | losing for real |
| always_up | 1376 | 46.6 | 50.6 | $-1591.01 | -11.6% | $-591.01 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2082 | 47.0 | 49.2 | $-1718.87 |
| ETH | 2335 | 47.5 | 48.7 | $-1692.64 |
| SOL | 2406 | 48.0 | 49.3 | $-1794.79 |
| XRP | 2459 | 48.8 | 49.1 | $-1161.62 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
