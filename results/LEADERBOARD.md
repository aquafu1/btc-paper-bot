# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 8:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 576 windows, 15937 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1354 | 51.3 | 49.7 | $-208.07 | -1.5% | $791.93 | -0.6 | done | can't tell from luck |
| value_ev20 | 310 | 33.5 | 35.2 | $-314.56 | -10.1% | $685.44 | -1.4 | done | can't tell from luck |
| trend_filter | 923 | 50.7 | 51.1 | $-464.64 | -5.0% | $535.36 | -1.6 | done | can't tell from luck |
| value_ev10 | 749 | 37.7 | 39.4 | $-677.94 | -9.1% | $322.06 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1619 | 51.1 | 51.0 | $-733.21 | -4.5% | $266.79 | -1.9 | done | can't tell from luck |
| value_ev5 | 1121 | 40.1 | 41.3 | $-823.91 | -7.3% | $176.09 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 1619 | 48.9 | 49.9 | $-986.94 | -6.1% | $13.06 | -2.5 | done | losing for real |
| coinflip | 2296 | 49.9 | 50.5 | $-1226.02 | -5.3% | $-226.02 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1354 | 48.7 | 51.2 | $-1343.84 | -9.9% | $-343.84 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2296 | 50.3 | 51.9 | $-1593.63 | -6.9% | $-593.63 | -3.5 | done | losing for real |
| always_up | 2296 | 47.2 | 49.9 | $-2234.22 | -9.7% | $-1234.22 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3610 | 47.8 | 49.3 | $-2622.63 |
| ETH | 3976 | 48.0 | 48.6 | $-2699.80 |
| SOL | 4151 | 47.8 | 48.8 | $-3073.46 |
| XRP | 4200 | 48.5 | 48.6 | $-2211.08 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
