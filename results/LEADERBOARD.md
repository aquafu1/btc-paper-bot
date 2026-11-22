# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 11:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1118 windows, 30934 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 591 | 34.5 | 35.1 | $-359.77 | -6.1% | $640.23 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3119 | 51.1 | 50.5 | $-858.91 | -2.8% | $141.09 | -1.5 | done | can't tell from luck |
| value_ev10 | 1444 | 38.0 | 39.2 | $-910.86 | -6.3% | $89.14 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 2625 | 49.8 | 49.4 | $-1077.73 | -4.1% | $-77.73 | -2.1 | done | losing for real |
| value_ev5 | 2185 | 40.0 | 41.0 | $-1276.70 | -5.8% | $-276.70 | -2.3 | done | losing for real |
| trend_filter | 1834 | 49.2 | 50.4 | $-1391.61 | -7.6% | $-391.61 | -3.3 | done | losing for real |
| reversal_60m_0.30pct | 2625 | 50.2 | 51.1 | $-1707.54 | -6.5% | $-707.54 | -3.4 | done | losing for real |
| coinflip | 4464 | 50.4 | 50.2 | $-1771.82 | -4.0% | $-771.82 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 3119 | 48.9 | 50.2 | $-2052.07 | -6.6% | $-1052.07 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4464 | 50.5 | 51.4 | $-2530.25 | -5.7% | $-1530.25 | -3.9 | done | losing for real |
| always_up | 4464 | 47.7 | 49.3 | $-3452.97 | -7.7% | $-2452.97 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7087 | 48.3 | 49.0 | $-3616.45 |
| ETH | 7662 | 48.1 | 48.4 | $-4650.24 |
| SOL | 8048 | 48.0 | 48.4 | $-4540.72 |
| XRP | 8137 | 48.2 | 48.2 | $-4582.85 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
