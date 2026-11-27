# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 7:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1534 windows, 37860 settled trades, 374 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 773 | 34.4 | 35.3 | $-586.25 | -7.6% | $413.75 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3757 | 50.9 | 50.0 | $-968.99 | -2.6% | $31.01 | -1.6 | done | can't tell from luck |
| value_ev10 | 1856 | 38.5 | 39.2 | $-987.26 | -5.3% | $12.74 | -1.9 | done | can't tell from luck |
| value_ev5 | 2798 | 40.6 | 41.1 | $-1381.63 | -4.9% | $-381.63 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3152 | 51.0 | 51.0 | $-1464.01 | -4.6% | $-464.01 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3152 | 49.0 | 49.2 | $-1691.76 | -5.4% | $-691.76 | -3.0 | done | losing for real |
| trend_filter | 2241 | 48.6 | 50.3 | $-1917.96 | -8.6% | $-917.96 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3757 | 49.1 | 50.2 | $-2342.07 | -6.2% | $-1342.07 | -3.9 | done | losing for real |
| coinflip | 5458 | 49.9 | 50.0 | $-2434.95 | -4.5% | $-1434.95 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5458 | 50.1 | 51.3 | $-3397.10 | -6.2% | $-2397.10 | -4.7 | done | losing for real |
| always_up | 5458 | 48.1 | 49.2 | $-3579.64 | -6.6% | $-2579.64 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9891 | 47.9 | 48.7 | $-5647.13 |
| ETH | 10659 | 48.1 | 47.9 | $-5520.26 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
