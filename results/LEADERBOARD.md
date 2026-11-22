# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 4:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1136 windows, 31381 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 602 | 34.6 | 35.2 | $-373.62 | -6.2% | $626.38 | -1.2 | done | can't tell from luck |
| value_ev10 | 1471 | 38.1 | 39.2 | $-910.10 | -6.2% | $89.90 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3157 | 51.0 | 50.5 | $-935.65 | -3.0% | $64.35 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2650 | 49.7 | 49.4 | $-1121.45 | -4.2% | $-121.45 | -2.2 | done | losing for real |
| value_ev5 | 2226 | 40.1 | 41.1 | $-1293.93 | -5.8% | $-293.93 | -2.3 | done | losing for real |
| trend_filter | 1860 | 49.1 | 50.4 | $-1419.83 | -7.6% | $-419.83 | -3.4 | done | losing for real |
| reversal_60m_0.30pct | 2650 | 50.3 | 51.1 | $-1681.42 | -6.3% | $-681.42 | -3.4 | done | losing for real |
| coinflip | 4536 | 50.3 | 50.2 | $-1844.49 | -4.1% | $-844.49 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 3157 | 49.0 | 50.2 | $-1992.18 | -6.3% | $-992.18 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4536 | 50.3 | 51.4 | $-2754.20 | -6.1% | $-1754.20 | -4.2 | done | losing for real |
| always_up | 4536 | 47.8 | 49.3 | $-3365.45 | -7.4% | $-2365.45 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7190 | 48.4 | 49.0 | $-3620.97 |
| ETH | 7778 | 48.2 | 48.4 | $-4562.42 |
| SOL | 8166 | 48.0 | 48.4 | $-4639.14 |
| XRP | 8247 | 48.1 | 48.2 | $-4869.78 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
