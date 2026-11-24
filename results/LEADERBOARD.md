# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 6:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1242 windows, 33790 settled trades, 412 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 664 | 34.2 | 35.3 | $-514.16 | -7.7% | $485.84 | -1.5 | done | can't tell from luck |
| value_ev10 | 1620 | 38.5 | 39.2 | $-860.67 | -5.3% | $139.33 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3390 | 50.9 | 50.3 | $-1067.41 | -3.1% | $-67.41 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2830 | 49.5 | 49.4 | $-1292.87 | -4.6% | $-292.87 | -2.4 | done | losing for real |
| value_ev5 | 2447 | 40.3 | 41.1 | $-1324.34 | -5.4% | $-324.34 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 2830 | 50.5 | 51.1 | $-1670.19 | -5.9% | $-670.19 | -3.2 | done | losing for real |
| trend_filter | 1997 | 48.7 | 50.4 | $-1693.24 | -8.5% | $-693.24 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3390 | 49.1 | 50.2 | $-2135.86 | -6.3% | $-1135.86 | -3.7 | done | losing for real |
| coinflip | 4874 | 50.1 | 50.1 | $-2185.75 | -4.5% | $-1185.75 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4874 | 50.2 | 51.4 | $-2975.16 | -6.1% | $-1975.16 | -4.4 | done | losing for real |
| always_up | 4874 | 47.8 | 49.3 | $-3589.98 | -7.4% | $-2589.98 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7925 | 48.0 | 48.9 | $-4679.77 |
| ETH | 8555 | 48.1 | 48.3 | $-5045.63 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
