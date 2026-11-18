# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 11:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 734 windows, 20220 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 382 | 33.5 | 34.9 | $-322.66 | -8.4% | $677.34 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 2074 | 51.6 | 50.7 | $-465.32 | -2.2% | $534.68 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1700 | 50.2 | 49.6 | $-556.90 | -3.3% | $443.10 | -1.3 | done | can't tell from luck |
| value_ev10 | 925 | 38.1 | 39.1 | $-596.66 | -6.5% | $403.34 | -1.6 | done | can't tell from luck |
| trend_filter | 1185 | 50.2 | 51.0 | $-690.04 | -5.8% | $309.96 | -2.0 | done | losing for real |
| value_ev5 | 1396 | 40.5 | 41.1 | $-721.72 | -5.2% | $278.28 | -1.6 | done | can't tell from luck |
| coinflip | 2928 | 50.2 | 50.3 | $-1211.15 | -4.1% | $-211.15 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1700 | 49.8 | 51.2 | $-1238.22 | -7.3% | $-238.22 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2074 | 48.4 | 50.1 | $-1483.65 | -7.2% | $-483.65 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 2928 | 50.9 | 51.8 | $-1550.93 | -5.3% | $-550.93 | -3.0 | done | losing for real |
| always_up | 2928 | 47.0 | 49.6 | $-2684.72 | -9.2% | $-1684.72 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4581 | 48.1 | 49.1 | $-2845.95 |
| ETH | 5038 | 48.2 | 48.6 | $-3079.85 |
| SOL | 5265 | 48.1 | 48.7 | $-3015.06 |
| XRP | 5336 | 48.5 | 48.5 | $-2581.11 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
