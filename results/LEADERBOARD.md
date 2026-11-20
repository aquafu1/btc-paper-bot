# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 1:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 886 windows, 24469 settled trades, 37 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 461 | 35.6 | 34.9 | $-99.37 | -2.2% | $900.63 | -0.3 | done | can't tell from luck |
| value_ev10 | 1123 | 38.3 | 39.1 | $-591.54 | -5.3% | $408.46 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 2069 | 50.0 | 49.8 | $-900.72 | -4.4% | $99.28 | -2.0 | done | can't tell from luck |
| trend_filter | 1441 | 50.2 | 50.9 | $-931.24 | -6.5% | $68.76 | -2.5 | done | losing for real |
| value_ev5 | 1698 | 39.9 | 41.0 | $-1018.51 | -6.0% | $-18.51 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2497 | 50.5 | 50.4 | $-1019.67 | -4.1% | $-19.67 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 2497 | 49.5 | 50.4 | $-1381.95 | -5.5% | $-381.95 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2069 | 50.0 | 50.9 | $-1387.03 | -6.7% | $-387.03 | -3.1 | done | losing for real |
| coinflip | 3538 | 50.3 | 50.3 | $-1541.32 | -4.4% | $-541.32 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3538 | 51.3 | 51.7 | $-1566.80 | -4.4% | $-566.80 | -2.7 | done | losing for real |
| always_up | 3538 | 46.9 | 49.6 | $-3502.16 | -9.9% | $-2502.16 | -5.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5579 | 48.3 | 49.1 | $-3050.03 |
| ETH | 6089 | 48.2 | 48.5 | $-3772.28 |
| SOL | 6383 | 48.3 | 48.5 | $-3563.82 |
| XRP | 6418 | 48.4 | 48.5 | $-3554.19 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
