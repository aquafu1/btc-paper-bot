# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 10:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 777 windows, 21429 settled trades, 65 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 404 | 32.9 | 34.9 | $-391.45 | -9.7% | $608.55 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 2188 | 51.1 | 50.6 | $-695.22 | -3.2% | $304.78 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 1812 | 49.9 | 49.6 | $-735.31 | -4.1% | $264.69 | -1.7 | done | can't tell from luck |
| value_ev10 | 980 | 37.4 | 39.1 | $-754.62 | -7.7% | $245.38 | -2.0 | done | can't tell from luck |
| trend_filter | 1262 | 50.1 | 50.8 | $-774.98 | -6.1% | $225.02 | -2.2 | done | losing for real |
| value_ev5 | 1483 | 39.8 | 41.0 | $-985.88 | -6.6% | $14.12 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1812 | 50.1 | 51.2 | $-1229.11 | -6.8% | $-229.11 | -2.9 | done | losing for real |
| coinflip | 3100 | 50.2 | 50.3 | $-1313.67 | -4.2% | $-313.67 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 2188 | 48.9 | 50.2 | $-1425.49 | -6.5% | $-425.49 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 3100 | 51.2 | 51.6 | $-1441.71 | -4.7% | $-441.71 | -2.7 | done | losing for real |
| always_up | 3100 | 47.2 | 49.5 | $-2797.05 | -9.0% | $-1797.05 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4867 | 48.2 | 49.1 | $-2920.38 |
| ETH | 5351 | 48.0 | 48.5 | $-3575.24 |
| SOL | 5577 | 48.1 | 48.6 | $-3256.35 |
| XRP | 5634 | 48.5 | 48.5 | $-2792.52 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
