# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 11:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 542 windows, 15023 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1286 | 51.6 | 49.8 | $-149.24 | -1.2% | $850.76 | -0.4 | done | can't tell from luck |
| value_ev20 | 288 | 33.7 | 35.5 | $-292.64 | -10.2% | $707.36 | -1.3 | done | can't tell from luck |
| trend_filter | 876 | 50.7 | 50.9 | $-422.46 | -4.8% | $577.54 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1524 | 49.7 | 49.7 | $-669.72 | -4.4% | $330.28 | -1.7 | done | can't tell from luck |
| value_ev10 | 705 | 37.2 | 39.6 | $-730.63 | -10.4% | $269.37 | -2.3 | done | losing for real |
| value_ev5 | 1051 | 39.4 | 41.4 | $-944.23 | -9.0% | $55.77 | -2.5 | done | losing for real |
| reversal_15m_0.10pct | 1524 | 50.3 | 51.4 | $-1064.54 | -7.0% | $-64.54 | -2.8 | done | losing for real |
| coinflip | 2161 | 49.8 | 50.6 | $-1285.31 | -5.9% | $-285.31 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1286 | 48.4 | 51.3 | $-1329.77 | -10.3% | $-329.77 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2161 | 50.1 | 51.7 | $-1549.65 | -7.2% | $-549.65 | -3.5 | done | losing for real |
| always_up | 2161 | 46.7 | 50.1 | $-2426.33 | -11.2% | $-1426.33 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3403 | 47.5 | 49.2 | $-2819.97 |
| ETH | 3757 | 47.9 | 48.6 | $-2697.83 |
| SOL | 3916 | 47.7 | 48.9 | $-3013.75 |
| XRP | 3947 | 48.5 | 48.8 | $-2332.97 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
