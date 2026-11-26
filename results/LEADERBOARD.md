# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 5:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1479 windows, 37175 settled trades, 367 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 754 | 34.4 | 35.4 | $-573.12 | -7.6% | $426.88 | -1.6 | done | can't tell from luck |
| value_ev10 | 1811 | 38.5 | 39.2 | $-939.91 | -5.2% | $60.09 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3704 | 50.9 | 50.1 | $-1008.14 | -2.7% | $-8.14 | -1.7 | done | can't tell from luck |
| value_ev5 | 2731 | 40.5 | 41.1 | $-1402.02 | -5.1% | $-402.02 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3110 | 50.9 | 51.0 | $-1530.25 | -4.9% | $-530.25 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 3110 | 49.1 | 49.3 | $-1590.88 | -5.1% | $-590.88 | -2.8 | done | losing for real |
| trend_filter | 2207 | 48.6 | 50.3 | $-1918.00 | -8.7% | $-918.00 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3704 | 49.1 | 50.2 | $-2274.70 | -6.1% | $-1274.70 | -3.8 | done | losing for real |
| coinflip | 5348 | 49.9 | 50.0 | $-2406.06 | -4.5% | $-1406.06 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5348 | 50.1 | 51.3 | $-3417.43 | -6.4% | $-2417.43 | -4.8 | done | losing for real |
| always_up | 5348 | 48.1 | 49.2 | $-3526.01 | -6.6% | $-2526.01 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9577 | 48.0 | 48.7 | $-5217.35 |
| ETH | 10288 | 47.9 | 48.0 | $-5784.93 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
