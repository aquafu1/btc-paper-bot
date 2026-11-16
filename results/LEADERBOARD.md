# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 11:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 541 windows, 14996 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1283 | 51.6 | 49.8 | $-132.34 | -1.0% | $867.66 | -0.4 | done | can't tell from luck |
| value_ev20 | 287 | 33.8 | 35.5 | $-282.64 | -9.8% | $717.36 | -1.3 | done | can't tell from luck |
| trend_filter | 873 | 50.7 | 50.9 | $-405.56 | -4.6% | $594.44 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1522 | 49.8 | 49.7 | $-649.72 | -4.3% | $350.28 | -1.7 | done | can't tell from luck |
| value_ev10 | 703 | 37.3 | 39.7 | $-710.63 | -10.1% | $289.37 | -2.2 | done | losing for real |
| value_ev5 | 1049 | 39.5 | 41.4 | $-924.23 | -8.8% | $75.77 | -2.5 | done | losing for real |
| reversal_15m_0.10pct | 1522 | 50.2 | 51.3 | $-1074.79 | -7.1% | $-74.79 | -2.8 | done | losing for real |
| coinflip | 2158 | 49.9 | 50.6 | $-1255.31 | -5.8% | $-255.31 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1283 | 48.4 | 51.3 | $-1330.02 | -10.4% | $-330.02 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2158 | 50.1 | 51.7 | $-1532.75 | -7.1% | $-532.75 | -3.4 | done | losing for real |
| always_up | 2158 | 46.8 | 50.1 | $-2409.43 | -11.2% | $-1409.43 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3395 | 47.5 | 49.2 | $-2770.90 |
| ETH | 3738 | 48.0 | 48.7 | $-2589.81 |
| SOL | 3916 | 47.7 | 48.9 | $-3013.75 |
| XRP | 3947 | 48.5 | 48.8 | $-2332.97 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
