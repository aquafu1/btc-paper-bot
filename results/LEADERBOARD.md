# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 5:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1477 windows, 37143 settled trades, 370 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 752 | 34.2 | 35.4 | $-598.98 | -8.0% | $401.02 | -1.7 | done | can't tell from luck |
| value_ev10 | 1809 | 38.5 | 39.2 | $-965.77 | -5.3% | $34.23 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3702 | 50.9 | 50.1 | $-988.14 | -2.7% | $11.86 | -1.6 | done | can't tell from luck |
| value_ev5 | 2728 | 40.4 | 41.1 | $-1439.49 | -5.3% | $-439.49 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 3106 | 49.2 | 49.2 | $-1550.88 | -5.0% | $-550.88 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 3106 | 50.8 | 51.0 | $-1580.84 | -5.1% | $-580.84 | -2.9 | done | losing for real |
| trend_filter | 2206 | 48.6 | 50.3 | $-1908.00 | -8.6% | $-908.00 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3702 | 49.1 | 50.2 | $-2300.56 | -6.2% | $-1300.56 | -3.8 | done | losing for real |
| coinflip | 5344 | 49.9 | 50.0 | $-2387.67 | -4.5% | $-1387.67 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5344 | 50.0 | 51.3 | $-3446.41 | -6.4% | $-2446.41 | -4.9 | done | losing for real |
| always_up | 5344 | 48.0 | 49.2 | $-3576.60 | -6.7% | $-2576.60 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9560 | 48.0 | 48.7 | $-5285.08 |
| ETH | 10273 | 47.9 | 48.0 | $-5874.02 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
