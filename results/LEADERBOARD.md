# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 10:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1594 windows, 38656 settled trades, 415 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 814 | 34.5 | 35.1 | $-575.00 | -7.1% | $425.00 | -1.5 | done | can't tell from luck |
| value_ev10 | 1923 | 38.5 | 39.0 | $-1009.67 | -5.3% | $-9.67 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3816 | 50.9 | 50.0 | $-1013.04 | -2.7% | $-13.04 | -1.6 | done | can't tell from luck |
| value_ev5 | 2886 | 40.5 | 41.0 | $-1450.38 | -5.0% | $-450.38 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3197 | 51.0 | 50.9 | $-1471.17 | -4.6% | $-471.17 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3197 | 49.0 | 49.2 | $-1725.71 | -5.4% | $-725.71 | -3.0 | done | losing for real |
| trend_filter | 2273 | 48.4 | 50.3 | $-2036.82 | -9.0% | $-1036.82 | -4.4 | done | losing for real |
| coinflip | 5578 | 50.1 | 49.9 | $-2288.56 | -4.1% | $-1288.56 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3816 | 49.1 | 50.2 | $-2346.54 | -6.1% | $-1346.54 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5578 | 50.1 | 51.3 | $-3518.92 | -6.3% | $-2518.92 | -4.8 | done | losing for real |
| always_up | 5578 | 48.2 | 49.1 | $-3557.75 | -6.4% | $-2557.75 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10263 | 48.0 | 48.6 | $-5760.19 |
| ETH | 11083 | 48.0 | 47.7 | $-5649.15 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
