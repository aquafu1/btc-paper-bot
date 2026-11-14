# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 2:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 360 windows, 9705 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 186 | 37.1 | 36.6 | $-58.35 | -3.1% | $941.65 | -0.3 | Sat 9:00 PM | too few trades (186/200) |
| value_ev10 | 466 | 39.9 | 40.3 | $-221.42 | -4.8% | $778.58 | -0.9 | done | can't tell from luck |
| value_ev5 | 693 | 41.4 | 42.0 | $-370.39 | -5.3% | $629.61 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 960 | 52.0 | 52.0 | $-413.34 | -4.3% | $586.66 | -1.4 | done | can't tell from luck |
| trend_filter | 538 | 48.5 | 50.5 | $-450.88 | -8.4% | $549.12 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 803 | 51.1 | 52.0 | $-457.12 | -5.7% | $542.88 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 803 | 48.9 | 49.7 | $-483.76 | -6.0% | $516.24 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 960 | 48.0 | 49.7 | $-721.87 | -7.5% | $278.13 | -2.3 | done | losing for real |
| coinflip | 1432 | 50.1 | 50.8 | $-759.92 | -5.3% | $240.08 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1432 | 49.7 | 51.5 | $-1045.82 | -7.3% | $-45.82 | -2.9 | done | losing for real |
| always_up | 1432 | 46.3 | 50.6 | $-1752.59 | -12.2% | $-752.59 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2176 | 47.3 | 49.3 | $-1765.17 |
| ETH | 2443 | 47.7 | 48.8 | $-1749.86 |
| SOL | 2516 | 48.1 | 49.4 | $-1867.98 |
| XRP | 2570 | 48.8 | 49.1 | $-1352.43 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
