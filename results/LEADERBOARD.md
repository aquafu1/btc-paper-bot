# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 12:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1024 windows, 28525 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 528 | 34.7 | 35.1 | $-284.79 | -5.4% | $715.21 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2907 | 51.1 | 50.5 | $-879.00 | -3.0% | $121.00 | -1.6 | done | can't tell from luck |
| value_ev10 | 1309 | 37.5 | 39.2 | $-964.07 | -7.4% | $35.93 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2457 | 49.9 | 49.6 | $-1042.65 | -4.2% | $-42.65 | -2.1 | done | losing for real |
| trend_filter | 1709 | 49.6 | 50.7 | $-1221.06 | -7.1% | $-221.06 | -3.0 | done | losing for real |
| value_ev5 | 1984 | 39.4 | 41.0 | $-1403.61 | -7.1% | $-403.61 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2457 | 50.1 | 51.0 | $-1661.74 | -6.8% | $-661.74 | -3.4 | done | losing for real |
| coinflip | 4089 | 50.5 | 50.4 | $-1690.34 | -4.1% | $-690.34 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2907 | 48.9 | 50.3 | $-1944.04 | -6.7% | $-944.04 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4089 | 50.7 | 51.5 | $-2230.30 | -5.5% | $-1230.30 | -3.6 | done | losing for real |
| always_up | 4089 | 47.4 | 49.5 | $-3579.63 | -8.8% | $-2579.63 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6508 | 48.3 | 49.1 | $-3508.22 |
| ETH | 7082 | 48.1 | 48.5 | $-4464.70 |
| SOL | 7450 | 48.2 | 48.6 | $-4235.48 |
| XRP | 7485 | 48.1 | 48.4 | $-4692.84 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
