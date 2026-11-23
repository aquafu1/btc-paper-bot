# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 7:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1196 windows, 33031 settled trades, 66 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 645 | 34.7 | 35.3 | $-398.79 | -6.2% | $601.21 | -1.2 | done | can't tell from luck |
| value_ev10 | 1573 | 38.6 | 39.2 | $-822.09 | -5.2% | $177.91 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3309 | 50.8 | 50.3 | $-1089.77 | -3.3% | $-89.77 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2768 | 49.6 | 49.4 | $-1229.44 | -4.4% | $-229.44 | -2.3 | done | losing for real |
| value_ev5 | 2383 | 40.4 | 41.1 | $-1268.67 | -5.3% | $-268.67 | -2.2 | done | losing for real |
| trend_filter | 1948 | 48.8 | 50.5 | $-1644.02 | -8.4% | $-644.02 | -3.8 | done | losing for real |
| reversal_60m_0.30pct | 2768 | 50.4 | 51.1 | $-1696.50 | -6.1% | $-696.50 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3309 | 49.2 | 50.3 | $-2034.07 | -6.1% | $-1034.07 | -3.6 | done | losing for real |
| coinflip | 4776 | 50.1 | 50.1 | $-2117.99 | -4.4% | $-1117.99 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4776 | 50.2 | 51.4 | $-3004.24 | -6.3% | $-2004.24 | -4.5 | done | losing for real |
| always_up | 4776 | 47.8 | 49.3 | $-3579.84 | -7.5% | $-2579.84 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7583 | 48.1 | 48.9 | $-4299.57 |
| ETH | 8192 | 48.0 | 48.4 | $-5060.88 |
| SOL | 8601 | 48.2 | 48.4 | $-4418.48 |
| XRP | 8655 | 48.1 | 48.2 | $-5106.49 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
