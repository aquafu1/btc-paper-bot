# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 7:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1007 windows, 28018 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 518 | 34.2 | 35.0 | $-312.56 | -6.0% | $687.44 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2855 | 51.0 | 50.4 | $-875.32 | -3.1% | $124.68 | -1.6 | done | can't tell from luck |
| value_ev10 | 1283 | 37.5 | 39.1 | $-922.99 | -7.2% | $77.01 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2411 | 50.1 | 49.7 | $-950.86 | -3.9% | $49.14 | -1.9 | done | can't tell from luck |
| trend_filter | 1680 | 49.8 | 50.8 | $-1167.29 | -6.9% | $-167.29 | -2.9 | done | losing for real |
| value_ev5 | 1945 | 39.6 | 41.0 | $-1274.73 | -6.6% | $-274.73 | -2.4 | done | losing for real |
| coinflip | 4020 | 50.5 | 50.4 | $-1656.72 | -4.1% | $-656.72 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2411 | 49.9 | 51.0 | $-1722.52 | -7.1% | $-722.52 | -3.6 | done | losing for real |
| momentum_15m_0.10pct | 2855 | 49.0 | 50.3 | $-1923.52 | -6.7% | $-923.52 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4020 | 50.7 | 51.5 | $-2218.80 | -5.5% | $-1218.80 | -3.6 | done | losing for real |
| always_up | 4020 | 47.2 | 49.5 | $-3686.22 | -9.2% | $-2686.22 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6388 | 48.2 | 49.0 | $-3562.77 |
| ETH | 6960 | 48.1 | 48.5 | $-4424.64 |
| SOL | 7323 | 48.2 | 48.6 | $-4095.85 |
| XRP | 7347 | 48.1 | 48.4 | $-4628.27 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
