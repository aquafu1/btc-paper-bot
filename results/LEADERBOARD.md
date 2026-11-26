# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 4:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1521 windows, 37674 settled trades, 383 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 765 | 34.6 | 35.4 | $-536.35 | -7.0% | $463.65 | -1.5 | done | can't tell from luck |
| value_ev10 | 1842 | 38.7 | 39.2 | $-921.56 | -5.0% | $78.44 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3744 | 51.0 | 50.1 | $-938.53 | -2.5% | $61.47 | -1.5 | done | can't tell from luck |
| value_ev5 | 2779 | 40.6 | 41.1 | $-1336.18 | -4.8% | $-336.18 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3138 | 51.1 | 51.0 | $-1426.82 | -4.5% | $-426.82 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3138 | 48.9 | 49.2 | $-1716.88 | -5.5% | $-716.88 | -3.0 | done | losing for real |
| trend_filter | 2228 | 48.5 | 50.3 | $-1932.55 | -8.7% | $-932.55 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3744 | 49.0 | 50.2 | $-2333.97 | -6.2% | $-1333.97 | -3.8 | done | losing for real |
| coinflip | 5432 | 50.0 | 50.0 | $-2371.98 | -4.4% | $-1371.98 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5432 | 50.1 | 51.3 | $-3376.16 | -6.2% | $-2376.16 | -4.7 | done | losing for real |
| always_up | 5432 | 48.1 | 49.2 | $-3520.68 | -6.5% | $-2520.68 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9807 | 48.0 | 48.7 | $-5446.33 |
| ETH | 10557 | 48.1 | 47.9 | $-5381.12 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
