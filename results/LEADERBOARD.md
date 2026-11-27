# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 2:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1562 windows, 38260 settled trades, 420 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 794 | 34.4 | 35.3 | $-579.84 | -7.3% | $420.16 | -1.6 | done | can't tell from luck |
| value_ev10 | 1889 | 38.4 | 39.1 | $-1000.54 | -5.3% | $-0.54 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3789 | 50.9 | 50.0 | $-1008.67 | -2.7% | $-8.67 | -1.6 | done | can't tell from luck |
| value_ev5 | 2836 | 40.4 | 41.0 | $-1424.19 | -5.0% | $-424.19 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3181 | 51.0 | 50.9 | $-1515.79 | -4.8% | $-515.79 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3181 | 49.0 | 49.2 | $-1667.95 | -5.2% | $-667.95 | -2.9 | done | losing for real |
| trend_filter | 2259 | 48.6 | 50.3 | $-1951.52 | -8.6% | $-951.52 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3789 | 49.1 | 50.2 | $-2325.48 | -6.1% | $-1325.48 | -3.8 | done | losing for real |
| coinflip | 5514 | 50.0 | 49.9 | $-2364.00 | -4.3% | $-1364.00 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5514 | 50.1 | 51.3 | $-3430.75 | -6.2% | $-2430.75 | -4.8 | done | losing for real |
| always_up | 5514 | 48.2 | 49.2 | $-3507.04 | -6.4% | $-2507.04 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10079 | 48.0 | 48.6 | $-5663.33 |
| ETH | 10871 | 48.0 | 47.8 | $-5528.21 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
