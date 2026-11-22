# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 2:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1082 windows, 29898 settled trades, 71 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 560 | 34.6 | 35.1 | $-308.28 | -5.5% | $691.72 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 3023 | 51.3 | 50.5 | $-770.27 | -2.5% | $229.73 | -1.4 | done | can't tell from luck |
| value_ev10 | 1382 | 37.8 | 39.2 | $-910.65 | -6.6% | $89.35 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 2536 | 49.7 | 49.6 | $-1136.36 | -4.5% | $-136.36 | -2.3 | done | losing for real |
| trend_filter | 1777 | 49.5 | 50.6 | $-1253.32 | -7.1% | $-253.32 | -3.0 | done | losing for real |
| value_ev5 | 2101 | 39.8 | 41.1 | $-1294.13 | -6.2% | $-294.13 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2536 | 50.3 | 51.1 | $-1615.87 | -6.4% | $-615.87 | -3.3 | done | losing for real |
| coinflip | 4320 | 50.5 | 50.3 | $-1677.23 | -3.9% | $-677.23 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 4320 | 51.0 | 51.5 | $-2039.15 | -4.7% | $-1039.15 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3023 | 48.7 | 50.3 | $-2134.61 | -7.1% | $-1134.61 | -3.9 | done | losing for real |
| always_up | 4320 | 47.4 | 49.4 | $-3650.87 | -8.5% | $-2650.87 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6823 | 48.5 | 49.0 | $-3334.82 |
| ETH | 7403 | 48.2 | 48.5 | $-4452.80 |
| SOL | 7800 | 48.1 | 48.5 | $-4380.48 |
| XRP | 7872 | 48.2 | 48.3 | $-4622.62 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
