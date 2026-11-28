# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 7:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1628 windows, 39091 settled trades, 352 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 830 | 34.3 | 35.2 | $-625.19 | -7.5% | $374.81 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3850 | 50.8 | 50.0 | $-1028.71 | -2.7% | $-28.71 | -1.7 | done | can't tell from luck |
| value_ev10 | 1959 | 38.3 | 39.0 | $-1118.52 | -5.7% | $-118.52 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3222 | 51.0 | 50.9 | $-1499.85 | -4.7% | $-499.85 | -2.7 | done | losing for real |
| value_ev5 | 2928 | 40.4 | 41.0 | $-1541.06 | -5.3% | $-541.06 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 3222 | 49.0 | 49.2 | $-1738.45 | -5.4% | $-738.45 | -3.0 | done | losing for real |
| trend_filter | 2292 | 48.6 | 50.4 | $-1999.36 | -8.7% | $-999.36 | -4.3 | done | losing for real |
| momentum_15m_0.10pct | 3850 | 49.2 | 50.2 | $-2346.42 | -6.1% | $-1346.42 | -3.8 | done | losing for real |
| coinflip | 5646 | 50.1 | 49.9 | $-2356.57 | -4.2% | $-1356.57 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5646 | 50.2 | 51.3 | $-3399.61 | -6.0% | $-2399.61 | -4.7 | done | losing for real |
| always_up | 5646 | 48.2 | 49.1 | $-3567.66 | -6.3% | $-2567.66 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10453 | 48.0 | 48.6 | $-5821.78 |
| ETH | 11328 | 48.0 | 47.7 | $-5815.38 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
