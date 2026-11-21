# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 9:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1012 windows, 28185 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 519 | 34.1 | 35.0 | $-322.56 | -6.2% | $677.44 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2875 | 51.0 | 50.5 | $-899.35 | -3.1% | $100.65 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2431 | 50.1 | 49.7 | $-933.06 | -3.8% | $66.94 | -1.9 | done | can't tell from luck |
| value_ev10 | 1290 | 37.3 | 39.1 | $-992.99 | -7.7% | $7.01 | -2.3 | done | losing for real |
| trend_filter | 1691 | 49.9 | 50.8 | $-1142.60 | -6.8% | $-142.60 | -2.9 | done | losing for real |
| value_ev5 | 1953 | 39.4 | 41.0 | $-1354.73 | -6.9% | $-354.73 | -2.6 | done | losing for real |
| coinflip | 4040 | 50.5 | 50.4 | $-1672.93 | -4.1% | $-672.93 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2431 | 49.9 | 51.0 | $-1754.39 | -7.2% | $-754.39 | -3.7 | done | losing for real |
| momentum_15m_0.10pct | 2875 | 49.0 | 50.3 | $-1913.56 | -6.7% | $-913.56 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4040 | 50.8 | 51.5 | $-2191.14 | -5.4% | $-1191.14 | -3.6 | done | losing for real |
| always_up | 4040 | 47.2 | 49.5 | $-3668.42 | -9.1% | $-2668.42 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6428 | 48.3 | 49.1 | $-3559.07 |
| ETH | 6999 | 48.0 | 48.5 | $-4462.65 |
| SOL | 7367 | 48.2 | 48.6 | $-4165.30 |
| XRP | 7391 | 48.1 | 48.4 | $-4658.69 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
