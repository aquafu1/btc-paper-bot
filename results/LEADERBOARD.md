# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 1:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 596 windows, 16494 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1397 | 51.3 | 49.6 | $-181.37 | -1.3% | $818.63 | -0.5 | done | can't tell from luck |
| value_ev20 | 323 | 34.4 | 35.2 | $-232.82 | -7.2% | $767.18 | -1.0 | done | can't tell from luck |
| trend_filter | 955 | 50.3 | 50.9 | $-536.54 | -5.6% | $463.46 | -1.8 | done | can't tell from luck |
| value_ev10 | 775 | 38.2 | 39.4 | $-548.90 | -7.1% | $451.10 | -1.6 | done | can't tell from luck |
| value_ev5 | 1159 | 40.6 | 41.2 | $-633.37 | -5.5% | $366.63 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1677 | 50.8 | 51.0 | $-797.40 | -4.8% | $202.60 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1677 | 49.2 | 49.9 | $-935.66 | -5.6% | $64.34 | -2.3 | done | losing for real |
| coinflip | 2378 | 50.0 | 50.5 | $-1163.62 | -4.9% | $-163.62 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1397 | 48.7 | 51.4 | $-1360.83 | -9.7% | $-360.83 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2378 | 50.3 | 51.8 | $-1551.31 | -6.5% | $-551.31 | -3.3 | done | losing for real |
| always_up | 2378 | 47.1 | 49.8 | $-2235.82 | -9.4% | $-1235.82 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3751 | 48.0 | 49.2 | $-2435.00 |
| ETH | 4116 | 48.0 | 48.6 | $-2607.29 |
| SOL | 4285 | 47.9 | 48.7 | $-2881.40 |
| XRP | 4342 | 48.5 | 48.6 | $-2253.96 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
