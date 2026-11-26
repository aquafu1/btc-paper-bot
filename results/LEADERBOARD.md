# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 12:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1507 windows, 37530 settled trades, 383 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 763 | 34.5 | 35.4 | $-561.57 | -7.4% | $438.43 | -1.6 | done | can't tell from luck |
| value_ev10 | 1832 | 38.5 | 39.2 | $-955.09 | -5.2% | $44.91 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3734 | 50.9 | 50.1 | $-960.91 | -2.6% | $39.09 | -1.6 | done | can't tell from luck |
| value_ev5 | 2763 | 40.6 | 41.1 | $-1352.97 | -4.9% | $-352.97 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3132 | 51.1 | 51.0 | $-1422.57 | -4.5% | $-422.57 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3132 | 48.9 | 49.2 | $-1727.92 | -5.5% | $-727.92 | -3.1 | done | losing for real |
| trend_filter | 2222 | 48.6 | 50.3 | $-1919.92 | -8.6% | $-919.92 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3734 | 49.1 | 50.2 | $-2309.93 | -6.2% | $-1309.93 | -3.8 | done | losing for real |
| coinflip | 5406 | 50.0 | 50.0 | $-2360.40 | -4.4% | $-1360.40 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5406 | 50.2 | 51.3 | $-3333.26 | -6.2% | $-2333.26 | -4.7 | done | losing for real |
| always_up | 5406 | 48.0 | 49.2 | $-3590.25 | -6.6% | $-2590.25 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9739 | 48.0 | 48.7 | $-5381.15 |
| ETH | 10481 | 48.0 | 47.9 | $-5529.43 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
