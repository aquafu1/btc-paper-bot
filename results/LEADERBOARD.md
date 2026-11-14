# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 7:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 287 windows, 7597 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 749 | 54.2 | 51.8 | $+19.24 | +0.3% | $1019.24 | +0.1 | done | can't tell from luck |
| value_ev20 | 141 | 35.5 | 36.4 | $-115.17 | -8.2% | $884.83 | -0.8 | Sun 4:00 AM | too few trades (141/200) |
| reversal_60m_0.30pct | 610 | 52.3 | 51.8 | $-209.74 | -3.4% | $790.26 | -0.9 | done | can't tell from luck |
| value_ev10 | 368 | 38.3 | 40.5 | $-350.85 | -9.5% | $649.15 | -1.6 | done | can't tell from luck |
| trend_filter | 404 | 46.8 | 50.4 | $-476.66 | -11.8% | $523.34 | -2.4 | done | losing for real |
| value_ev5 | 543 | 40.0 | 42.2 | $-519.38 | -9.6% | $480.62 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 610 | 47.7 | 49.8 | $-557.45 | -9.1% | $442.55 | -2.3 | done | losing for real |
| coinflip | 1141 | 50.0 | 50.9 | $-676.80 | -5.9% | $323.20 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1141 | 49.6 | 51.5 | $-881.97 | -7.7% | $118.03 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 749 | 45.8 | 49.9 | $-926.62 | -12.4% | $73.38 | -3.4 | done | losing for real |
| always_up | 1141 | 47.6 | 50.2 | $-1079.22 | -9.5% | $-79.22 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1696 | 46.9 | 49.4 | $-1509.76 |
| ETH | 1895 | 47.2 | 48.8 | $-1720.83 |
| SOL | 1973 | 48.3 | 49.3 | $-1525.15 |
| XRP | 2033 | 48.8 | 49.0 | $-1018.88 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
