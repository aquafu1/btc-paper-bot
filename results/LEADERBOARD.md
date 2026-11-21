# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 9:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1013 windows, 28212 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 519 | 34.1 | 35.0 | $-322.56 | -6.2% | $677.44 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2876 | 51.0 | 50.5 | $-891.88 | -3.1% | $108.12 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2433 | 50.1 | 49.7 | $-953.06 | -3.9% | $46.94 | -1.9 | done | can't tell from luck |
| value_ev10 | 1292 | 37.2 | 39.1 | $-1012.99 | -7.8% | $-12.99 | -2.3 | done | losing for real |
| trend_filter | 1692 | 49.9 | 50.8 | $-1137.03 | -6.7% | $-137.03 | -2.8 | done | losing for real |
| value_ev5 | 1956 | 39.4 | 41.0 | $-1384.73 | -7.1% | $-384.73 | -2.6 | done | losing for real |
| coinflip | 4045 | 50.5 | 50.4 | $-1687.69 | -4.2% | $-687.69 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2433 | 49.9 | 51.0 | $-1738.83 | -7.1% | $-738.83 | -3.6 | done | losing for real |
| momentum_15m_0.10pct | 2876 | 49.0 | 50.3 | $-1923.56 | -6.7% | $-923.56 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4045 | 50.8 | 51.6 | $-2155.36 | -5.3% | $-1155.36 | -3.5 | done | losing for real |
| always_up | 4045 | 47.3 | 49.5 | $-3632.64 | -9.0% | $-2632.64 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6436 | 48.3 | 49.1 | $-3531.47 |
| ETH | 7008 | 48.1 | 48.5 | $-4465.31 |
| SOL | 7371 | 48.2 | 48.6 | $-4171.54 |
| XRP | 7397 | 48.1 | 48.4 | $-4671.99 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
