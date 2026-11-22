# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 7:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1052 windows, 29155 settled trades, 34 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 544 | 34.6 | 35.1 | $-308.54 | -5.7% | $691.46 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2954 | 51.3 | 50.5 | $-773.31 | -2.6% | $226.69 | -1.4 | done | can't tell from luck |
| value_ev10 | 1350 | 37.6 | 39.2 | $-953.39 | -7.1% | $46.61 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2484 | 49.6 | 49.6 | $-1182.66 | -4.8% | $-182.66 | -2.4 | done | losing for real |
| trend_filter | 1738 | 49.3 | 50.7 | $-1368.44 | -7.9% | $-368.44 | -3.4 | done | losing for real |
| value_ev5 | 2044 | 39.5 | 41.0 | $-1413.23 | -6.9% | $-413.23 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2484 | 50.4 | 51.0 | $-1546.08 | -6.2% | $-546.08 | -3.2 | done | losing for real |
| coinflip | 4201 | 50.5 | 50.3 | $-1704.50 | -4.1% | $-704.50 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2954 | 48.7 | 50.3 | $-2068.19 | -7.0% | $-1068.19 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4201 | 50.7 | 51.5 | $-2272.16 | -5.4% | $-1272.16 | -3.6 | done | losing for real |
| always_up | 4201 | 47.3 | 49.4 | $-3657.17 | -8.7% | $-2657.17 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6646 | 48.3 | 49.0 | $-3541.62 |
| ETH | 7217 | 48.1 | 48.5 | $-4625.79 |
| SOL | 7612 | 48.1 | 48.5 | $-4393.82 |
| XRP | 7680 | 48.2 | 48.3 | $-4686.44 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
