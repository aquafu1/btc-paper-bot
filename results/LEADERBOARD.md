# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 5:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 855 windows, 23616 settled trades, 29 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 443 | 34.3 | 34.8 | $-255.60 | -5.8% | $744.40 | -0.9 | done | can't tell from luck |
| value_ev10 | 1081 | 37.7 | 39.0 | $-733.94 | -6.8% | $266.06 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2001 | 50.2 | 49.7 | $-788.01 | -3.9% | $211.99 | -1.8 | done | can't tell from luck |
| trend_filter | 1391 | 50.2 | 50.9 | $-883.02 | -6.3% | $116.98 | -2.4 | done | losing for real |
| reversal_15m_0.10pct | 2411 | 50.6 | 50.5 | $-963.46 | -4.0% | $36.54 | -2.0 | done | can't tell from luck |
| value_ev5 | 1632 | 39.8 | 41.0 | $-1032.94 | -6.3% | $-32.94 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2411 | 49.4 | 50.3 | $-1399.69 | -5.8% | $-399.69 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2001 | 49.8 | 51.0 | $-1476.83 | -7.4% | $-476.83 | -3.4 | done | losing for real |
| coinflip | 3415 | 50.2 | 50.3 | $-1504.23 | -4.4% | $-504.23 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3415 | 51.3 | 51.7 | $-1560.29 | -4.6% | $-560.29 | -2.8 | done | losing for real |
| always_up | 3415 | 46.9 | 49.5 | $-3276.19 | -9.6% | $-2276.19 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5385 | 48.3 | 49.0 | $-2938.04 |
| ETH | 5878 | 48.0 | 48.5 | $-3900.50 |
| SOL | 6160 | 48.3 | 48.5 | $-3550.42 |
| XRP | 6193 | 48.3 | 48.5 | $-3485.26 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
