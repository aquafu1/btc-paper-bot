# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 12:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1409 windows, 36247 settled trades, 403 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 726 | 34.8 | 35.3 | $-452.49 | -6.2% | $547.51 | -1.3 | done | can't tell from luck |
| value_ev10 | 1754 | 39.0 | 39.2 | $-707.69 | -4.0% | $292.31 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 3623 | 50.8 | 50.1 | $-1013.97 | -2.8% | $-13.97 | -1.7 | done | can't tell from luck |
| value_ev5 | 2649 | 40.8 | 41.1 | $-1141.65 | -4.3% | $-141.65 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 3043 | 49.3 | 49.3 | $-1416.79 | -4.7% | $-416.79 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 3043 | 50.7 | 51.0 | $-1591.12 | -5.2% | $-591.12 | -3.0 | done | losing for real |
| trend_filter | 2156 | 48.6 | 50.3 | $-1867.18 | -8.7% | $-867.18 | -4.1 | done | losing for real |
| coinflip | 5210 | 50.0 | 50.0 | $-2205.39 | -4.2% | $-1205.39 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3623 | 49.2 | 50.2 | $-2208.56 | -6.1% | $-1208.56 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 5210 | 50.1 | 51.3 | $-3221.02 | -6.2% | $-2221.02 | -4.6 | done | losing for real |
| always_up | 5210 | 48.0 | 49.3 | $-3594.40 | -6.9% | $-2594.40 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9124 | 48.1 | 48.8 | $-4782.75 |
| ETH | 9813 | 48.1 | 48.0 | $-5053.28 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
