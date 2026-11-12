# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 11:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 167 windows, 4277 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 315 | 60.6 | 53.3 | $+350.93 | +11.1% | $1350.93 | +2.1 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 415 | 57.3 | 52.7 | $+262.84 | +6.3% | $1262.84 | +1.4 | done | can't tell from luck |
| value_ev20 | 80 | 35.0 | 37.1 | $-101.99 | -12.7% | $898.01 | -0.9 | Sun 4:45 AM | too few trades (80/200) |
| momentum_5m_0.00pct | 660 | 52.1 | 51.2 | $-144.78 | -2.2% | $855.22 | -0.6 | done | can't tell from luck |
| value_ev10 | 219 | 37.9 | 40.8 | $-261.47 | -11.9% | $738.53 | -1.5 | done | can't tell from luck |
| value_ev5 | 321 | 38.9 | 42.5 | $-401.73 | -12.5% | $598.27 | -2.0 | done | losing for real |
| coinflip | 660 | 50.0 | 51.0 | $-411.53 | -6.2% | $588.47 | -1.7 | done | can't tell from luck |
| trend_filter | 217 | 40.6 | 48.9 | $-429.61 | -19.8% | $570.39 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 415 | 42.7 | 49.5 | $-697.00 | -16.8% | $303.00 | -3.5 | done | losing for real |
| momentum_60m_0.30pct | 315 | 39.4 | 48.8 | $-702.13 | -22.3% | $297.87 | -4.0 | done | losing for real |
| always_up | 660 | 46.2 | 50.0 | $-778.53 | -11.8% | $221.47 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 928 | 46.1 | 49.5 | $-843.93 |
| ETH | 1067 | 45.6 | 48.8 | $-1197.36 |
| SOL | 1122 | 48.0 | 49.0 | $-888.20 |
| XRP | 1160 | 50.0 | 49.0 | $-385.51 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
