# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 11:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 166 windows, 4257 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 315 | 60.6 | 53.3 | $+350.93 | +11.1% | $1350.93 | +2.1 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 411 | 56.9 | 52.7 | $+222.11 | +5.4% | $1222.11 | +1.2 | done | can't tell from luck |
| value_ev20 | 80 | 35.0 | 37.1 | $-101.99 | -12.7% | $898.01 | -0.9 | Sun 4:00 AM | too few trades (80/200) |
| momentum_5m_0.00pct | 656 | 52.4 | 51.2 | $-104.78 | -1.6% | $895.22 | -0.4 | done | can't tell from luck |
| value_ev10 | 219 | 37.9 | 40.8 | $-261.47 | -11.9% | $738.53 | -1.5 | done | can't tell from luck |
| coinflip | 656 | 50.2 | 51.0 | $-390.46 | -6.0% | $609.54 | -1.6 | done | can't tell from luck |
| value_ev5 | 321 | 38.9 | 42.5 | $-401.73 | -12.5% | $598.27 | -2.0 | done | losing for real |
| trend_filter | 217 | 40.6 | 48.9 | $-429.61 | -19.8% | $570.39 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 411 | 43.1 | 49.4 | $-657.00 | -16.0% | $343.00 | -3.3 | done | losing for real |
| momentum_60m_0.30pct | 315 | 39.4 | 48.8 | $-702.13 | -22.3% | $297.87 | -4.0 | done | losing for real |
| always_up | 656 | 45.9 | 50.0 | $-819.27 | -12.5% | $180.73 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 923 | 46.0 | 49.5 | $-850.74 |
| ETH | 1062 | 45.7 | 48.8 | $-1189.19 |
| SOL | 1117 | 48.0 | 49.0 | $-883.78 |
| XRP | 1155 | 50.0 | 49.0 | $-371.70 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
