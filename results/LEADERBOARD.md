# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 3:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1183 windows, 32702 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 638 | 35.0 | 35.3 | $-353.40 | -5.5% | $646.60 | -1.1 | done | can't tell from luck |
| value_ev10 | 1550 | 38.6 | 39.2 | $-765.47 | -4.9% | $234.53 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3277 | 50.7 | 50.3 | $-1090.31 | -3.3% | $-90.31 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2754 | 49.6 | 49.4 | $-1205.21 | -4.4% | $-205.21 | -2.3 | done | losing for real |
| value_ev5 | 2345 | 40.3 | 41.1 | $-1233.78 | -5.3% | $-233.78 | -2.2 | done | losing for real |
| trend_filter | 1935 | 48.9 | 50.5 | $-1585.94 | -8.2% | $-585.94 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2754 | 50.4 | 51.1 | $-1698.23 | -6.2% | $-698.23 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3277 | 49.3 | 50.2 | $-1971.14 | -6.0% | $-971.14 | -3.5 | done | losing for real |
| coinflip | 4724 | 50.0 | 50.1 | $-2151.00 | -4.6% | $-1151.00 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4724 | 50.1 | 51.4 | $-2997.49 | -6.3% | $-1997.49 | -4.5 | done | losing for real |
| always_up | 4724 | 47.9 | 49.3 | $-3376.75 | -7.1% | $-2376.75 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7501 | 48.2 | 48.9 | $-4104.89 |
| ETH | 8109 | 48.1 | 48.4 | $-4863.90 |
| SOL | 8505 | 48.2 | 48.4 | $-4400.44 |
| XRP | 8587 | 48.1 | 48.2 | $-5059.49 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
