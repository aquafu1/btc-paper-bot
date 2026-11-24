# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 7:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1295 windows, 34585 settled trades, 406 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 682 | 34.2 | 35.3 | $-534.70 | -7.8% | $465.30 | -1.6 | done | can't tell from luck |
| value_ev10 | 1667 | 38.8 | 39.2 | $-765.98 | -4.6% | $234.02 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3469 | 50.8 | 50.2 | $-1033.28 | -3.0% | $-33.28 | -1.8 | done | can't tell from luck |
| value_ev5 | 2515 | 40.5 | 41.1 | $-1243.67 | -4.9% | $-243.67 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2899 | 49.4 | 49.4 | $-1357.96 | -4.7% | $-357.96 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2899 | 50.6 | 51.0 | $-1592.36 | -5.5% | $-592.36 | -3.0 | done | losing for real |
| trend_filter | 2045 | 48.9 | 50.5 | $-1671.10 | -8.2% | $-671.10 | -3.8 | done | losing for real |
| momentum_15m_0.10pct | 3469 | 49.2 | 50.3 | $-2182.43 | -6.3% | $-1182.43 | -3.7 | done | losing for real |
| coinflip | 4980 | 50.0 | 50.1 | $-2224.99 | -4.5% | $-1224.99 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4980 | 50.4 | 51.4 | $-2823.20 | -5.7% | $-1823.20 | -4.1 | done | losing for real |
| always_up | 4980 | 47.9 | 49.3 | $-3582.04 | -7.2% | $-2582.04 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8312 | 48.0 | 48.8 | $-4766.70 |
| ETH | 8963 | 48.3 | 48.2 | $-4660.77 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
