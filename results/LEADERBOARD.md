# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 9:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1207 windows, 33275 settled trades, 185 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 649 | 34.5 | 35.3 | $-438.79 | -6.8% | $561.21 | -1.3 | done | can't tell from luck |
| value_ev10 | 1590 | 38.7 | 39.2 | $-794.81 | -5.0% | $205.19 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3335 | 50.8 | 50.3 | $-1077.94 | -3.2% | $-77.94 | -1.9 | done | can't tell from luck |
| value_ev5 | 2405 | 40.5 | 41.1 | $-1203.15 | -5.0% | $-203.15 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2789 | 49.4 | 49.4 | $-1308.45 | -4.7% | $-308.45 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2789 | 50.6 | 51.1 | $-1626.40 | -5.8% | $-626.40 | -3.2 | done | losing for real |
| trend_filter | 1965 | 48.7 | 50.4 | $-1683.03 | -8.6% | $-683.03 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3335 | 49.2 | 50.2 | $-2053.43 | -6.2% | $-1053.43 | -3.6 | done | losing for real |
| coinflip | 4806 | 50.1 | 50.1 | $-2148.80 | -4.5% | $-1148.80 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4806 | 50.2 | 51.4 | $-2902.99 | -6.0% | $-1902.99 | -4.3 | done | losing for real |
| always_up | 4806 | 47.9 | 49.3 | $-3472.52 | -7.2% | $-2472.52 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7673 | 48.1 | 48.9 | $-4258.18 |
| ETH | 8292 | 48.1 | 48.3 | $-4867.91 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
