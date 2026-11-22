# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 2:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1081 windows, 29887 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 560 | 34.6 | 35.1 | $-308.28 | -5.5% | $691.72 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 3022 | 51.3 | 50.5 | $-760.27 | -2.5% | $239.73 | -1.4 | done | can't tell from luck |
| value_ev10 | 1382 | 37.8 | 39.2 | $-910.65 | -6.6% | $89.35 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 2536 | 49.7 | 49.6 | $-1136.36 | -4.5% | $-136.36 | -2.3 | done | losing for real |
| trend_filter | 1777 | 49.5 | 50.6 | $-1253.32 | -7.1% | $-253.32 | -3.0 | done | losing for real |
| value_ev5 | 2101 | 39.8 | 41.1 | $-1294.13 | -6.2% | $-294.13 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2536 | 50.3 | 51.1 | $-1615.87 | -6.4% | $-615.87 | -3.3 | done | losing for real |
| coinflip | 4317 | 50.5 | 50.3 | $-1667.73 | -3.9% | $-667.73 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 4317 | 51.1 | 51.5 | $-2009.15 | -4.7% | $-1009.15 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3022 | 48.7 | 50.3 | $-2146.71 | -7.1% | $-1146.71 | -3.9 | done | losing for real |
| always_up | 4317 | 47.3 | 49.4 | $-3681.90 | -8.5% | $-2681.90 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6823 | 48.5 | 49.0 | $-3334.82 |
| ETH | 7398 | 48.2 | 48.5 | $-4447.00 |
| SOL | 7797 | 48.1 | 48.5 | $-4391.49 |
| XRP | 7869 | 48.3 | 48.3 | $-4611.06 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
