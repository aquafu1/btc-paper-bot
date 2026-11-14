# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 4:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 370 windows, 10013 settled trades, 69 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 189 | 38.1 | 36.4 | $+15.78 | +0.8% | $1015.78 | +0.1 | Sat 10:00 PM | too few trades (189/200) |
| value_ev10 | 485 | 41.0 | 40.4 | $-86.39 | -1.8% | $913.61 | -0.3 | done | can't tell from luck |
| value_ev5 | 717 | 42.3 | 42.1 | $-226.26 | -3.2% | $773.74 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 829 | 49.7 | 49.8 | $-372.37 | -4.5% | $627.63 | -1.3 | done | can't tell from luck |
| trend_filter | 554 | 48.9 | 50.5 | $-408.83 | -7.4% | $591.17 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 997 | 51.5 | 52.1 | $-517.22 | -5.2% | $482.78 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 997 | 48.5 | 49.7 | $-583.32 | -5.9% | $416.68 | -1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 829 | 50.3 | 52.0 | $-596.24 | -7.2% | $403.76 | -2.2 | done | losing for real |
| coinflip | 1472 | 49.7 | 50.8 | $-841.43 | -5.7% | $158.57 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1472 | 49.5 | 51.5 | $-1082.53 | -7.4% | $-82.53 | -2.9 | done | losing for real |
| always_up | 1472 | 45.6 | 50.7 | $-2006.53 | -13.6% | $-1006.53 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2251 | 47.4 | 49.4 | $-1773.68 |
| ETH | 2518 | 47.7 | 48.9 | $-1775.43 |
| SOL | 2594 | 48.0 | 49.4 | $-1858.06 |
| XRP | 2650 | 48.8 | 49.1 | $-1298.17 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
