# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 11:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 168 windows, 4302 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 316 | 60.4 | 53.3 | $+340.93 | +10.8% | $1340.93 | +2.1 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 419 | 57.8 | 52.7 | $+299.12 | +7.1% | $1299.12 | +1.5 | done | can't tell from luck |
| value_ev20 | 80 | 35.0 | 37.1 | $-101.99 | -12.7% | $898.01 | -0.9 | Sun 5:15 AM | too few trades (80/200) |
| momentum_5m_0.00pct | 664 | 52.4 | 51.2 | $-108.50 | -1.6% | $891.50 | -0.4 | done | can't tell from luck |
| value_ev10 | 219 | 37.9 | 40.8 | $-261.47 | -11.9% | $738.53 | -1.5 | done | can't tell from luck |
| value_ev5 | 322 | 38.8 | 42.5 | $-411.73 | -12.8% | $588.27 | -2.1 | done | losing for real |
| trend_filter | 219 | 41.1 | 48.9 | $-412.69 | -18.8% | $587.31 | -2.8 | done | losing for real |
| coinflip | 664 | 50.0 | 51.0 | $-413.51 | -6.2% | $586.49 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 316 | 39.6 | 48.8 | $-693.80 | -22.0% | $306.20 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 419 | 42.2 | 49.5 | $-737.00 | -17.6% | $263.00 | -3.6 | done | losing for real |
| always_up | 664 | 45.9 | 50.0 | $-818.53 | -12.3% | $181.47 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 933 | 46.1 | 49.5 | $-854.57 |
| ETH | 1072 | 45.7 | 48.8 | $-1188.32 |
| SOL | 1130 | 48.1 | 49.0 | $-876.53 |
| XRP | 1167 | 50.0 | 49.0 | $-399.75 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
