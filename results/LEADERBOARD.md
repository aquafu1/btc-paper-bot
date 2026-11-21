# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 8:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1010 windows, 28118 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 519 | 34.1 | 35.0 | $-322.56 | -6.2% | $677.44 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 2423 | 50.2 | 49.7 | $-902.03 | -3.7% | $97.97 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 2867 | 51.0 | 50.4 | $-923.01 | -3.2% | $76.99 | -1.7 | done | can't tell from luck |
| value_ev10 | 1287 | 37.4 | 39.1 | $-962.99 | -7.5% | $37.01 | -2.2 | done | losing for real |
| trend_filter | 1687 | 49.8 | 50.8 | $-1151.58 | -6.8% | $-151.58 | -2.9 | done | losing for real |
| value_ev5 | 1949 | 39.5 | 41.0 | $-1314.73 | -6.7% | $-314.73 | -2.5 | done | losing for real |
| coinflip | 4032 | 50.5 | 50.4 | $-1659.70 | -4.1% | $-659.70 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2423 | 49.8 | 51.0 | $-1770.21 | -7.3% | $-770.21 | -3.7 | done | losing for real |
| momentum_15m_0.10pct | 2867 | 49.0 | 50.3 | $-1874.69 | -6.5% | $-874.69 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 4032 | 50.7 | 51.5 | $-2234.31 | -5.5% | $-1234.31 | -3.6 | done | losing for real |
| always_up | 4032 | 47.2 | 49.5 | $-3637.40 | -9.0% | $-2637.40 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6413 | 48.3 | 49.1 | $-3555.32 |
| ETH | 6984 | 48.1 | 48.5 | $-4414.43 |
| SOL | 7348 | 48.2 | 48.6 | $-4144.39 |
| XRP | 7373 | 48.1 | 48.4 | $-4639.06 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
