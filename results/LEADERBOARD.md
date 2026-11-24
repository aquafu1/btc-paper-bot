# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 7:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1292 windows, 34537 settled trades, 405 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 680 | 34.0 | 35.3 | $-551.91 | -8.1% | $448.09 | -1.6 | done | can't tell from luck |
| value_ev10 | 1664 | 38.7 | 39.2 | $-806.28 | -4.8% | $193.72 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3464 | 50.8 | 50.2 | $-1091.79 | -3.2% | $-91.79 | -1.9 | done | can't tell from luck |
| value_ev5 | 2511 | 40.5 | 41.1 | $-1273.97 | -5.1% | $-273.97 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2895 | 49.5 | 49.4 | $-1317.96 | -4.6% | $-317.96 | -2.4 | done | losing for real |
| trend_filter | 2042 | 49.0 | 50.5 | $-1641.10 | -8.0% | $-641.10 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2895 | 50.5 | 51.0 | $-1660.87 | -5.7% | $-660.87 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3464 | 49.2 | 50.3 | $-2151.20 | -6.2% | $-1151.20 | -3.7 | done | losing for real |
| coinflip | 4974 | 50.0 | 50.1 | $-2234.32 | -4.5% | $-1234.32 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4974 | 50.5 | 51.4 | $-2796.30 | -5.6% | $-1796.30 | -4.1 | done | losing for real |
| always_up | 4974 | 47.9 | 49.3 | $-3582.03 | -7.2% | $-2582.03 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8288 | 48.0 | 48.8 | $-4799.11 |
| ETH | 8939 | 48.3 | 48.2 | $-4724.37 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
