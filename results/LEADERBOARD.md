# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 1:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1461 windows, 36947 settled trades, 350 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 748 | 34.1 | 35.3 | $-613.47 | -8.2% | $386.53 | -1.7 | done | can't tell from luck |
| value_ev10 | 1800 | 38.6 | 39.2 | $-930.25 | -5.2% | $69.75 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3682 | 50.9 | 50.0 | $-965.03 | -2.6% | $34.97 | -1.6 | done | can't tell from luck |
| value_ev5 | 2712 | 40.4 | 41.1 | $-1413.06 | -5.2% | $-413.06 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 3095 | 49.2 | 49.3 | $-1541.60 | -5.0% | $-541.60 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 3095 | 50.8 | 51.0 | $-1580.93 | -5.1% | $-580.93 | -2.9 | done | losing for real |
| trend_filter | 2194 | 48.7 | 50.3 | $-1865.56 | -8.5% | $-865.56 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3682 | 49.1 | 50.2 | $-2339.87 | -6.4% | $-1339.87 | -3.9 | done | losing for real |
| coinflip | 5313 | 49.9 | 50.0 | $-2383.69 | -4.5% | $-1383.69 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5313 | 50.2 | 51.3 | $-3299.69 | -6.2% | $-2299.69 | -4.7 | done | losing for real |
| always_up | 5313 | 48.0 | 49.2 | $-3627.80 | -6.8% | $-2627.80 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9465 | 48.0 | 48.7 | $-5259.12 |
| ETH | 10172 | 48.0 | 48.0 | $-5717.60 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
