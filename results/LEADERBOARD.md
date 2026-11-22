# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 8:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1104 windows, 30545 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 580 | 34.5 | 35.0 | $-351.49 | -6.1% | $648.51 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3082 | 51.2 | 50.4 | $-818.60 | -2.7% | $181.40 | -1.5 | done | can't tell from luck |
| value_ev10 | 1423 | 37.9 | 39.1 | $-911.09 | -6.4% | $88.91 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 2597 | 49.7 | 49.4 | $-1071.85 | -4.1% | $-71.85 | -2.1 | done | losing for real |
| value_ev5 | 2156 | 39.9 | 41.0 | $-1277.31 | -5.9% | $-277.31 | -2.3 | done | losing for real |
| trend_filter | 1804 | 49.3 | 50.4 | $-1323.65 | -7.3% | $-323.65 | -3.2 | done | losing for real |
| coinflip | 4408 | 50.5 | 50.2 | $-1677.44 | -3.8% | $-677.44 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2597 | 50.3 | 51.1 | $-1700.29 | -6.5% | $-700.29 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3082 | 48.8 | 50.2 | $-2079.17 | -6.7% | $-1079.17 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4408 | 50.7 | 51.4 | $-2331.58 | -5.3% | $-1331.58 | -3.6 | done | losing for real |
| always_up | 4408 | 47.5 | 49.3 | $-3557.05 | -8.1% | $-2557.05 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6996 | 48.4 | 49.0 | $-3467.52 |
| ETH | 7562 | 48.2 | 48.4 | $-4481.73 |
| SOL | 7951 | 48.1 | 48.4 | $-4448.37 |
| XRP | 8036 | 48.2 | 48.2 | $-4701.89 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
