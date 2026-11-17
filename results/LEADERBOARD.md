# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 12:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 593 windows, 16408 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1389 | 51.2 | 49.6 | $-209.99 | -1.5% | $790.01 | -0.6 | done | can't tell from luck |
| value_ev20 | 322 | 34.2 | 35.2 | $-257.97 | -8.0% | $742.03 | -1.1 | done | can't tell from luck |
| trend_filter | 952 | 50.2 | 51.0 | $-545.68 | -5.7% | $454.32 | -1.8 | done | can't tell from luck |
| value_ev10 | 770 | 37.8 | 39.4 | $-636.74 | -8.3% | $363.26 | -1.9 | done | can't tell from luck |
| value_ev5 | 1151 | 40.4 | 41.2 | $-713.04 | -6.2% | $286.96 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1670 | 50.9 | 51.0 | $-771.37 | -4.6% | $228.63 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1670 | 49.1 | 49.9 | $-964.71 | -5.8% | $35.29 | -2.4 | done | losing for real |
| coinflip | 2365 | 49.9 | 50.5 | $-1227.42 | -5.2% | $-227.42 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1389 | 48.8 | 51.3 | $-1341.93 | -9.7% | $-341.93 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2365 | 50.2 | 51.8 | $-1596.64 | -6.8% | $-596.64 | -3.4 | done | losing for real |
| always_up | 2365 | 47.3 | 49.8 | $-2166.92 | -9.2% | $-1166.92 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3721 | 47.9 | 49.2 | $-2562.19 |
| ETH | 4091 | 48.0 | 48.6 | $-2643.13 |
| SOL | 4272 | 47.9 | 48.7 | $-2965.55 |
| XRP | 4324 | 48.5 | 48.6 | $-2261.52 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
