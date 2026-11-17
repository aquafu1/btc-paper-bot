# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 2:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 601 windows, 16607 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 324 | 34.6 | 35.2 | $-214.70 | -6.6% | $785.30 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1405 | 51.1 | 49.6 | $-218.06 | -1.6% | $781.94 | -0.6 | done | can't tell from luck |
| value_ev10 | 777 | 38.2 | 39.4 | $-540.78 | -7.0% | $459.22 | -1.6 | done | can't tell from luck |
| trend_filter | 957 | 50.2 | 50.9 | $-556.54 | -5.8% | $443.46 | -1.8 | done | can't tell from luck |
| value_ev5 | 1165 | 40.5 | 41.2 | $-665.25 | -5.7% | $334.75 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1693 | 50.9 | 50.9 | $-743.90 | -4.4% | $256.10 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 1693 | 49.1 | 50.0 | $-999.15 | -5.9% | $0.85 | -2.4 | done | losing for real |
| coinflip | 2396 | 50.0 | 50.5 | $-1202.26 | -5.0% | $-202.26 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1405 | 48.9 | 51.4 | $-1320.56 | -9.4% | $-320.56 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2396 | 50.2 | 51.7 | $-1577.21 | -6.6% | $-577.21 | -3.3 | done | losing for real |
| always_up | 2396 | 47.3 | 49.8 | $-2160.33 | -9.0% | $-1160.33 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3774 | 48.0 | 49.2 | $-2486.35 |
| ETH | 4141 | 48.0 | 48.6 | $-2668.39 |
| SOL | 4317 | 47.9 | 48.7 | $-2885.61 |
| XRP | 4375 | 48.6 | 48.6 | $-2158.38 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
