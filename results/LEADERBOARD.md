# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 1:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1462 windows, 36958 settled trades, 348 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 748 | 34.1 | 35.3 | $-613.47 | -8.2% | $386.53 | -1.7 | done | can't tell from luck |
| value_ev10 | 1800 | 38.6 | 39.2 | $-930.25 | -5.2% | $69.75 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3683 | 50.9 | 50.0 | $-955.91 | -2.6% | $44.09 | -1.6 | done | can't tell from luck |
| value_ev5 | 2712 | 40.4 | 41.1 | $-1413.06 | -5.2% | $-413.06 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 3096 | 49.2 | 49.3 | $-1532.10 | -4.9% | $-532.10 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3096 | 50.8 | 51.0 | $-1590.93 | -5.1% | $-590.93 | -2.9 | done | losing for real |
| trend_filter | 2195 | 48.7 | 50.3 | $-1856.06 | -8.5% | $-856.06 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3683 | 49.1 | 50.2 | $-2349.87 | -6.4% | $-1349.87 | -3.9 | done | losing for real |
| coinflip | 5315 | 49.9 | 50.0 | $-2403.69 | -4.5% | $-1403.69 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5315 | 50.2 | 51.3 | $-3281.06 | -6.2% | $-2281.06 | -4.6 | done | losing for real |
| always_up | 5315 | 48.0 | 49.2 | $-3628.67 | -6.8% | $-2628.67 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9476 | 48.0 | 48.7 | $-5253.24 |
| ETH | 10172 | 48.0 | 48.0 | $-5717.60 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
