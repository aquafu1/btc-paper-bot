# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 8:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1008 windows, 28050 settled trades, 68 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 518 | 34.2 | 35.0 | $-312.56 | -6.0% | $687.44 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 2415 | 50.2 | 49.7 | $-905.15 | -3.7% | $94.85 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 2859 | 51.0 | 50.4 | $-915.32 | -3.2% | $84.68 | -1.7 | done | can't tell from luck |
| value_ev10 | 1283 | 37.5 | 39.1 | $-922.99 | -7.2% | $77.01 | -2.1 | done | losing for real |
| trend_filter | 1684 | 49.9 | 50.8 | $-1121.58 | -6.7% | $-121.58 | -2.8 | done | losing for real |
| value_ev5 | 1945 | 39.6 | 41.0 | $-1274.73 | -6.6% | $-274.73 | -2.4 | done | losing for real |
| coinflip | 4024 | 50.5 | 50.4 | $-1655.08 | -4.1% | $-655.08 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2415 | 49.8 | 51.0 | $-1762.52 | -7.3% | $-762.52 | -3.7 | done | losing for real |
| momentum_15m_0.10pct | 2859 | 49.0 | 50.3 | $-1877.81 | -6.6% | $-877.81 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 4024 | 50.8 | 51.5 | $-2173.09 | -5.4% | $-1173.09 | -3.5 | done | losing for real |
| always_up | 4024 | 47.2 | 49.5 | $-3640.51 | -9.0% | $-2640.51 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6396 | 48.3 | 49.0 | $-3523.44 |
| ETH | 6968 | 48.1 | 48.5 | $-4393.04 |
| SOL | 7331 | 48.3 | 48.6 | $-4067.09 |
| XRP | 7355 | 48.1 | 48.4 | $-4577.77 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
