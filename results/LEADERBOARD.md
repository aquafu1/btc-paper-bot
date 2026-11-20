# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 6:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 907 windows, 25053 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 468 | 35.3 | 34.9 | $-141.30 | -3.0% | $858.70 | -0.5 | done | can't tell from luck |
| value_ev10 | 1148 | 38.2 | 39.1 | $-613.08 | -5.3% | $386.92 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2120 | 49.9 | 49.8 | $-976.46 | -4.6% | $23.54 | -2.1 | done | losing for real |
| value_ev5 | 1735 | 39.9 | 41.0 | $-997.46 | -5.7% | $2.54 | -2.0 | done | losing for real |
| reversal_15m_0.10pct | 2555 | 50.5 | 50.5 | $-1037.87 | -4.1% | $-37.87 | -2.1 | done | losing for real |
| trend_filter | 1486 | 49.8 | 51.0 | $-1046.14 | -7.0% | $-46.14 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2120 | 50.1 | 50.9 | $-1347.83 | -6.4% | $-347.83 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2555 | 49.5 | 50.3 | $-1387.49 | -5.4% | $-387.49 | -2.8 | done | losing for real |
| coinflip | 3622 | 50.2 | 50.3 | $-1603.83 | -4.4% | $-603.83 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3622 | 51.1 | 51.6 | $-1711.31 | -4.7% | $-711.31 | -2.9 | done | losing for real |
| always_up | 3622 | 46.9 | 49.7 | $-3588.85 | -9.9% | $-2588.85 | -6.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5706 | 48.2 | 49.1 | $-3127.98 |
| ETH | 6234 | 48.2 | 48.5 | $-3842.34 |
| SOL | 6540 | 48.1 | 48.6 | $-3796.11 |
| XRP | 6573 | 48.3 | 48.5 | $-3685.19 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
