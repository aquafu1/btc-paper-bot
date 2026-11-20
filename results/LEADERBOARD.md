# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 1:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 887 windows, 24494 settled trades, 32 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 461 | 35.6 | 34.9 | $-99.37 | -2.2% | $900.63 | -0.3 | done | can't tell from luck |
| value_ev10 | 1124 | 38.3 | 39.1 | $-601.54 | -5.4% | $398.46 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2070 | 50.0 | 49.8 | $-910.72 | -4.4% | $89.28 | -2.0 | done | losing for real |
| trend_filter | 1444 | 50.1 | 51.0 | $-961.24 | -6.7% | $38.76 | -2.6 | done | losing for real |
| reversal_15m_0.10pct | 2500 | 50.5 | 50.4 | $-1008.29 | -4.0% | $-8.29 | -2.0 | done | losing for real |
| value_ev5 | 1699 | 39.8 | 41.0 | $-1028.51 | -6.1% | $-28.51 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 2070 | 50.0 | 50.9 | $-1376.55 | -6.6% | $-376.55 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2500 | 49.5 | 50.4 | $-1391.37 | -5.6% | $-391.37 | -2.8 | done | losing for real |
| coinflip | 3542 | 50.3 | 50.3 | $-1519.45 | -4.3% | $-519.45 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3542 | 51.3 | 51.7 | $-1606.80 | -4.5% | $-606.80 | -2.8 | done | losing for real |
| always_up | 3542 | 46.9 | 49.6 | $-3500.78 | -9.9% | $-2500.78 | -5.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5579 | 48.3 | 49.1 | $-3050.03 |
| ETH | 6102 | 48.2 | 48.5 | $-3806.56 |
| SOL | 6395 | 48.2 | 48.5 | $-3593.84 |
| XRP | 6418 | 48.4 | 48.5 | $-3554.19 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
