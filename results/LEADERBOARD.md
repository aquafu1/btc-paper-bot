# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 9:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 246 windows, 6428 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 633 | 56.1 | 52.2 | $+217.29 | +3.4% | $1217.29 | +0.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 508 | 54.1 | 52.2 | $-5.99 | -0.1% | $994.01 | -0.0 | done | can't tell from luck |
| value_ev20 | 114 | 34.2 | 36.7 | $-120.27 | -10.6% | $879.73 | -0.9 | Sun 11:15 AM | too few trades (114/200) |
| value_ev10 | 310 | 37.1 | 40.9 | $-393.26 | -12.7% | $606.74 | -1.9 | done | can't tell from luck |
| trend_filter | 338 | 45.3 | 50.4 | $-476.38 | -14.1% | $523.62 | -2.7 | done | losing for real |
| value_ev5 | 456 | 39.5 | 42.6 | $-515.11 | -11.3% | $484.89 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 508 | 45.9 | 49.9 | $-629.55 | -12.4% | $370.45 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 976 | 49.9 | 51.6 | $-713.75 | -7.3% | $286.25 | -2.4 | done | losing for real |
| coinflip | 976 | 49.2 | 50.9 | $-753.99 | -7.7% | $246.01 | -2.5 | done | losing for real |
| momentum_15m_0.10pct | 633 | 43.9 | 49.9 | $-991.59 | -15.7% | $8.41 | -4.0 | done | losing for real |
| always_up | 976 | 47.1 | 50.5 | $-1073.69 | -11.0% | $-73.69 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1438 | 46.4 | 49.8 | $-1523.71 |
| ETH | 1603 | 46.6 | 49.1 | $-1670.98 |
| SOL | 1663 | 48.2 | 49.4 | $-1331.24 |
| XRP | 1724 | 48.7 | 49.2 | $-930.37 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
