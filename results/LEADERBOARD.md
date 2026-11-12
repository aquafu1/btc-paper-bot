# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 4:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 139 windows, 3488 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 242 | 62.4 | 53.1 | $+363.39 | +15.0% | $1363.39 | +2.5 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 334 | 56.9 | 52.2 | $+221.39 | +6.6% | $1221.39 | +1.3 | done | can't tell from luck |
| value_ev20 | 67 | 31.3 | 37.0 | $-135.47 | -20.2% | $864.53 | -1.4 | Sun 5:00 AM | too few trades (67/200) |
| momentum_5m_0.00pct | 548 | 52.0 | 51.1 | $-141.39 | -2.6% | $858.61 | -0.6 | done | can't tell from luck |
| coinflip | 548 | 51.8 | 51.0 | $-163.67 | -3.0% | $836.33 | -0.7 | done | can't tell from luck |
| value_ev10 | 184 | 37.5 | 40.6 | $-225.28 | -12.2% | $774.72 | -1.4 | Thu 7:15 AM | too few trades (184/200) |
| value_ev5 | 266 | 38.7 | 42.2 | $-334.16 | -12.6% | $665.84 | -1.8 | done | can't tell from luck |
| trend_filter | 175 | 40.0 | 49.1 | $-374.41 | -21.4% | $625.59 | -2.8 | Thu 9:15 AM | too few trades (175/200) |
| always_up | 548 | 47.4 | 50.1 | $-532.92 | -9.7% | $467.08 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 334 | 43.1 | 50.1 | $-554.98 | -16.6% | $445.02 | -3.1 | done | losing for real |
| momentum_60m_0.30pct | 242 | 37.6 | 49.1 | $-618.64 | -25.6% | $381.36 | -4.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 749 | 45.8 | 49.6 | $-774.66 |
| ETH | 865 | 45.1 | 48.7 | $-994.17 |
| SOL | 917 | 49.1 | 48.8 | $-517.96 |
| XRP | 957 | 50.7 | 49.1 | $-209.35 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
