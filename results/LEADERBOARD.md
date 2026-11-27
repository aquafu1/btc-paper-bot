# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 5:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1575 windows, 38411 settled trades, 396 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 804 | 34.5 | 35.2 | $-571.63 | -7.1% | $428.37 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3798 | 50.9 | 50.0 | $-951.13 | -2.5% | $48.87 | -1.5 | done | can't tell from luck |
| value_ev10 | 1903 | 38.5 | 39.0 | $-964.04 | -5.1% | $35.96 | -1.8 | done | can't tell from luck |
| value_ev5 | 2857 | 40.5 | 41.0 | $-1413.41 | -4.9% | $-413.41 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3183 | 51.0 | 50.9 | $-1493.91 | -4.7% | $-493.91 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3183 | 49.0 | 49.2 | $-1687.95 | -5.3% | $-687.95 | -3.0 | done | losing for real |
| trend_filter | 2262 | 48.5 | 50.3 | $-1981.52 | -8.8% | $-981.52 | -4.3 | done | losing for real |
| coinflip | 5541 | 50.0 | 49.9 | $-2378.74 | -4.3% | $-1378.74 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3798 | 49.1 | 50.2 | $-2379.09 | -6.3% | $-1379.09 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 5541 | 50.1 | 51.3 | $-3493.25 | -6.3% | $-2493.25 | -4.8 | done | losing for real |
| always_up | 5541 | 48.2 | 49.2 | $-3526.40 | -6.4% | $-2526.40 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10146 | 47.9 | 48.6 | $-5726.59 |
| ETH | 10955 | 48.0 | 47.7 | $-5530.25 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
