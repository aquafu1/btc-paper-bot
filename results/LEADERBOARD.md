# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 2:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 841 windows, 23137 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 424 | 33.0 | 34.9 | $-410.80 | -9.7% | $589.20 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 1950 | 50.0 | 49.7 | $-881.18 | -4.5% | $118.82 | -2.0 | done | losing for real |
| value_ev10 | 1053 | 37.2 | 39.2 | $-890.49 | -8.5% | $109.51 | -2.2 | done | losing for real |
| reversal_15m_0.10pct | 2363 | 50.9 | 50.6 | $-894.63 | -3.8% | $105.37 | -1.9 | done | can't tell from luck |
| trend_filter | 1360 | 49.9 | 50.9 | $-962.96 | -7.1% | $37.04 | -2.7 | done | losing for real |
| value_ev5 | 1597 | 39.6 | 41.1 | $-1173.03 | -7.3% | $-173.03 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1950 | 50.0 | 51.1 | $-1412.83 | -7.2% | $-412.83 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 2363 | 49.1 | 50.3 | $-1483.78 | -6.3% | $-483.78 | -3.1 | done | losing for real |
| coinflip | 3359 | 50.3 | 50.3 | $-1502.15 | -4.5% | $-502.15 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3359 | 51.2 | 51.7 | $-1606.67 | -4.8% | $-606.67 | -2.9 | done | losing for real |
| always_up | 3359 | 47.1 | 49.6 | $-3184.69 | -9.5% | $-2184.69 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5256 | 48.0 | 49.1 | $-3418.97 |
| ETH | 5764 | 48.0 | 48.5 | $-4007.01 |
| SOL | 6036 | 48.2 | 48.6 | $-3621.26 |
| XRP | 6081 | 48.4 | 48.5 | $-3355.96 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
