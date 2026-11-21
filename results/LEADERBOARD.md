# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 12:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1025 windows, 28544 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 528 | 34.7 | 35.1 | $-284.79 | -5.4% | $715.21 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2909 | 51.1 | 50.5 | $-879.86 | -3.0% | $120.14 | -1.6 | done | can't tell from luck |
| value_ev10 | 1310 | 37.5 | 39.2 | $-974.07 | -7.4% | $25.93 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2458 | 49.9 | 49.6 | $-1052.65 | -4.3% | $-52.65 | -2.1 | done | losing for real |
| trend_filter | 1711 | 49.6 | 50.7 | $-1241.06 | -7.3% | $-241.06 | -3.1 | done | losing for real |
| value_ev5 | 1985 | 39.4 | 41.0 | $-1413.61 | -7.1% | $-413.61 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2458 | 50.1 | 51.0 | $-1655.67 | -6.7% | $-655.67 | -3.4 | done | losing for real |
| coinflip | 4092 | 50.5 | 50.4 | $-1685.13 | -4.1% | $-685.13 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2909 | 48.9 | 50.3 | $-1944.53 | -6.7% | $-944.53 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4092 | 50.7 | 51.5 | $-2241.16 | -5.5% | $-1241.16 | -3.6 | done | losing for real |
| always_up | 4092 | 47.4 | 49.5 | $-3590.49 | -8.8% | $-2590.49 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6508 | 48.3 | 49.1 | $-3508.22 |
| ETH | 7087 | 48.1 | 48.5 | $-4438.15 |
| SOL | 7456 | 48.2 | 48.6 | $-4275.97 |
| XRP | 7493 | 48.1 | 48.4 | $-4740.71 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
