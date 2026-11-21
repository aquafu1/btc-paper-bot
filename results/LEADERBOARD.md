# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 8:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1009 windows, 28099 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 519 | 34.1 | 35.0 | $-322.56 | -6.2% | $677.44 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 2421 | 50.2 | 49.7 | $-882.03 | -3.6% | $117.97 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 2865 | 50.9 | 50.4 | $-939.43 | -3.3% | $60.57 | -1.8 | done | can't tell from luck |
| value_ev10 | 1285 | 37.4 | 39.1 | $-942.99 | -7.3% | $57.01 | -2.1 | done | losing for real |
| trend_filter | 1686 | 49.8 | 50.8 | $-1141.58 | -6.8% | $-141.58 | -2.9 | done | losing for real |
| value_ev5 | 1947 | 39.5 | 41.0 | $-1294.73 | -6.6% | $-294.73 | -2.5 | done | losing for real |
| coinflip | 4030 | 50.5 | 50.4 | $-1658.48 | -4.1% | $-658.48 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2421 | 49.8 | 51.0 | $-1786.63 | -7.4% | $-786.63 | -3.7 | done | losing for real |
| momentum_15m_0.10pct | 2865 | 49.1 | 50.3 | $-1854.69 | -6.5% | $-854.69 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 4030 | 50.7 | 51.5 | $-2233.09 | -5.5% | $-1233.09 | -3.6 | done | losing for real |
| always_up | 4030 | 47.3 | 49.5 | $-3617.40 | -9.0% | $-2617.40 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6413 | 48.3 | 49.1 | $-3555.32 |
| ETH | 6975 | 48.1 | 48.5 | $-4399.55 |
| SOL | 7338 | 48.3 | 48.6 | $-4079.68 |
| XRP | 7373 | 48.1 | 48.4 | $-4639.06 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
